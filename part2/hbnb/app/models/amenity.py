#!/usr/bin/python3
''' Amenity Class represents an amenity, inheriting from BaseModel'''


from .basemodel import BaseModel


class Amenity(BaseModel):
    '''représents a amenity with attributes and restrictions'''
    def __init__(self, name):
        '''Initialize a new Amenity instance with restrictions'''
        super().__init__()
        self.name = name
        self.restrictions()

    def restrictions(self):
        '''Amenity must exist and must be a string of 50 characters maximum'''
        if len(self.name) > 50 or not self.name:
            raise ValueError("Amenity must be a string with max 50 characters")
