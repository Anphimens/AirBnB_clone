#!/usr/bin/env python3

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime

class TestAmenity(unittest.TestCase):

    def test_inheritance(self):
        # Test if Amenity inherits from BaseModel
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_attribute_defaults(self):
        # Test if default attribute values are set correctly
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_attribute_assignment(self):
        # Test if attributes can be assigned
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_str_representation(self):
        # Test string representation of the instance
        amenity = Amenity()
        amenity.name = "Gym"
        str_rep = str(amenity)
        self.assertIn("[Amenity]", str_rep)
        self.assertIn(amenity.id, str_rep)
        self.assertIn("name", str_rep)
        self.assertIn("Gym", str_rep)

    def test_to_dict_method(self):
        # Test the to_dict method
        amenity = Amenity()
        amenity.name = "Spa"
        amenity_dict = amenity.to_dict()
        self.assertIn('id', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
        self.assertIn('__class__', amenity_dict)
        self.assertIn('name', amenity_dict)
        self.assertEqual(amenity_dict['name'], "Spa")

    def test_from_dict_method(self):
        # Test creating an instance from dictionary representation
        data = {
            'id': '1234',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T00:00:00',
            '__class__': 'Amenity',
            'name': 'Tennis Court'
        }
        amenity = Amenity(**data)
        self.assertEqual(amenity.id, '1234')
        self.assertEqual(amenity.created_at, datetime(2022, 1, 1))
        self.assertEqual(amenity.updated_at, datetime(2022, 1, 2))
        self.assertEqual(amenity.name, 'Tennis Court')

if __name__ == '__main__':
    unittest.main()

