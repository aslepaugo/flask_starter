from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


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
        validators=[DataRequired()],
        render_kw={"class": "form-control"})
    password = PasswordField(
        "Password",
        validators=[DataRequired()],
        render_kw={"class": "form-control"})
    password2 = PasswordField(
        "Repeat Password",
        validators=[DataRequired()],
        render_kw={"class": "form-control"})
    submit = SubmitField(
        "Register",
        render_kw={"class": "btn btn-primary"})
