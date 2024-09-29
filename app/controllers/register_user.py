from flask import render_template
from flask import flash, redirect
import typing

from ..plugins.models import db, User

from ..utils.password import hash_password
from ..utils.notification import Notification
from ..utils.validation import StrValidation, validation_error

class RegisterForm(typing.TypedDict):
    email: str
    full_name: str
    password: str
    confirm_password: str

def _validation_error(form: RegisterForm) -> str|None:
    err = validation_error([
        StrValidation('email', "email", form['email']),
        StrValidation('name', "full name", form['full_name']),
        StrValidation('password', "password", form['password']),
    ])

    if err:
        return err

    if form['password'] != form['confirm_password']:
        return "confirm password mismatch"

    return None

def _database_error(form: RegisterForm) -> str|None:
    email = form['email']
    full_name = form['full_name']
    password = form['password']

    password_hash = hash_password(password)

    try:
        user = User(
            email=email, # type: ignore
            full_name=full_name, # type: ignore
            password_hash=password_hash, # type: ignore
        )
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        if "Duplicate entry" in str(e):
            e = "Email already exists"
        else:
            e = "Database error: " + str(e)
        return e
    
    return None

def register_user(form: RegisterForm):
    err = _validation_error(form) or _database_error(form)
    if err:
        return render_template("register.html", notifications=[
            Notification('error', err),
        ])

    flash("You have successfully registered, please login.", 'success')
    return redirect('/login')
