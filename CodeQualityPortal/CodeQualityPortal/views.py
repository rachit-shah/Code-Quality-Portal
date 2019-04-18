"""
Routes and views for the flask application.
"""
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from flask import render_template, redirect, request, url_for, Response
from CodeQualityPortal.forms import SubmitRepositoryForm, ChooseMetricsForm
from CodeQualityPortal import app
from CodeQualityPortal import sql_db
import logging
import requests
import os
import base64
import re
import math
import json
import lizard
import subprocess
import pandas as pd
import time

logger = logging.getLogger(__name__)

url_root = "https://api.github.com"
headers = {
    "content-type": "application/json",
    "Accept": "application/vnd.github.squirrel-girl-preview+json",
}


def update_repo_data():
    result = sql_db.get_urls()
    for repo_root_url, token in result:

        owner = repo_root_url.split("/")[4]
        repo_name = repo_root_url.split("/")[5]
        print(owner,repo_name)
        headers["Authorization"] = "token " + token
        response = requests.get(repo_root_url, headers=headers)
        response = response.json()
        tree_sha = response["commit"]["sha"]
        repo_tree_url = os.path.join(url_root, "repos", owner, repo_name, "git/trees", tree_sha + "?recursive=1")

        response = requests.get(repo_tree_url, headers=headers)
        response = response.json()

        tree = response["tree"]

        class_objects = {}
        for x in tree:
            if ".java" in x["path"]:
                response = requests.get(x["url"], headers=headers)
                if "content" in response.json():
                    response = response.json()["content"]
                    content = base64.b64decode(response)
                    file_name = x["path"].split("/")[-1]

                    parse_file_content(str(content, "utf-8"), file_name, class_objects)
                    calculate_cyclomatic_complexity(file_name, content, class_objects)

        calculate_coupling_and_collaborators(class_objects, token, owner, repo_name, repo_root_url)

scheduler = BackgroundScheduler()
scheduler.add_job(update_repo_data, 'interval', hours=1)
scheduler.start()



class ClassContent(object):

    def __init__(self, file_name):
        self.file_name = file_name
        self.first_line = 0
        self.last_line = 0
        self.parents = []
        self.no_of_methods = 0
        self.no_of_comments = 0
        self.cyclomatic_complexity = 0
        self.coupling = 0


def strip_generalize_class(class_name):
    if "<" in class_name:
        class_name = class_name[:class_name.index("<")]
    return class_name.replace("{","").strip()


def delete_temp_files():

    folder='temp'
    for file in os.listdir(folder):
        file_path=os.path.join(folder,file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
    for file in os.listdir('.'):
        if file.split('.')[-1]=='csv':
            try:
                os.unlink(file)
            except Exception as e:
                print(e)


def parse_file_content(content, file_name, class_objects):
    function_regex = "(public|protected|private|static|abstract|synchronized|final|transient|volatile|native|strictfp|\s)*[\w\<\>\[\]]+\s+(\w+) *\([^\)]*\) *(\{?|[^;])"
    lines = content.split("\n")

    class_size_pointer = {}
    other = 0
    class_stack = []
    multi_comment_flag = False
    for i, line in enumerate(lines):
        if "*/" in line:
            if class_stack:
                class_objects[class_stack[-1]].no_of_comments += 1

            multi_comment_flag = False

        if multi_comment_flag:
            if class_stack:
                class_objects[class_stack[-1]].no_of_comments += 1
            continue

        prev = line
        line = line.split("//")[0]
        if prev != line:
            if class_stack:
                class_objects[class_stack[-1]].no_of_comments += 1
        words = line.split(" ")

        if "/*" in line:
            if "*/" in line:
                continue
            multi_comment_flag = True
            continue

        if "class" in words or "interface" in words:

            # create class object
            class_content = ClassContent(file_name)

            # save line where class is found
            class_content.first_line = i

            # get class name and store objects
            if "interface" in words:
                class_name = strip_generalize_class(words[words.index("interface") + 1])
            else:
                class_name = strip_generalize_class(words[words.index("class") + 1])

            # Add parent of the current class if it exists (for nested classes)
            if class_stack:
                class_content.parents.append(class_stack[-1])

            if "extends" in words:
                class_content.parents.append(strip_generalize_class(words[words.index("extends") + 1]))

            if "implements" in words:
                t = line[line.index("implements") + 11:]
                p = t.split(",")

                for x in p[:len(p) - 1]:
                    class_content.parents.append(strip_generalize_class(x))

                if "{" in p[len(p) - 1]:
                    last = p[len(p) - 1].strip()[:-1]
                else:
                    last = p[len(p) - 1]
                class_content.parents.append(strip_generalize_class(last))

            # Lines of code
            if "{" in line:
                class_size_pointer[class_name] = 1
            else:
                class_size_pointer[class_name] = -1
            class_stack.append(class_name)
            class_objects[class_name] = class_content
        elif "{" in line:
            open_braces = line.count("{")
            if not class_stack:
                other += open_braces
                continue
            recent_class = class_stack[-1]
            if class_size_pointer[recent_class] == -1:
                class_size_pointer[recent_class] = 1
                open_braces -= 1
                other += open_braces
            else:
                other += open_braces
        if "}" in line:
            close_braces = line.count("}")
            if other == 0:
                recent_class = class_stack.pop()
                class_size_pointer[recent_class] = 0
                class_objects[recent_class].last_line = i
            else:
                other -= close_braces
                if other < 0:
                    count_class = math.abs(other)
                    for j in range(count_class):
                        recent_class = class_stack.pop()
                        class_size_pointer[recent_class] = 0
                        class_objects[recent_class].last_line = j
                    other = 0

        # Number of methods per class
        if "=" not in line and re.match(function_regex, line):
            if class_objects[class_stack[-1]].no_of_methods is None:
                class_objects[class_stack[-1]].no_of_methods = 0
            class_objects[class_stack[-1]].no_of_methods += 1


def calculate_coupling_and_collaborators(class_objects, token, owner, repo_name, repo_root_url):
    # Coupling Between Objects
    #os.system("java -jar ck.jar temp")
    subprocess.call(['/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java', '-jar', 'ck.jar', 'temp'])
    df = pd.read_csv("class.csv", usecols=['class', 'cbo'], index_col=False)
    df["class"] = df["class"].map(lambda x: strip_generalize_class(x.split(".")[-1]))

    for _, row in df.iterrows():
        if row['class'] in class_objects:
            class_objects[row['class']].coupling = int(row['cbo'])

    header = {
            "content-type": "application/json",
            "Authorization": "token " + token,
            'Accept': 'application/vnd.github.hellcat-preview+json'
    }
    response_collab = requests.get(url_root + '/repos/' + owner + '/' + repo_name + '/stats/contributors',
                                   headers=header)
    response_collab = response_collab.json()
    r = response_collab[-1]
    major_collab = r["author"]["login"]

    total_collab = 0
    for i in range(1, 10):
        response = requests.get(
            url_root + '/repos/' + owner + '/' + repo_name + '/contributors?page=' + str(i) + '&per_page=1000',
            headers=header)
        response = response.json()
        total_collab += len(response)

    delete_temp_files()
    sql_db.save_url(repo_root_url, token)
    sql_db.mock_database_generator(class_objects, repo_name, major_collab, total_collab)

def calculate_cyclomatic_complexity(file_name, content, class_objects):
    with(open("temp/" + file_name, "w")) as f:
        f.write(str(content, "utf-8"))
        f.close()
    cmd = ["lizard", "--csv", "temp/" + file_name]
    with open('out.csv', 'w') as fout:
        subprocess.call(cmd, stdout=fout, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        fout.close()

    df = pd.read_csv("out.csv", header=None,
                     names=['nloc', 'ccn', 'token', 'param', 'length', 'location', 'filename', 'methodname',
                            'methodparams', 'a', 'b'])

    df["class_name"] = df["location"].map(lambda x: str(x).split("@")[0])
    for i in range(len(df)):
        try:
            df.at[i, "class_name"] = strip_generalize_class(df.at[i, "class_name"].split("::")[-2])
        except:
            df.at[i, "class_name"] = None
    class_ccn = df.groupby("class_name")["ccn"].max()
    for key, val in class_ccn.iteritems():
        if key in class_objects:
            class_objects[key].cyclomatic_complexity = val


@app.route('/', methods=['GET', 'POST'])
def index():
    """Renders the home page."""

    form = SubmitRepositoryForm()

    if request.method == "POST":
        if form.validate_on_submit():
            repo_name = ""
            owner = ""
            token = ""
            try:
                repo_url = request.form["repo_url"]
                token = request.form["access_token"]
                data = repo_url.split("/")
                owner = data[3]
                repo_name = data[4]
            except:
                form.repo_url.errors.append("Invalid Github Repository URL")

            return render_template(
                'index.html',
                form=form,
                repo_name=repo_name,
                owner=owner,
                token=token,
                flag="1"
            )

    return render_template(
        'index.html',
        form=form,
        repo_name="",
        owner="",
        token="",
        flag="0"
    )


@app.route('/progress/<repo_name>/<owner>/<token>')
def progress(repo_name, owner, token):

    def generate():
        headers["Authorization"] = "token " + token

        repo_root_url = os.path.join(url_root, "repos", owner, repo_name, "branches/master")

        result = sql_db.check_table()
        if result and any(repo_root_url in s for s in result):
            yield "data:" + "100" + "\n\n"
        else:
            response = requests.get(repo_root_url, headers=headers)
            if response.status_code != 200:
                yield "data:" + "99" + "\n\n"
            else:
                response = response.json()
                tree_sha = response["commit"]["sha"]
                repo_tree_url = os.path.join(url_root, "repos", owner, repo_name, "git/trees", tree_sha + "?recursive=1")

                response = requests.get(repo_tree_url, headers=headers)
                response = response.json()

                tree = response["tree"]

                class_objects = {}
                for x in tree:
                    if ".java" in x["path"]:
                        response = requests.get(x["url"], headers=headers)
                        if "content" in response.json():
                            response = response.json()["content"]
                            content = base64.b64decode(response)
                            file_name = x["path"].split("/")[-1]

                            yield "data:" + x["path"] + "\n\n"

                            parse_file_content(str(content, "utf-8"), file_name, class_objects)
                            calculate_cyclomatic_complexity(file_name, content, class_objects)
                calculate_coupling_and_collaborators(class_objects, token, owner, repo_name, repo_root_url)
                yield "data:" + "100" + "\n\n"
    return Response(generate(), mimetype='text/event-stream')


@app.route('/choose-metric', methods=['GET', 'POST'])
def choose_metric():
    """Renders the contact page."""
    form = ChooseMetricsForm()
    if request.method == "POST":
        if form.validate_on_submit():
            metrics = []
            if 'comments_or_documentation' in request.form:
                metrics.append('Comments or Documentation')
            if 'no_of_methods_per_class' in request.form:
                metrics.append('No. of Methods per Class')
            if 'cyclomatic_complexity' in request.form:
                metrics.append('Cyclomatic Complexity')
            if 'no_of_collaborators_per_file' in request.form:
                metrics.append('No. of Collaborators per File')
            if 'lines_of_code' in request.form:
                metrics.append('Lines of Code')
            if 'class_hierarchy_level' in request.form:
                metrics.append('Class Hierarchy Level')
            if 'coupling_between_objects' in request.form:
                metrics.append('Coupling Between Objects')

            return redirect(url_for('visualisations', metrics=metrics))

    return render_template(
        'choose-metric.html',
        form=form
    )


@app.route('/visualisations', methods=['GET', 'POST'])
def visualisations():
    """Renders the about page."""
    metrics = request.args.getlist('metrics')
    return render_template(
        'visualisations.html',
        metrics=metrics
    )



