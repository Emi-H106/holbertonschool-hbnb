from app.models.__init__ import BaseModel  #create the class User with BaseModel

class User(BaseModel):
    def __init__(self, email, first_name, last_name):
        super().__init__()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

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
        self._email = value

    def to_dict(self):
        """Convert the user object to a dictionary."""
        return {
                'id': self.id,
                'email': self.email,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'created.at': self.created_at.isoformat(),
                'updated_at': self.updated_at.isoformat()
        }
