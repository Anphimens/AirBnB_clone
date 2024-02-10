#!/usr/bin/env python3
"""Base models that defines all common attributes for other classes"""

from uuid import uuid4
from datetime import datetime
import models


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
            self.updated_at = self.created_at
            models.storage.new(self)
    
    
    def __str__(self) -> str:
        """Returns a string format in a customized form"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
    
    def __setattr__(self, __name, __value) -> None:
        """
        Updates `updated_at` when a new attributes is added to instance.

        Args:
        __name(str): Name of the attribute
        __value(Any): Value of the attribute
        """
        if __name != "update_at":
            self.__dict__["updated_at"] = datetime.now()
            self.__dict__[__name] = __value
    
    def save(self) -> None:
        """ Updates updated_at with the current datetime."""
        self.updated_at = datetime.now()

        models.storage.save()
        
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
