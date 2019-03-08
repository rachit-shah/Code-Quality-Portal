"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect, request, url_for
from CodeQualityPortal.forms import SubmitRepositoryForm, ChooseMetricsForm
from CodeQualityPortal import app
import logging
import json

logger = logging.getLogger(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Renders the home page."""
    form = SubmitRepositoryForm()
    if request.method == "POST":
        if form.validate_on_submit():
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
