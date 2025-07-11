from app.models.__init__ import BaseModel
from sqlalchemy.orm import validates, relationship
from app.extensions import bcrypt
from app import db
import re

class User(BaseModel, db.Model):
    __tablename__ = 'user'

    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    places = relationship('Place', backref='owner', lazy=True)
    reviews = relationship('Review', backref='author', lazy=True)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        """Hashes the password before storing it."""
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password_hash, password)

    @validates('email')
    def validate_email(self, key, email):
        if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
            raise ValueError("Email is not conforme to standar")
        return email

    @validates('first_name')
    def validate_first_name(self, key, first_name):
        if len(first_name) > 50:
            raise ValueError("First name too long")
        if not first_name:
            raise ValueError("First name mustn't be empty")
        return first_name

    @validates('last_name')
    def validate_last_name(self, key, last_name):
        if len(last_name) > 50:
            raise ValueError("Last name too long")
        if not last_name:
            raise ValueError("Last name mustn't be empty")
        return last_name

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
        }

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
