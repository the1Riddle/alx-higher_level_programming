# Python - Object-relational mapping

## <p align="center">![Python-ORM](https://github.com/the1Riddle/alx-higher_level_programming/assets/125451537/bc071ba1-4a10-4636-875a-ba556e89b5f9)</p>

Before you start…
-----------------------------------
**Please make sure your MySQL server is in 8.0** -> [How to install MySQL 8.0 in Ubuntu 20.04](https://github.com/the1Riddle/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/README.md#more-infro)

## Background Context

In this project, I will be linking two amazing worlds: Databases and Python!
- In the first part, the module MySQLdb is used to connect to a MySQL database and execute your SQL queries.
- In the second part, the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM) will be used.

**The biggest difference is**: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “`What can I do with my objects`” and not “`How this object is stored? where? when?`”. No any SQL queries is writen only Python code. Last thing, the code won’t be “`storage type`” dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:
-----------------------

	conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
	cur = conn.cursor()
	cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
	query_rows = cur.fetchall()
	for row in query_rows:
    		print(row)
	cur.close()
	conn.close()

With an ORM:
------------------------

	engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
	Base.metadata.create_all(engine)

	session = Session(engine)
	for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    		print("{}: {}".format(state.id, state.name))
	session.close()

Do you see the difference? Cool, right?<br>
The biggest difficulty with ORM is: The syntax!<br>
Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.

## More Info

How to Install and activate venv
---------------------------
To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:

	$ sudo apt-get install python3.8-venv
	$ python3 -m venv venv
	$ source venv/bin/activate

How to Install MySQLdb module version 2.0.x
---------------------------
For installing MySQLdb, you need to have MySQL installed: [How to install MySQL 8.0 in Ubuntu 20.04](https://github.com/the1Riddle/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/README.md#more-infro)

	$ sudo apt-get install python3-dev
	$ sudo apt-get install libmysqlclient-dev
	$ sudo apt-get install zlib1g-dev
	$ sudo pip3 install mysqlclient
	...
	$ python3
	>>> import MySQLdb
	>>> MySQLdb.version_info 
	(2, 0, 3, 'final', 0)

How to Install SQLAlchemy module version 1.4.x
----------------------------

	$ sudo pip3 install SQLAlchemy
	...
	$ python3
	>>> import sqlalchemy
	>>> sqlalchemy.__version__ 
	'1.4.22'

- Also, you can have this warning message:

	/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be removed in a future release.")
	cursor.execute(statement, parameters)

- **But You can ignore it.**
