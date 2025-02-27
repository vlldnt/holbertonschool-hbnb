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

    @property
    def text(self):
        return self.text

    @text.setter
    def text(self, string):
        if not string or len(string) > 500:
            raise ValueError(
                "Text review must be present and with 500 characters maximum."
            )
        self.text = string

    @property
    def user_id(self):
        return self.user_id

    @user_id.setter
    def user_id(self, value):
        if not value or not isinstance(value, User):
            raise ValueError("User must be present and an instance of User.")
        self.user_id = value

    @property
    def place_id(self):
        return self.place_id

    @place_id.setter
    def place_id(self, value):
        if not value or not isinstance(value, Place):
            raise ValueError("Place must be present and an instanc of Place.")
        self.place_id = value

    @property
    def rating(self):
        return self.rating

    @rating.setter
    def rating(self, value):
        if not (value > 0 and value <= 5):
            raise ValueError("Rating must be between 0 and 5.")
        if not isinstance(value, int):
            raise TypeError("Rating must be an integer.")
        self.rating = value

    def to_dict(self):
        '''Convert the Review object to a dictionary'''
        return {
            'id': self.id,
            'text': self.text,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'rating': self.rating
        }
