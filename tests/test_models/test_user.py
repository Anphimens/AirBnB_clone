import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime

class TestUser(unittest.TestCase):

    def test_inheritance(self):
        # Test if User inherits from BaseModel
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_attribute_defaults(self):
        # Test if default attribute values are set correctly
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attribute_assignment(self):
        # Test if attributes can be assigned
        user = User()
        user.email = "john@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"
        self.assertEqual(user.email, "john@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_str_representation(self):
        # Test string representation of the instance
        user = User()
        user.first_name = "John"
        str_rep = str(user)
        self.assertIn("[User]", str_rep)
        self.assertIn(user.id, str_rep)
        self.assertIn("first_name", str_rep)
        self.assertIn("John", str_rep)

    def test_to_dict_method(self):
        # Test the to_dict method
        user = User()
        user.first_name = "John"
        user_dict = user.to_dict()
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertIn('__class__', user_dict)
        self.assertIn('first_name', user_dict)
        self.assertEqual(user_dict['first_name'], "John")

    def test_from_dict_method(self):
        # Test creating an instance from dictionary representation
        data = {
            'id': '1234',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T00:00:00',
            '__class__': 'User',
            'first_name': 'John'
        }
        user = User(**data)
        self.assertEqual(user.id, '1234')
        self.assertEqual(user.created_at, datetime(2022, 1, 1))
        self.assertEqual(user.updated_at, datetime(2022, 1, 2))
        self.assertEqual(user.first_name, 'John')

if __name__ == '__main__':
    unittest.main()

