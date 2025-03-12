#!/usr/bin/python3
'''Place Class'''

from app.models.basemodel import BaseModel
from app.models.user import User
from app.models.amenity import Amenity
from app import db
from sqlalchemy.orm import validates


class Place(BaseModel):
    """Place class that inherits from BaseModel."""
    __tablename__ = 'places'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=True)
    price = db.Column(db.Integer, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=False)
    
    @validates('title')
    def validate_title(self, key, value):
        """Validation for title"""
        if len(value) > 100:
            raise ValueError(
                "Title must be present with a maximum of 100 characters.")
        return value

    @validates('price')
    def validate_price(self, key, value):
        if not isinstance(value, int):
            raise TypeError("Price must be an integer.")
        if value <= 0:
            raise ValueError("The price must be greater than 0.")
        return value

    @validates('latitude')
    def validate_latitude(self, key, value):
        if not isinstance(value, float):
            raise TypeError("Latitude must be a float.")
        if value < -90 or value > 90:
            raise ValueError("Latitude must be between -90.0 and 90.0")
        return value

    @validates('longitude')
    def validate_longitude(self, key, value):
        if not isinstance(value, float):
            raise TypeError("Longitude must be a float.")
        if value < -180 or value > 180:
            raise ValueError("Longitude must be between -180.0 and 180.0")
        return value

    @validates('owner_id')
    def validate_owner_id(self, key, value):
        if not isinstance(value, str):
            raise TypeError("Owner must be a User ID string.")
        return value

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)
        self.save()

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        if not isinstance(amenity, Amenity):
            raise TypeError("Amenity must be an Amenity instance.")
        self.amenities.append(amenity)
        self.save()

    def to_dict(self):
        """Convert the Place object to a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id
        }
