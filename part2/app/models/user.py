#!/usr/bin/python3
'''User Class'''

import re
from basemodel import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.restrictions()

    def restrictions(self):
        if len(self.first_name) > 50 or not self.first_name:
            raise ValueError("The maximum first name length is 50 characters.")
        if len(self.last_name) > 50 or not self.last_name:
            raise ValueError("The maximum last name length is 50 characters.")
        if not re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.email):
            raise ValueError("The email format is invalid.")