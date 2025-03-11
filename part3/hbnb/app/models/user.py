#!/usr/bin/python3
'''User Class module
Defines a User class that inherits from BaseModel
including attributes for user information and validation'''

import re
from sqlalchemy.orm import validates
from .basemodel import BaseModel
from app import bcrypt, db

class User(BaseModel):
    '''Represents a user with various attributes and restrictions'''
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, first_name, last_name, email, password,
                 is_admin=False):
        '''Initialize a new User instance with validation'''
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.password = password

    @validates('first_name', 'last_name')
    def validate_names(self, key, value):
        """Validation for first_name and last_name"""
        if len(value) > 50 or not re.fullmatch(
            r'^[A-Za-zÀ-ÖØ-öø-ÿ -\']+$', value):
            raise ValueError(
                "{} must be present with a maximum of 50 characters"
                " and can only contain letters, spaces '-' and '".format(
                    key.replace('_', ' ').title()))

        if not isinstance(value, str):
            raise TypeError("{} must be a string of characters.".format(
                key.replace('_', ' ').title()))

    @validates('email')
    def validate_email(self, key, value):
        """Validates the email format before saving it"""
        if not isinstance(value, str):
            raise TypeError("{} must be a string.".format(
                key.replace('_', ' ').title()))

        value = value.strip()  # delete spaces before and after the email
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.fullmatch(email_regex, value):
            raise TypeError("{} must be a valid email.".format(
                key.replace('_', ' ').title()))

        return value

    @validates('is_admin')
    def validate_is_admin(self, key, value):
        """Validates if is_admin is a boolean"""
        if not isinstance(value, bool):
            raise TypeError("{} must be a boolean.".format(
                key.replace('_', ' ').title()))
        return value

    def hash_password(self, password):
        """Hashes the password before storing it"""
        self.password = bcrypt.generate_password_hash(password) \
            .decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password"""
        return bcrypt.check_password_hash(self.password, password)
