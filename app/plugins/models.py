from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.mysql import LONGTEXT, VARCHAR
from ..env import (
    MYSQL_HOSTNAME, MYSQL_HOSTPORT,
    MYSQL_USERNAME, MYSQL_PASSWORD,
    MYSQL_DATABASE,
)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class User(db.Model):
    id: Mapped[int] = mapped_column(nullable=False, primary_key=True)
    email: Mapped[str] = mapped_column(VARCHAR(321), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(VARCHAR(256), nullable=False)
    full_name: Mapped[str] = mapped_column(LONGTEXT, nullable=False)

def register_models(app: Flask) -> SQLAlchemy:
    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}:{MYSQL_HOSTPORT}/{MYSQL_DATABASE}"
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return db
