"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect
from CodeQualityPortal.forms import SubmitRepositoryForm
from CodeQualityPortal import app
import logging

logger = logging.getLogger(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    """Renders the home page."""
    form = SubmitRepositoryForm()
    if form.validate_on_submit():
       return redirect('/contact')

    print(form.errors.items())
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        form=form
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
