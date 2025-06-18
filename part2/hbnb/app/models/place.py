from __init__ import BaseModel

class Place(BaseModel):
    def __init__(self, owner_id, name, description='', city='', price=0):
        super().__init__()
        self.owner_id = owner_id      # id of the User who created the location
        self.name = name
        self.description = description
        self.city = city
        self.price = price
        self.amenity_ids = []         # list of Amenities ids
        self.reviews = []             # Review object list
