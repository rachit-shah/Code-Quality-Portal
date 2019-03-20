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
import json

logger = logging.getLogger(__name__)

url_root = "https://api.github.com"

token = "8fede56e8b1ee9ac65d84b4b2b9ccec65c19d7db"

headers = {
    "content-type": "application/json",
    "Authorization": "token " + token,
    "Accept": "application/vnd.github.squirrel-girl-preview+json",
}


def parse_file_content(content, param):
    pass


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


            for x in tree:
                if ".java" in x["path"]:
                    response = requests.get(x["url"])
                    response = response.json()["content"]
                    content = base64.b64decode(response)

                    parse_file_content(content, x["path"].split("/")[-1])


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



