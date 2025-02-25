#!/usr/bin/python3
'''Place Class'''

from datetime import datetime
from .basemodel import BaseModel
from .user import User


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
<<<<<<< HEAD
        self.reviews = []
        self.amenities = []
=======
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities
>>>>>>> main
        self.restrictions()

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)
        self.save()

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
        self.save()

    def restrictions(self):
        '''Validate the place's attributes restrictions'''
        if len(self.title) > 100 or not self.title:
            raise ValueError("The maximum title length is 100 characters.")

        if not isinstance(self.price, int):
            raise TypeError("Price must be an integer.")
        if self.price <= 0:
            raise ValueError("The price must be greater than 0.")

        if not isinstance(self.latitude, float):
            raise TypeError("Latitude must be a float.")
        if self.latitude < -90 or self.latitude > 90:
<<<<<<< HEAD
            raise ValueError("Latitude must be between -90.0 and 90.0")

        if not isinstance(self.longitude, float):
            raise TypeError("Longitude must be a float.")
        if self.longitude < -180 or self.longitude > 180:
            raise ValueError("Longitude must be between -180.0 and 180.0")

=======
            raise ValueError("Latitude must be between -90 and 90.")
        if not isinstance(self.longitude, float):
            raise TypeError("Longitude must be a float.")
        if self.longitude < -180 or self.longitude > 180:
            raise ValueError("Longitude must be between -180 and 180.")
>>>>>>> main
        if not isinstance(self.owner, User):
            raise TypeError("Owner must be a User instance.")
