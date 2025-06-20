from app.models.__init__ import BaseModel

class Review(BaseModel):
    def __init__(self, user_id, place_id, text, rating=5, **kwargs):
        super().__init__()

        self.user_id = user_id
        self.place_id = place_id
        self.text = text
        self.rating = rating  # optional, default to 5

    def to_dict(self):
        """Serialize the review instance to a dictionary"""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "place_id": self.place_id,
            "text": self.text,
            "rating": self.rating,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

