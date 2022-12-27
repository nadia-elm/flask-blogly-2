"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

default_image = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement= True)

    first_name=db.Column(db.String(30),
                            nullable= False,)

    last_name=db.Column(db.String(30))

    image_url=db.Column(db.String, default = default_image)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

