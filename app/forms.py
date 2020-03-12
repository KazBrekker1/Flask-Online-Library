from flask_wtf import FlaskForm
from app.models import User
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, url, Email


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=18)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=8, max=18), EqualTo('password')])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username Is Already Registered')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('E-mail Is Already Registered')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=18)])
    submit = SubmitField("Sign In")


class MovieForm(FlaskForm):
    title = StringField('Movie Name', validators=[DataRequired(), Length(min=10, max=50)])
    link = URLField('Movie Link', validators=[DataRequired(), url()])
    watched = BooleanField('Watched')
    anime = BooleanField('Animation')
    dubbed = BooleanField('Dubbed')
    submit = SubmitField("Submit")


class SeriesForm(FlaskForm):
    title = StringField('Series Name', validators=[DataRequired(), Length(min=10, max=50)])
    link = URLField('Movie Link', validators=[DataRequired(), url()])
    watching = BooleanField('Watching')
    anime = BooleanField('Animation')
    dubbed = BooleanField('Dubbed')
    submit = SubmitField("Submit")


class BookForm(FlaskForm):
    title = StringField('Book Name', validators=[DataRequired(), Length(min=10, max=50)])
    writer = StringField('Book Writer', validators=[DataRequired()])
    link = URLField('Movie Link', validators=[DataRequired(), url()])
    pages = IntegerField('Number Of Pages', validators=[DataRequired()])
    finished = BooleanField('Finished')
    submit = SubmitField("Submit")
