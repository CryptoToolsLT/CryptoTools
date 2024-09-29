from flask import redirect
from flask_login import logout_user as flask_logout_user # type: ignore

def logout_user():
    flask_logout_user()
    return redirect('/')
