# 0x07. Python

This project is about Test-driven development in python

## Python Test Cases

All the test files are inside the tests folder <br>
All the test files are text files (extension: .txt) <br>
All your tests are executed using the command: <br>

    All the files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
    The first line of all files are exactly #!/usr/bin/python3
    The codes uses the pycodestyle (version 2.8.*)
    All the files are executable
    All the module have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All the classes have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All the functions (inside and outside a class) have a documentation
	(python3 -c 'print(__import__("my_module").my_function.__doc__)' 
	and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    python3 -m doctest ./tests/
All the modules have the documentation(python3 -c 'print(__import__("my_module").__doc__)')
And the functions documentation(python3 -c 'printi(__import__("my_module").my_function.__doc__)')

#### more info

A documentation is not a simple word, it's a real sentence explaining what's the purpose of th module,
class or method <br>
its adviceble to work well on test cases, so that you don’t miss any edge case
 – The Checker is checking for tests!
