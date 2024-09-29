from flask import Flask
from .plugins.models import register_models
from .plugins.migrate import register_migrate
from .plugins.auth import register_login_manager
from .plugins.csrf import register_csrf_protection
from .plugins.routes import register_routes
from .env import SECRET_KEY

app = Flask(__name__)

app.config.update(SECRET_KEY=SECRET_KEY) # type: ignore

db = register_models(app)
migrate = register_migrate(app, db)
register_csrf_protection(app)
register_login_manager(app)
register_routes(app)
