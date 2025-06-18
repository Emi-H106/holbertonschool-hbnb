from __init__ import BaseModel

class Place(BaseModel):
    def __init__(self, owner, name, description, latitude, longitude, price):
        super().__init__()
        self.owner = owner      # id of the User who created the location
        self.name = name
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.price = price
        self.amenity = []         # list of Amenities ids
        self.reviews = []             # Review object list
