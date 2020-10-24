from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired


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
