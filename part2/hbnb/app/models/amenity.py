#!/usr/bin/python3
''' Amenity Class represents an amenity, inheriting from BaseModel'''


from .basemodel import BaseModel


class Amenity(BaseModel):
    '''Represents an amenity with attributes and restrictions'''
    def __init__(self, name):
        '''Initialize a new Amenity instance with restrictions'''
        super().__init__()
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 50 or not value:
            raise ValueError(
                "Amenity name must be a string with max 50 characters"
                )
        if not isinstance(value, str):
            raise TypeError("Amenity name must be a string of characters.")
        self._name = value

    def to_dict(self):
        """Convert the Amenity object to a dictionary."""
        return {
            "id": self.id,
            "name": self.name
        }
