from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Optional

class SubmitRepositoryForm(FlaskForm):
    repo_url = StringField('Repository URL', validators=[DataRequired()])
    private = BooleanField('Private?', validators=[Optional()])
    access_token = StringField('Access Token', validators=[Optional()])
    submit = SubmitField('GO')

    def validate(self):
        if not super(SubmitRepositoryForm, self).validate():
            return False
        if self.private.data == True and not self.access_token.data:
            error = "If Repository is private you must give an Access Token"
            self.access_token.errors.append(error)
            return False
        return True