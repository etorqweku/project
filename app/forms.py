from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,SelectField,TextAreaField
from wtforms.validators import DataRequired,ValidationError,Email,EqualTo,Length
from app.models import Agent,Client
from flask_wtf.file import FileField,FileRequired,FileAllowed
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class AgentRegistrationForm(FlaskForm):
    name = StringField('Full Name',validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    proffession = SelectField(u'Proffession', choices=[('','--select--'),('DJ','DJ'),('MC','MC'),('Caterer','Caterer'),('Usher','Usher'),('Photographer','Photographer'),('Event Organizer','Event Organizer')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        agent = Agent.query.filter_by(username=username.data).first()
        if agent is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        agent = Agent.query.filter_by(email=email.data).first()
        if agent is not None:
            raise ValidationError('Please use a different email address.')


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    contact = TextAreaField('Contact', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

class ClientRegistrationForm(FlaskForm):
    name = StringField('Full Name',validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        client = Client.query.filter_by(username=username.data).first()
        if client is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        client = Client.query.filter_by(email=email.data).first()
        if client is not None:
            raise ValidationError('Please use a different email address.')

class UploadForm(FlaskForm):
    image        = FileField('Choose file', validators=[FileRequired(), FileAllowed(['jpg','png','mp4'],'Images or Videos only')])
    description  = TextAreaField(u'Image Description')
    submit = SubmitField('Upload')