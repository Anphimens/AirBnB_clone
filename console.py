#!/usr/bin/env python3
# console.py
import cmd


class OurCmd(cmd.Cmd):
    """This is simple command interpreter of Antoinette and Eugenious"""
    intro = "You are welcome to OurCmd, explore for more features"
    prompt = "(OurCmd) "

    def do_greet(self, person):
        """Greets the user"""
        if person:
            print(f"hi {person} you are welcome, how may we help you?")
        else:
            print("Hi, you are welcome. How may we help you?")
        
    def emptyline(self):
        pass

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    OurCmd().cmdloop()
