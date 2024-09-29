from flask import render_template, flash, redirect, request
from flask_login import login_user as flask_login_user, login_required # type: ignore
import typing

from ..plugins.models import db, User
from ..plugins.auth import AuthUser

from ..utils.password import check_password
from ..utils.notification import Notification
from ..utils.validation import StrValidation, validation_error
from ..utils.safe_redirect import get_safe_redirect

class LoginForm(typing.TypedDict):
    email: str
    password: str

def _validation_error(form: LoginForm) -> str|None:
    err = validation_error([
        StrValidation('email', "email", form['email']),
        StrValidation('password', "password", form['password']),
    ])
    if err:
        return err
    return None

def _database_error(form: LoginForm) -> str|None:
    email = form['email']
    password = form['password']

    user = db.session.execute(
        db.select(User).filter_by(email=email)
    ).scalar_one_or_none()

    if not user:
        return "No account with this email. Please register a new account!"

    if not check_password(password, user.password_hash):
        return "Wrong password"
    
    flask_login_user(AuthUser(
        id=user.id, email=user.email,
        full_name=user.full_name,
    ))

    return None

def login_user(form: LoginForm):
    err = _validation_error(form) or _database_error(form)
    if err:
        return render_template("login.html", notifications=[
            Notification('error', err),
        ])
    
    next = get_safe_redirect(request.args.get('next'))

    flash("Successfully logged in. Let's explore our best tools!", 'success')
    return redirect(next)
