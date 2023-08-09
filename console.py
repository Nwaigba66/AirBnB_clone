import cmd
import models


class HBNBCommand(cmd.Cmd):
    """ initializing the command line """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """ to Quit the program """
        return True

    def do_EOF(self, line):
        """ End of the file """
        print()
        return True

    def emptyline(self):
        """ To handle the empty line """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
