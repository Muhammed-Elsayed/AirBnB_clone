#!/usr/bin/python3
"""defines a command interpreter 'console' for the AirBnB web app"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """represents HBNB command interpreter"""

    prompt = "(hbnb) "

    classes = {"BaseModel": BaseModel}

    def emptyline(self):
        """Called when an empty line is entered and do nothing"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """exits the cmd"""
        return True

    def do_create(self, arg):
        """create an instance of the specified class"""
        if not arg:
            print("** class name missing **")
            return
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new = HBNBCommand.classes[arg]()
        print(new.id)
        storage.save()

    def do_show(self, arg):
        """show an object"""
        args = arg.partition(" ")
        class_name = args[0]
        class_id = args[1]
        # manipulate trailling args
        if class_id and ' ' in class_id:
            class_id = class_id.partition("  ")[0]
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if not class_id:
            print("** class doesn't exist **")
            return
        key = class_name + "." + class_id
        try:
            print(storage._FileSotorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def do_destory(self, arg):
        """delete an object"""
        args = arg.partition(" ")
        class_name = args[0]
        class_id = args[1]
        # manipulate trailling args
        if class_id and ' ' in class_id:
            class_id = class_id.partition(' ')[0]
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if not class_id:
            print("** class doesn't exist **")
            return
        key = class_name + "." + class_id
        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """display the string representation
        of all instances or an instance
        """
        print_list = []
        if arg:
            class_name = arg.partition(' ')[0]
            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for key, value in storage._FileStorage__objects.items():
                if key.parttion('.')[0] == arg:
                    print_list.append(str(value))
        else:
            for key, value in storage._FileStorage__objects.items():
                print_list.append(str(value))

    #def

if __name__ == '__main__':
    HBNBCommand().cmdloop()
