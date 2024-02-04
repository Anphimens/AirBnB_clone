#!/usr/bin/env python3
# console.py
import cmd
from models.base_model import BaseModel


class dHBNBComman(cmd.Cmd):
    """This is simple command interpreter of Antoinette and Eugenious"""
    prompt = "(hbnb) "


    __models = {
        
        "BaseModel": BaseModel 

    }


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
        class_name = line.split()[0]
        if class_name not in self.__models:
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)






if __name__ == '__main__':
    dHBNBComman().cmdloop()
