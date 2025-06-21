from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


# Registration Form
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired( ), Length(min=2, max=20)], render_kw={"style": "background-color: #282830; color: #dddddd"})
    email = StringField('Email',
                        validators=[DataRequired( ), Email( )], render_kw={"style": "background-color: #282830; color: #dddddd"})
    password = PasswordField('Password', validators=[DataRequired( )], render_kw={"style": "background-color: #282830; color: #dddddd"})
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired( ), EqualTo('password')], render_kw={"style": "background-color: #282830; color: #dddddd;"})
    submit = SubmitField('Sign Up')

    @staticmethod
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first( )
        if user:
            raise ValidationError("That username is taken. Please choose a different one")

    @staticmethod
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first( )
        if user:
            raise ValidationError("That email is taken. Please choose a different one")


# Login Form
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired( ), Email( )], render_kw={"style": "background-color: #282830; color: #dddddd"})
    password = PasswordField('Password', validators=[DataRequired( )], render_kw={"style": "background-color: #282830; color: #dddddd"})
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


# (7) User Account and User Picture
# Update Form
class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)], render_kw={"style": "background-color: #282830; color: #dddddd"})
    email = StringField('Email',
                        validators=[DataRequired(), Email()], render_kw={"style": "background-color: #282830; color: #dddddd"})
    picture = FileField("Update Profile Picture", validators=[FileAllowed(["jpg", "png", "jpeg"])])
    submit = SubmitField('Update')

    @staticmethod
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("That username is taken. Please choose a different one")

    @staticmethod
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("That email is taken. Please choose a different one")


# (8) Create, Update and Delete Posts
class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()], render_kw={"style": "background-color: #282830; color: #dddddd; font-size: 18px;"})
    content = TextAreaField("Content", validators=[DataRequired()],  render_kw={"style": "background-color: #282830; color: #dddddd;  font-size: 18px; border-color: #444444;"})
    submit = SubmitField("Post")


# (10) Email and Password Reset
class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()], render_kw={"style": "background-color: #282830; color: #dddddd"})
    submit = SubmitField("Request Password Reset")

    @staticmethod
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError("There is no account with that email. You must register first.")


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"style": "background-color: #282830; color: #dddddd"})
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')], render_kw={"style": "background-color: #282830; color: #dddddd;"})
    submit = SubmitField("Reset Password")
