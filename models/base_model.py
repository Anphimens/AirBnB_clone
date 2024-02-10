#!/usr/bin/env python3
"""Base models that defines all common attributes for other classes"""

from uuid import uuid4
from datetime import datetime
class BaseModel:
    """Sets the atributes for all dependencies """
    def __init__(self, *args, **kwargs) -> None:
        """ Initialization of base model."""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)

                self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    
    
    def __str__(self) -> str:
        """Returns a string format in a customized form"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
    
    
    def save(self) -> None:
        """ Updates updated_at with the current datetime."""
        self.updated_at = datetime.now()
        
        
    def to_dict(self) -> dict:
        """Returns a dictionary containing all keys/values of __dict__

        Returns:
            dict: key, value of instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
