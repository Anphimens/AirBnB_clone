import unittest
from unittest.mock import patch, mock_open
from io import StringIO
from console import HBNBCommand
import cmd
import sys

class TestHBNBCommand(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        with patch('builtins.input', return_value="quit"):
            HBNBCommand().cmdloop()
        self.assertEqual(mock_stdout.getvalue(), "(hbnb) ")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_command(self, mock_stdout):
        with patch('builtins.input', return_value="create BaseModel"):
            HBNBCommand().cmdloop()
        self.assertIn("hbnb.storage.FileStorage", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_command(self, mock_stdout):
        with patch('builtins.input', return_value="show BaseModel"):
            HBNBCommand().cmdloop()
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_command(self, mock_stdout):
        with patch('builtins.input', return_value="destroy BaseModel"):
            HBNBCommand().cmdloop()
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_command(self, mock_stdout):
        with patch('builtins.input', return_value="all"):
            HBNBCommand().cmdloop()
        self.assertIn("[]", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_command(self, mock_stdout):
        with patch('builtins.input', return_value="update BaseModel"):
            HBNBCommand().cmdloop()
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()

