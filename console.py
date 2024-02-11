#!/usr/bin/env python3

""" console.py"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """This is simple command interpreter of Antoinette and Eugenious"""
    prompt = "(hbnb) "
    __models = {
        "BaseModel": BaseModel
        "User": User
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
        if not line:
            print("** class name missing **")
            return

        argslist = line.split()

        class_name = argslist[0]

        if class_name not in self.__models:
            print("** class doesn't exist **")
            return
        if len(argslist) < 2:
            print("** instance id missing **")
            return
        id_name = argslist[1]
        objects = storage.all()
        key = f"{class_name}.{id_name}"
        if key in objects:
            print(objects[key])

        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.
        Changes is saved in JSON file
        """
        if not line:
            print("** class name missing **")
            return
        argslist = line.split()
        class_name = argslist[0]
        if class_name not in self.__models:
            print("** class doesn't exist **")
            return
        if len(argslist) < 2:
            print("** instance id missing **")
            return
        id_name = argslist[1]
        objects = storage.all()
        key = f"{class_name}.{id_name}"
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        if line:
            class_name = line.split()[0]
            if class_name not in self.__models:
                print("** class doesn't exist **")
                return
            else:
                pass
        objects = storage.all()
        all_instances = []
        for obj in objects.values():
            all_instances.append(str(obj))

        print(all_instances)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        By adding or updating the attribute and saving
        """
        if not line:
            print("** class name missing **")
            return

        argslist = line.split()
        class_name = argslist[0]

        if class_name not in self.__models:
            print("** class doesn't exist **")
            return
        if len(argslist) < 2:
            print("** instance id missing **")
            return
        id_name = argslist[1]
        if len(argslist) < 3:
            print("** attribute name missing **")
            return
        if len(argslist) < 4:
            print("** value missing **")
            return

        key = f"{class_name}.{id_name}"
        objects = storage.all()

        if key in objects:
            obj = objects[key]
        else:
            print("** no instance found**")
            return

        attr_name = argslist[2]
        attr_value = argslist[3]
        try:
            attr_value = eval(attr_value)
        except Exception as e:
            pass

        setattr(obj, attr_name, attr_value)
        obj.save()

#if __name__ == "__main__":
#    if not sys.stdin.isatty():
#        for line in sys.stdin:
#            HBNBCommand().onecmd(line.strip())

if __name__ == '__main__':
    HBNBCommand().cmdloop()
