#!/usr/bin/env python3
# console.py
import cmd
from models.base_model import BaseModel


class dHBNBCommand(cmd.Cmd):
    """This is simple command interpreter of Antoinette and Eugenious"""
    prompt = "(hbnb) "


    __models = {
        
        "BaseModel": BaseModel 

    }

    def __init__(self):
        """ Initializes the methods """
        super().__init__()
        self.class_name = None


    def emptyline(self):
        """Prints a new line when the user enters the enter key"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """This function exits the cmd"""
        return True
    
    def do_create(self, line):
        """This method create a new instance of the BaseModel:
        Saves it to the JSON file and the prints the id.

        It prints message when no name found or name does not exist
        """
        if not line:
            print("** class name missing **")
            return
        self.class_name = line.split()[0]
        if self.class_name not in self.__models:
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        on the class name and id"""
        if not self.class_name:
            print("** class name missing **")
            return
        if self.class_name not in self.__models:
            print("** class doesn't exist **")
            return
        if not line:
            print("** instance id missing **")
            return
        class_name, class_id = line.split()
        



if __name__ == '__main__':
    dHBNBCommand().cmdloop()
