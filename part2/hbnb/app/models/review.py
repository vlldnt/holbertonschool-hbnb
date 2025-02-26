#!/usr/bin/python3
'''Review Class'''


from .basemodel import BaseModel
from .user import User
from .place import Place


class Review(BaseModel):
    def __init__(self, text, user_id, place_id, rating):
        super().__init__()
        self.user_id = user_id
        self.place_id = place_id
        self.text = text
        self.rating = rating
        self.validate_attributes()

    def validate_attributes(self):
        '''
        Validate the review attributes for length, format,
        and type restrictions
        '''

        if not isinstance(self.user_id, User) or not self.user_id:
            raise TypeError("must be a instance of user")

        if not isinstance(self.place_id, Place) or not self.place_id:
            raise TypeError("must be a instance of place")

        if not isinstance(self.text, str) or len(self.text) > 500:
            raise ValueError(
                "Text must be a string with a maximum of 500 characters."
            )

        if not isinstance(self.rating, (int, float)) or not (
                1 <= self.rating <= 5
                ):
            raise ValueError("Rating must be a number between 1 and 5.")
