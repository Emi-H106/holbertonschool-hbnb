from app.models.__init__ import BaseModel  #create the class User with BaseModel
import re
from app.extensions import bcrypt


class User(BaseModel):
    def __init__(self, email, first_name, last_name, password=None, is_admin=False):
        super().__init__()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.is_admin = is_admin
        if password:
            self.hash_password(password)
    
    def update(self, data):
        """Update user attributes with the provided data."""
        if 'first_name' in data:
            self.first_name = data['first_name']
        if 'last_name' in data:
            self.last_name = data['last_name']
        if 'email' in data:
            self.email = data['email']
        if 'password' in data:
            self.hash_password(data['password'])
        if 'is_admin' in data:
            self.is_admin = data['is_admin']

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not value:
            raise ValueError("First name cannot be empty.")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not value:
            raise ValueError("Last name cannot be empty.")
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not value:
            raise ValueError("Email cannot be empty.")
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, value):
            raise ValueError("Invalid email format.")
        
        self._email = value


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)

    def to_dict(self):
        """Convert the user object to a dictionary."""
        return {
                'id': str(self.id),  # Ensure id is a string
                'email': self.email,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'created_at': self.created_at.isoformat(),
                'updated_at': self.updated_at.isoformat()
        }
