#!/usr/bin/env python3

""" Tests for the Basemodel Class"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_inititalization(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_save_method(self):
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        model = BaseModel()
        model_dict = model.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        for key in expected_keys:
            self.assertIn(key, model_dict)

    def test_str_method(self):
        model = BaseModel()
        str_rep = str(model)
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str_rep, expected_str)
    def test_id_generation(self):
        # Test that each instance has a unique ID
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_updated_at_after_save(self):
        # Test that updated_at attribute is updated after calling save()
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertGreater(model.updated_at, initial_updated_at)

    def test_attribute_assignment(self):
        # Test that attributes can be assigned to the instance
        model = BaseModel()
        model.name = "TestModel"
        model.age = 25
        self.assertEqual(model.name, "TestModel")
        self.assertEqual(model.age, 25)

    def test_from_dict_method(self):
        # Test creating an instance from dictionary representation
        data = {
            'id': '1234',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T00:00:00',
            '__class__': 'BaseModel',
            'name': 'TestModel'
        }
        model = BaseModel(**data)
        self.assertEqual(model.id, '1234')
        self.assertEqual(model.created_at, datetime(2022, 1, 1))
        self.assertEqual(model.updated_at, datetime(2022, 1, 2))
        self.assertEqual(model.name, 'TestModel')

    def test_str_representation(self):
        # Test the string representation of the instance
        model = BaseModel()
        model.name = "TestModel"
        model.age = 25
        str_rep = str(model)
        self.assertIn("[BaseModel]", str_rep)
        self.assertIn(model.id, str_rep)
        self.assertIn("name", str_rep)
        self.assertIn("TestModel", str_rep)
        self.assertIn("age", str_rep)
        self.assertIn("25", str_rep)

    def test_init_with_custom_id(self):
        # Test initialization with a custom ID
        custom_id = 'custom_id'
        model = BaseModel(id=custom_id)
        self.assertEqual(model.id, custom_id)

    def test_to_dict_with_custom_attributes(self):
        # Test to_dict method with custom attributes
        model = BaseModel()
        model.custom_attr = "CustomValue"
        model_dict = model.to_dict()
        self.assertIn('custom_attr', model_dict)
        self.assertEqual(model_dict['custom_attr'], "CustomValue")

    def test_str_representation_with_no_attributes(self):
        # Test string representation with no attributes
        model = BaseModel()
        str_rep = str(model)
        self.assertIn("[BaseModel]", str_rep)
        self.assertIn(model.id, str_rep)

    if __name__ == '__main__':
        unittest.main()
