#/usr/bin/env python3

import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime

class TestState(unittest.TestCase):

    def test_inheritance(self):
        # Test if State inherits from BaseModel
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_attribute_defaults(self):
        # Test if default attribute values are set correctly
        state = State()
        self.assertEqual(state.state_id, "")
        self.assertEqual(state.name, "")

    def test_attribute_assignment(self):
        # Test if attributes can be assigned
        state = State()
        state.state_id = "123"
        state.name = "California"
        self.assertEqual(state.state_id, "123")
        self.assertEqual(state.name, "California")

    def test_str_representation(self):
        # Test string representation of the instance
        state = State()
        state.state_id = "123"
        state.name = "California"
        str_rep = str(state)
        self.assertIn("[State]", str_rep)
        self.assertIn(state.id, str_rep)
        self.assertIn("state_id", str_rep)
        self.assertIn("123", str_rep)
        self.assertIn("name", str_rep)
        self.assertIn("California", str_rep)

    def test_to_dict_method(self):
        # Test the to_dict method
        state = State()
        state.state_id = "123"
        state.name = "California"
        state_dict = state.to_dict()
        self.assertIn('id', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)
        self.assertIn('__class__', state_dict)
        self.assertIn('state_id', state_dict)
        self.assertIn('name', state_dict)
        self.assertEqual(state_dict['state_id'], "123")
        self.assertEqual(state_dict['name'], "California")

    def test_from_dict_method(self):
        # Test creating an instance from dictionary representation
        data = {
            'id': '1234',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T00:00:00',
            '__class__': 'State',
            'state_id': '456',
            'name': 'Texas'
        }
        state = State(**data)
        self.assertEqual(state.id, '1234')
        self.assertEqual(state.created_at, datetime(2022, 1, 1))
        self.assertEqual(state.updated_at, datetime(2022, 1, 2))
        self.assertEqual(state.state_id, '456')
        self.assertEqual(state.name, 'Texas')

if __name__ == '__main__':
    unittest.main()
