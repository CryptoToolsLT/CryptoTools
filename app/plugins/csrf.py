from flask import Flask
from flask_wtf.csrf import CSRFProtect # type: ignore

def register_csrf_protection(app: Flask):
    csrf = CSRFProtect()
    csrf.init_app(app) # type: ignore
