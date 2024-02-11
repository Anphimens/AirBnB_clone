#!/usr/bin/env python3

""" Sets the state class"""

from models.base_model import BaseModel

class State(BaseModel):
    """Creates a state class that inherits from BaseModel"""
    state_id = ""
    name = ""
