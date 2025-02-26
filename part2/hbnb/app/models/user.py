#!/usr/bin/python3
'''User Class module
Defines a User class that inherits from BaseModel
including attributes for user information and validation'''


import re
from .basemodel import BaseModel


class User(BaseModel):
    '''Represents a user with various attributes and restrictions'''

    def __init__(self, first_name, last_name, email, is_admin=False):
        '''Initialize a new User instance with validation'''
        super().__init__()
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._is_admin = is_admin
        self.restrictions()

    def restrictions(self):
        '''Validate the user's attributes for len and format restrictions'''
        if len(self._first_name) > 50 or not self._first_name:
            raise ValueError(
                "First name must be present with a maximum of 50 characters."
            )
        if not isinstance(self._first_name, str):
            raise TypeError("First name must be a string of characters.")

        if len(self._last_name) > 50 or not self._last_name:
            raise ValueError(
                "Last name must be present with a maximum of 50 characters."
            )
        if not isinstance(self._last_name, str):
            raise TypeError("Last name must be a string of characters")

        if not re.fullmatch(
            r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self._email
        ):
            raise ValueError("The email format is invalid.")

        if not isinstance(self._is_admin, bool):
            raise TypeError("Admin must be a boolean.")

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if len(value) > 50 or not value:
            raise ValueError(
                "First name must be present with a maximum of 50 characters."
            )
        if not isinstance(value, str):
            raise TypeError("First name must be a string of characters.")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if len(value) > 50 or not value:
            raise ValueError(
                "Last name must be present with a maximum of 50 characters."
            )
        if not isinstance(value, str):
            raise TypeError("Last name must be a string of characters.")
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not re.fullmatch(
            r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value
        ):
            raise ValueError("The email format is invalid.")
        self._email = value

    @property
    def is_admin(self):
        return self._is_admin

    @is_admin.setter
    def is_admin(self, value):
        if not isinstance(value, bool):
            raise TypeError("Admin must be a boolean.")
        self._is_admin = value
