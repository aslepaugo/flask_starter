from flask_login import login_user, logout_user, current_user
from flask import Blueprint, render_template, flash, redirect, url_for

from webapp.db import db
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    title = "Authorization"
    login_form = LoginForm()

    return render_template(
        'user/login.html',
        page_title=title,
        form=login_form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash("You've logged in successfully")

            return redirect(url_for('news.index'))

    flash("Incorrect login or password")

    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash("You have been successfully loged out")
    return redirect(url_for('news.index'))


@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    title = "Registration"
    form = RegistrationForm()
    return render_template('user/registration.html', page_title=title, form=form)


@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        news_user = User(
            username=form.username.data,
            email=form.email.data,
            role='user')
        news_user.set_password(form.password.data)
        db.session.add(news_user)
        db.session.commit()
        flash("You have been successfully registered")

        return redirect(url_for('user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Error in field "{}": - {}'.format(
                    getattr(form, field).label.text,
                    error)
                )
        return redirect(url_for('user.register'))
