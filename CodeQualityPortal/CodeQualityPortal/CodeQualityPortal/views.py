"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect, request
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
                metrics.append('class_hierarchy_level')
            if 'no_of_methods_per_class' in request.form:
                metrics.append('no_of_methods_per_class')
            if 'cyclomatic_complexity' in request.form:
                metrics.append('cyclomatic_complexity')
            if 'coupling_between_objects' in request.form:
                metrics.append('coupling_between_objects')
            if 'comments_or_documentation' in request.form:
                metrics.append('comments_or_documentation')
            if 'lines_of_code' in request.form:
                metrics.append('lines_of_code')
            if 'avg_faults' in request.form:
                metrics.append('avg_faults')
            if 'no_of_collaborators_per_file' in request.form:
                metrics.append('no_of_collaborators_per_file')

            metrics = json.dumps(metrics)
            print(metrics)
            return render_template('visualisations.html',
                                   title='About',
                                   year=datetime.now().year,
                                   message=metrics)

    return render_template(
        'choose-metric.html',
        form=form
    )

@app.route('/visualisations', methods=['GET', 'POST'])
def visualisations():
    """Renders the about page."""
    return render_template(
        'visualisations.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
