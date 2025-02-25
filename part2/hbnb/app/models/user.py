#!/usr/bin/python3
'''User Class module
Defines a User class that inherits from BaseModel
including attributes for user information and restrictions'''

import re
from .basemodel import BaseModel


class User(BaseModel):
    '''Represents a user with various attributes and restrictions'''

    def __init__(self, first_name, last_name, email, is_admin=False):
        '''Initialize a new User instance with validation'''
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.restrictions()

    def restrictions(self):
        '''Validate the user's attributes for len and format restrictions'''
        if len(self.first_name) > 50 or not self.first_name:
            raise ValueError("The maximum first name length is 50 characters")
        if not isinstance(self.first_name, str):
            raise TypeError("First name must be a string of characters.")

        if len(self.last_name) > 50 or not self.last_name:
            raise ValueError("The maximum last name length is 50 characters.")
        if not isinstance(self.last_name, str):
            raise TypeError("Last name must be a string of characters.")

        if not self.email or not re.fullmatch(
            r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.email):
            raise ValueError("The email format is invalid.")

        if not isinstance(self.is_admin, bool):
            raise TypeError("Admin must be a boolean.")
