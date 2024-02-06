#!/usr/bin/env python3
"""Defines the User model"""

from models.base_model import BaseModel


class User(BaseModel):
    """Defines the User model inheriting from BaseModel."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
