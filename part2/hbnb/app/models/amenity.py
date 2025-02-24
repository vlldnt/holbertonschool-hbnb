#!/usr/bin/python3
''' Amenity Class represents an amenity, inheriting from BaseModel'''


from .basemodel import BaseModel


class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.restrictions()

    def restrictions(self, name):
        if len(name) > 50 or not self.name:
            raise ValueError("Amenity must be a string with a maximum of 50 characters.")
