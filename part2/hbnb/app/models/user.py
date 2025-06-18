from app.models.__init__ import BaseModel

class User(BaseModel):
    def __init__(self, email, first_name, last_name):
        super().__init__()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        

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
