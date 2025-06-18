from app.models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email, id=None):
        super().__init__()
        if id:
            self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def to_dict(self):
        """Convert the user object to a dictionary."""
        return {
                'id': self.id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email,
                'created.at': self.created_at.isoformat(),
                'updated_at': self.updated_at.isoformat()
        }
