#!/usr/bin/python3
'''Review Class'''

from .basemodel import BaseModel


class Review(BaseModel):
    def __init__(self, text, user, place, rating):
        super().__init__()
        self.user = user
        self.place = place
        self.text = text
        self.rating = rating
