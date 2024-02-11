#!/usr/bin/env python3

""" Sets the state class"""

from models.base_model import Base_Model

class State(BaseModel):
    """Creates a state class that inherits from BaseModel"""
    state_id = ""
    name = ""
