# 0x09. Python - Everything is object

Background Context
--------------------

As you understand that everything is an object let’s pause and look a little bit <br>
closer at how Python works with different types of objects.
<br>
BTW, have you ever modified a variable without knowing it or wanting to? I mean:<br>

::

	>>> a = 1
	>>> b = a
	>>> a = 2
	>>> b
	1
	>>>

<br>
OK. But what about this?
<br>

	>>> l = [1, 2, 3]
	>>> m = l
	>>> l[0] = 'x'
	>>> m
	['x', 2, 3]
	>>> 

### .txt Answer Files
    Only one line
    No Shebang
    All my files end with a new line
