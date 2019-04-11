from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, Optional

class SubmitRepositoryForm(FlaskForm):
    repo_url = StringField('Repository URL', validators=[DataRequired()])
    access_token = StringField('Access Token', validators=[DataRequired()])
    submit = SubmitField('GO')

class ChooseMetricsForm(FlaskForm):
    class_hierarchy_level = BooleanField('Class Hierarchy Level', validators=[Optional()])
    no_of_methods_per_class = BooleanField('Number of Methods per Class', validators=[Optional()])
    cyclomatic_complexity = BooleanField('Cyclomatic Complexity per Class', validators=[Optional()])
    comments_or_documentation = BooleanField('Number of Comment Lines per Class:', validators=[Optional()])
    lines_of_code = BooleanField('Lines of Code', validators=[Optional()])
    no_of_collaborators_per_file = BooleanField('Number of Collaborators for Repository', validators=[Optional()])
    submit = SubmitField('GO')

    def validate(self):
        if not super(ChooseMetricsForm, self).validate():
            return False
        if not self.class_hierarchy_level.data and \
            not self.no_of_methods_per_class.data and \
            not self.cyclomatic_complexity.data and \
            not self.comments_or_documentation.data and \
            not self.lines_of_code.data and \
            not self.no_of_collaborators_per_file.data:

            error = "You must choose at least one metric."
            self.submit.errors.append(error)
            return False
        return True