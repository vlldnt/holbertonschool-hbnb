#!/usr/bin/python3
'''Review Class'''

from .basemodel import BaseModel


class Review(BaseModel):
    def __init__(self, id, text, user, place, rating, created_at, updated_at):
        self.id = id
        self.user = user
        self.place = place
        self.text = text
        self.rating = rating
        self.created_at = created_at
        self.updated_at = updated_at
