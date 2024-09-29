from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def register_migrate(app: Flask, db: SQLAlchemy) -> Migrate:
    migrate = Migrate(app, db)
    return migrate
