from app.models.baseclass import BaseModel
from app import db
from sqlalchemy.orm import relationship, validates
from datetime import datetime


# Association table many-to-many
place_amenity = db.Table('place_amenity',
    db.Column('place_id', db.String(36), db.ForeignKey('places.id'), primary_key=True),
    db.Column('amenity_id', db.String(36), db.ForeignKey('amenities.id'), primary_key=True)
)

class Place(BaseModel):
    __tablename__ = 'places'


    owner_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1024), nullable=True)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    reviews = relationship('Review', backref='place', lazy=True)
    amenities = relationship('Amenity', secondary=place_amenity, backref=db.backref('places', lazy='dynamic'))

    @validates('title')
    def validate_title(self, key, value):
        if value == "" or len(value) > 50:
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
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner": self.owner.to_dict(),
            "amenities": [element.to_dict() for element in self.amenities],
            "reviews": [element.to_dict() for element in self.reviews]
        }
