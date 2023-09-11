# 0x0A. Python

This project is about Inheritance in python


## Python Scripts

All the files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5) <br>
The first line of all files are exactly #!/usr/bin/python3 <br>
The codes uses the pycodestyle (version 2.8.)


## Python Test Cases

All the module have a documentation (python3 -c 'print(__import__("my_module").__doc__)') <br>
All the classes have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)') <br>
All the functions (inside and outside a class) have a documentation
(python3 -c 'print(__import__("my_module").my_function.__doc__)' 
and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

<br>
All the tests should be executed by using this command:

	python3 -m doctest ./tests/*

Documentation
-------------

+. The words import or from are not used in comments, because the checker will think you try to import some modules
