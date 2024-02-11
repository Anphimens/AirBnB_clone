#!/usr/bin/python3

""" A class to serialize and deserialize python objects to JSON and back."""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """ Serializes and Deserializes objectss"""
    __file_path = "file.json"
    __objects = {}
    __models = {
            "BaseModel": BaseModel,
            }

    def all(self) -> dict:
        """
        Return dictionary containing objects

        dict: dictionary of serialized objects
        """
        return self.__objects

    def new(self, obj) -> None:
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self) -> None:
        """Serializes __objects to the JSON file"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """ Deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                try:
                    data = json.load(f)
                    for key, value in data.items():
                        m_name = value["__class__"]
                        self.__objects[key] = self.__models[m_name](**value)
                except Exception as e:
                    print("JSON file could not be reloaded: ", e)
