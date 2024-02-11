#!/usr/bin/python3

import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime

class TestPlace(unittest.TestCase):

    def test_inheritance(self):
        # Test if Place inherits from BaseModel
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_attribute_defaults(self):
        # Test if default attribute values are set correctly
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [""])

    def test_attribute_assignment(self):
        # Test if attributes can be assigned
        place = Place()
        place.city_id = "123"
        place.user_id = "456"
        place.name = "Beach House"
        place.description = "Beautiful beachfront property"
        place.number_rooms = 3
        place.number_bathrooms = 2
        place.max_guest = 6
        place.price_by_night = 200
        place.latitude = 40.7128
        place.longitude = -74.0060
        place.amenity_ids = ["pool", "wifi"]
        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.user_id, "456")
        self.assertEqual(place.name, "Beach House")
        self.assertEqual(place.description, "Beautiful beachfront property")
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 6)
        self.assertEqual(place.price_by_night, 200)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, ["pool", "wifi"])

    def test_str_representation(self):
        # Test string representation of the instance
        place = Place()
        place.name = "Cabin"
        str_rep = str(place)
        self.assertIn("[Place]", str_rep)
        self.assertIn(place.id, str_rep)
        self.assertIn("name", str_rep)
        self.assertIn("Cabin", str_rep)

    def test_to_dict_method(self):
        # Test the to_dict method
        place = Place()
        place.name = "Mountain Retreat"
        place_dict = place.to_dict()
        self.assertIn('id', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)
        self.assertIn('__class__', place_dict)
        self.assertIn('name', place_dict)
        self.assertEqual(place_dict['name'], "Mountain Retreat")

    def test_from_dict_method(self):
        # Test creating an instance from dictionary representation
        data = {
            'id': '1234',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T00:00:00',
            '__class__': 'Place',
            'name': 'Lake House'
        }
        place = Place(**data)
        self.assertEqual(place.id, '1234')
        self.assertEqual(place.created_at, datetime(2022, 1, 1))
        self.assertEqual(place.updated_at, datetime(2022, 1, 2))
        self.assertEqual(place.name, 'Lake House')

if __name__ == '__main__':
    unittest.main()

