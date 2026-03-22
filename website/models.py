from . import Db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(Db.Model, UserMixin):
    id = Db.Column(Db.Integer, primary_key=True)
    email = Db.Column(Db.String(150), unique=True, nullable=False)
    username = Db.Column(Db.String(150), unique=True, nullable=False)
    password = Db.Column(Db.String(150), nullable=False)
    date_created = Db.Column(Db.DateTime(timezone=True), default=func.now())