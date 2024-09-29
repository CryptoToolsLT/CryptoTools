from flask import Flask
from flask_login import LoginManager, UserMixin # type: ignore
from ..plugins.models import db, User

login_manager = LoginManager()

def register_login_manager(app: Flask):
    login_manager.init_app(app) # type: ignore

class AuthUser(UserMixin):
    def __init__(self, id: int, email: str, full_name: str):
        self.id = id
        self.email = email
        self.full_name = full_name
        super().__init__()

@login_manager.user_loader # type: ignore
def load_user(user_id: str):
    user = db.session.get(User, int(user_id))
    if user is None:
        return None
    return AuthUser(
        id=user.id,
        email=user.email,
        full_name=user.full_name,
    )
