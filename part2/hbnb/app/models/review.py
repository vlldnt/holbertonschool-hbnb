#!/usr/bin/python3
'''Review Class'''

import re
from .basemodel import BaseModel
from .user import User
from .place import Place


class Review(BaseModel):
    def __init__(self, text, user, place, rating):
        super().__init__()
        self.user = user
        self.place = place
        self.text = text
        self.rating = rating
        self.validate_attributes()

    def validate_attributes(self):
        '''
        Validate the review attributes for length, format,
        and type restrictions
        '''

        if not isinstance(self.user, User) or not self.user:
            raise TypeError("must be a instance of user")

        if not isinstance(self.place, Place) or not self.place:
            raise TypeError("must be a instance of place")

        if not isinstance(self.text, str) or len(self.text) > 500:
            raise ValueError(
                "Text must be a string with a maximum of 500 characters."
            )

        if not isinstance(self.rating, (int, float)) or not (
                1 <= self.rating <= 5
                ):
            raise ValueError("Rating must be a number between 1 and 5.")
