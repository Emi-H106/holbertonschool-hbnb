from app.models.__init__ import BaseModel
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import validates

class Place(BaseModel):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, nullable=False)
    title = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    city = Column(String(128), nullable=False)
    price = Column(Float, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    @validates('title')
    def validate_title(self, key, value):
        if value == "" or len(value) > 100:
            raise ValueError("Title cannot be empty and must be less than 100 characters.")
        return value

    @validates('price')
    def validate_price(self, key, value):
        if value < 0:
            raise ValueError("Price must be a non-negative float.")
        return value

    @validates('latitude')
    def validate_latitude(self, key, value):
        if value is not None and not -90 <= value <= 90:
            raise ValueError("Latitude must be between -90 and 90.")
        return value

    @validates('longitude')
    def validate_longitude(self, key, value):
        if value is not None and not -180 <= value <= 180:
            raise ValueError("Longitude must be between -180 and 180.")
        return value

    def to_dict(self):
        """Convert the place object to a dictionary."""
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'title': self.title,
            'description': self.description,
            'city': self.city,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'amenity_ids': self.amenity_ids,
            'reviews': self.reviews,
        }
