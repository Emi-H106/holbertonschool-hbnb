from app.models.__init__ import BaseModel

class Place(BaseModel):
    def __init__(self, owner_id, title, description='', city='', price=0, latitude=None, longitude=None, amenities=None):
        super().__init__()
        self.owner_id = owner_id      # id of the User who created the location
        self.title = title
        self.description = description
        self.city = city
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_ids =  amenities if amenities is not None else []      # list of Amenities ids
        self.reviews = []             # Review object list

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty.")
        self._title = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be a non-negative float.")
        self._price = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if value is not None and not -90 <= value <=90:
            raise ValueError("Latitude must be between -90 and 90.")
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if value is not None and not -180 <= value <= 180:
            raise ValueError("Longitude must be between -180 and 180.")
        self._longitude = value

    def to_dict(self):
        """Convert the place object to a dictionary."""
        return{
            'id': str(self.id),  # Ensure id is a string
            'owner_id': str(self.owner_id),  # Ensure owner_id is a string
            'title': self.title,
            'description': self.description,
            'city': self.city,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'amenity_ids': [str(aid) for aid in self.amenity_ids],
            'reviews': [r.to_dict() for r in self.reviews],
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
