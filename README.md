#AirBnB clone - The console Project

##![AirBnB Logo](https://www.pngitem.com/pimgs/m/132-1322125_transparent-background-airbnb-logo-hd-png-download.png)

##Description of the project:
The goal of the project is to deploy on your server a simple copy of the AirBnB website. I won’t build this application all at once, but step by step.

##The console
- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)
- The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.
- nThis abstraction will also allow you to change the type of storage easily without updating all of your codebase.
- The console will be a tool to validate this storage engine.

##Description of the command interpreter:
The command interpreter typically provides a command prompt, which is a specific character or symbol that indicates that the interpreter is ready to receive a command. Once the prompt appears, the user can enter commands, which are textual instructions specifying tasks or operations to be performed by the computer.

##Some of the commands available are:
- show
- create
- update
- destroy
- count

##The folowing actions can be performed:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Updating attributes of an object
- Destroy an object

##How to start it:
###Execution
- Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
-  Also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

##Examples include:
Here are some examples of command interpreters or shells:

1. Bash (Bourne Again SHell): It is the default command interpreter on most Unix-like systems, including Linux and macOS. It is a powerful and widely used shell that provides a rich set of features and scripting capabilities.

2. PowerShell: Developed by Microsoft, PowerShell is a command-line shell and scripting language primarily used in Windows operating systems. It provides an extensive set of commands and features for system administration and automation.

3. Command Prompt (CMD): This is the default command interpreter in Windows operating systems. It provides a basic set of commands for file and system management. While CMD is relatively simple compared to other shells, it can still be useful for executing basic commands and scripts.

4. Zsh (Z Shell): Zsh is an extended version of the Bourne shell (sh) with additional features and customization options. It is popular among advanced users and provides powerful command-line editing capabilities and extensive configuration options.

5. Csh (C Shell): Csh is another Unix shell that provides a C-like syntax. It offers features such as command-line editing, command history, and job control. While it is not as widely used as Bash, it is still available on many Unix-like systems.

6. Fish (Friendly Interactive SHell): Fish is a modern, user-friendly command shell with features like auto-completion, syntax highlighting, and a consistent syntax. It aims to provide a more intuitive and interactive command-line experience.

These are just a few examples of command interpreters, and there are many others available, each with its own set of features and capabilities. The choice of which interpreter to use depends on the operating system and personal preferences or specific requirements of the user.

##Files that allow the program to work:
 In here there will be several files that allow the program to work.

/console.py : The main executable of the project, the command interpreter.

models/engine/file_storage.py: Class that serializes instances to a JSON file and deserializes JSON file to instances

models/__ init __.py: A unique FileStorage instance for the application

models/base_model.py: Class that defines all common attributes/methods for other classes.

models/user.py: User class that inherits from BaseModel

models/state.py: State class that inherits from BaseModel

models/city.py: City class that inherits from BaseModel

models/amenity.py: Amenity class that inherits from BaseModel

models/place.py: Place class that inherits from BaseModel

models/review.py: Review class that inherits from BaseModel 


##AUTHORS:
Gloria Nwaigba <glorianwaigba@gmail.com>
Kate Onyebuchi <iamkatty3@gmail.com>
