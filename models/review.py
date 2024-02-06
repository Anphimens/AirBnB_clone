#!/usr/bin/env python3
""" A class for Reviews"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ A review model inheriting from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
