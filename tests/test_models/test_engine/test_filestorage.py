import unittest
from unittest.mock import patch, mock_open
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.engine.file_storage import FileStorage
import os

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all(self):
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        user = User()
        self.storage.new(user)
        self.assertEqual(len(self.storage.all()), 1)
        self.assertIn("User." + user.id, self.storage.all())

    @patch('json.dump')
    @patch('os.path.exists', return_value=True)
    def test_save(self, mock_exists, mock_json_dump):
        user = User()
        self.storage.new(user)
        self.storage.save()
        mock_json_dump.assert_called_once()

    @patch('builtins.open', new_callable=mock_open, read_data='{}')
    @patch('os.path.exists', return_value=True)
    def test_reload(self, mock_exists, mock_open):
        user = User()
        self.storage.new(user)
        self.storage.save()
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 1)
        self.assertIn("User." + user.id, self.storage.all())

    @patch('builtins.open', new_callable=mock_open, read_data='{"User.123": {"__class__": "User", "id": "123", "name": "John"}}')
    @patch('os.path.exists', return_value=True)
    def test_reload_with_existing_data(self, mock_exists, mock_open):
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 1)
        self.assertIn("User.123", self.storage.all())

    @patch('os.path.exists', return_value=False)
    def test_reload_file_not_found(self, mock_exists):
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

if __name__ == '__main__':
    unittest.main()
