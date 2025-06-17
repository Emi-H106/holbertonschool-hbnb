import uuid

class User:
    def __init__(self, first_name, last_name, email, id=None):
        self.id = id if id else str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def update(self, data):
        """Update user information based on the provided data."""
        if 'first_name' in data:
            self.first_name = data['first_name']
        if 'last_name' in data:
            self.last_name = data['last_name']
        if 'email' in data:
            self.email = data['email']

    def to_dict(self):
        """Convert the user object to a dictionary."""
        return {
                'id': self.id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email
        }

