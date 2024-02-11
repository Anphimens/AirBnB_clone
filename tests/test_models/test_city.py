import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime

class TestCity(unittest.TestCase):

    def test_inheritance(self):
        # Test if City inherits from BaseModel
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_attribute_defaults(self):
        # Test if default attribute values are set correctly
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_attribute_assignment(self):
        # Test if attributes can be assigned
        city = City()
        city.state_id = "123"
        city.name = "New York"
        self.assertEqual(city.state_id, "123")
        self.assertEqual(city.name, "New York")

    def test_str_representation(self):
        # Test string representation of the instance
        city = City()
        city.state_id = "123"
        city.name = "New York"
        str_rep = str(city)
        self.assertIn("[City]", str_rep)
        self.assertIn(city.id, str_rep)
        self.assertIn("state_id", str_rep)
        self.assertIn("123", str_rep)
        self.assertIn("name", str_rep)
        self.assertIn("New York", str_rep)

    def test_to_dict_method(self):
        # Test the to_dict method
        city = City()
        city.state_id = "123"
        city.name = "New York"
        city_dict = city.to_dict()
        self.assertIn('id', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertIn('__class__', city_dict)
        self.assertIn('state_id', city_dict)
        self.assertIn('name', city_dict)
        self.assertEqual(city_dict['state_id'], "123")
        self.assertEqual(city_dict['name'], "New York")

    def test_from_dict_method(self):
        # Test creating an instance from dictionary representation
        data = {
            'id': '1234',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T00:00:00',
            '__class__': 'City',
            'state_id': '456',
            'name': 'Los Angeles'
        }
        city = City(**data)
        self.assertEqual(city.id, '1234')
        self.assertEqual(city.created_at, datetime(2022, 1, 1))
        self.assertEqual(city.updated_at, datetime(2022, 1, 2))
        self.assertEqual(city.state_id, '456')
        self.assertEqual(city.name, 'Los Angeles')

if __name__ == '__main__':
    unittest.main()
