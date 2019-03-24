"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect, request, url_for
from CodeQualityPortal.forms import SubmitRepositoryForm, ChooseMetricsForm
from CodeQualityPortal import app
from CodeQualityPortal import sql_db
import logging
import requests
import os
import base64
import re
import json

logger = logging.getLogger(__name__)

url_root = "https://api.github.com"

token = "8fede56e8b1ee9ac65d84b4b2b9ccec65c19d7db"

headers = {
    "content-type": "application/json",
    "Authorization": "token " + token,
    "Accept": "application/vnd.github.squirrel-girl-preview+json",
}


class ClassContent(object):

    def __init__(self, file_name):
        self.file_name = file_name
        self.first_line = None
        self.last_line = None
        self.parents = []
        self.no_of_methods = None
        self.no_of_comments = 0
        self.cyclomatic_complexity = None
        self.no_of_objects = None


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
                class_objects[class_stack[-1]].no_of_comments+=1

            multi_comment_flag=False

        if multi_comment_flag:
            if class_stack:
                class_objects[class_stack[-1]].no_of_comments+=1
            continue

        prev = line
        line = line.split("//")[0]
        if prev != line:
            if class_stack:
                class_objects[class_stack[-1]].no_of_comments+=1
        words = line.split(" ")

        if "/*" in line:
            multi_comment_flag=True
            continue

        

         # Total Number of Classes   
        if "class" in words:

            # create class object
            class_content = ClassContent(file_name)

            # save line where class is found
            class_content.first_line = i

            # get class name and store objects
            class_name = strip_generalize_class(words[words.index("class")+1])

            #Add parent of the current class if it exists (for nested classes)
            if class_stack:
                class_content.parents.append(class_stack[-1])


            if "extends" in words:
                class_content.parents.append(strip_generalize_class(words[words.index("extends")+1]))

            if "implements" in words:
                t = line[line.index("implements")+11:]
                p = t.split(",")

                for x in p[:len(p)-1]:
                    class_content.parents.append(strip_generalize_class(x))

                if "{" in p[len(p)-1]:
                    last = p[len(p)-1].strip()[:-1]
                else:
                    last = p[len(p)-1]
                class_content.parents.append(strip_generalize_class(last))

            #Lines of code
            if "{" in line:
                class_size_pointer[class_name] = 1
            else:
                class_size_pointer[class_name] = -1
            class_stack.append(class_name)
            class_objects[class_name] = class_content
        elif "{" in line:
            recent_class = class_stack[-1]
            if class_size_pointer[recent_class]==-1:
                class_size_pointer[recent_class] = 1
            else:
                other+=1
        if "}" in line:
            if other==0:
                recent_class = class_stack.pop()
                class_size_pointer[recent_class] = 0
                class_objects[recent_class].last_line = i
            else:
                other -= 1

        #Number of methods per class
        if "=" not in line and re.match(function_regex,line):
            if class_objects[class_stack[-1]].no_of_methods is None:
                class_objects[class_stack[-1]].no_of_methods=0
            class_objects[class_stack[-1]].no_of_methods+=1

        








@app.route('/', methods=['GET', 'POST'])
def index():
    """Renders the home page."""
    form = SubmitRepositoryForm()
    if request.method == "POST":
        if form.validate_on_submit():
            repo_url = request.form["repo_url"]
            data = repo_url.split("/")
            owner = data[3]
            repo_name = data[4]

            repo_root_url = os.path.join(url_root, "repos", owner, repo_name, "branches/master")
            response = requests.get(repo_root_url, headers=headers)

            response = response.json()
            tree_sha = response["commit"]["sha"]
            repo_tree_url = os.path.join(url_root, "repos", owner, repo_name, "git/trees", tree_sha+"?recursive=1")

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
                        if x["path"].split("/")[-1] == "HEncoder.java":
                            print(content)


                        parse_file_content(content, x["path"].split("/")[-1], class_objects)



            sql_db.mock_database_generator()
            return redirect('/choose-metric')

    return render_template(
        'index.html',
        form=form
    )

@app.route('/choose-metric', methods=['GET', 'POST'])
def choose_metric():
    """Renders the contact page."""
    form = ChooseMetricsForm()
    if request.method == "POST":
        if form.validate_on_submit():
            metrics = []
            print(request.form)
            if 'class_hierarchy_level' in request.form:
                metrics.append('Class Hierarchy Level')
            if 'no_of_collaborators_per_file' in request.form:
                metrics.append('No. of Collaborators per File')
            if 'no_of_methods_per_class' in request.form:
                metrics.append('No. of Methods per Class')
            if 'cyclomatic_complexity' in request.form:
                metrics.append('Cyclomatic Complexity')
            if 'coupling_between_objects' in request.form:
                metrics.append('Coupling between Objects')
            if 'comments_or_documentation' in request.form:
                metrics.append('Comments or Documentation')
            if 'lines_of_code' in request.form:
                metrics.append('Lines of Code')
            if 'avg_faults' in request.form:
                metrics.append('Average Faults')

            return redirect(url_for('visualisations', metrics=metrics))

    return render_template(
        'choose-metric.html',
        form=form
    )

@app.route('/visualisations', methods=['GET', 'POST'])
def visualisations():
    """Renders the about page."""
    metrics = request.args.getlist('metrics')
    print(metrics)
    return render_template(
        'visualisations.html',
        metrics=metrics
    )



