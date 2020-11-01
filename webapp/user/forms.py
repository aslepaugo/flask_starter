from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from webapp.user.models import User

class LoginForm(FlaskForm):
    username = StringField(
        "User Name",
        validators=[DataRequired()],
        render_kw={"class": "form-control"})
    password = PasswordField(
        "Password",
        validators=[DataRequired()],
        render_kw={"class": "form-control"})
    submit = SubmitField(
        "Login",
        render_kw={"class": "btn btn-primary"})
    remember_me = BooleanField(
        "Remember me",
        default=False,
        render_kw={"class": "form-check-input"})


class RegistrationForm(FlaskForm):
    username = StringField(
        "User Name",
        validators=[DataRequired()],
        render_kw={"class": "form-control"})
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()],
        render_kw={"class": "form-control"})
    password = PasswordField(
        "Password",
        validators=[DataRequired()],
        render_kw={"class": "form-control"})
    password2 = PasswordField(
        "Repeat Password",
        validators=[DataRequired(), EqualTo('password')],
        render_kw={"class": "form-control"})
    submit = SubmitField(
        "Register",
        render_kw={"class": "btn btn-primary"})

    def validate_username(self, username):
        user_count = User.query.filter_by(username=username.data).count()
        if user_count > 0:
            raise ValidationError("User with this name is already exists")

    def validate_email(self, email):
        user_count = User.query.filter_by(email=email.data).count()
        if user_count > 0:
            raise ValidationError("User with this email is already exists")
