#!/usr/bin/env python3
import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime

class TestReview(unittest.TestCase):

    def test_inheritance(self):
        # Test if Review inherits from BaseModel
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_attribute_defaults(self):
        # Test if default attribute values are set correctly
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_attribute_assignment(self):
        # Test if attributes can be assigned
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "Great experience!"
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "Great experience!")

    def test_str_representation(self):
        # Test string representation of the instance
        review = Review()
        review.text = "Good service"
        str_rep = str(review)
        self.assertIn("[Review]", str_rep)
        self.assertIn(review.id, str_rep)
        self.assertIn("text", str_rep)
        self.assertIn("Good service", str_rep)

    def test_to_dict_method(self):
        # Test the to_dict method
        review = Review()
        review.text = "Nice location"
        review_dict = review.to_dict()
        self.assertIn('id', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)
        self.assertIn('__class__', review_dict)
        self.assertIn('text', review_dict)
        self.assertEqual(review_dict['text'], "Nice location")

    def test_from_dict_method(self):
        # Test creating an instance from dictionary representation
        data = {
            'id': '1234',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T00:00:00',
            '__class__': 'Review',
            'text': 'Great view'
        }
        review = Review(**data)
        self.assertEqual(review.id, '1234')
        self.assertEqual(review.created_at, datetime(2022, 1, 1))
        self.assertEqual(review.updated_at, datetime(2022, 1, 2))
        self.assertEqual(review.text, 'Great view')

if __name__ == '__main__':
    unittest.main()
