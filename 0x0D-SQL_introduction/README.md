# SQL - Introduction

**Welcome to SQL - Introduction project**
## ![introduction to SQL](https://github.com/the1Riddle/alx-higher_level_programming/assets/125451537/f7be1690-4b9b-4d98-95e2-992c39e0b6a4)

Brief Overview
-----------------------------

SQL || Stractured Query Language is language used to manage and manipulate relational databases which provides a standardized way of interaction with databases, allowing users to perform tasks such as:
- Querying data
- Inserting
- Updating
- Deleting records
It also defines the structure and relationships within the database. With this ability it plays a crucial role in data retrieval and management in various software applications.

Requirements -> General
------------------------------
The version of SQL used is: MySQL 8.0 (version 8.0.25)
All files end with a new line.
All SQL queries have a comment jist before (i.e. syntax above) as files start by a comment to describe the tasks.
All SQL keywords are in :upper:

More Infro
-------------------------------
**Install MySQL 8.0 on Ubuntu 20.04 LTS**

	$ sudo apt update
	$ sudo apt install mysql-server
	...
	$ mysql --version
	mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
	$

**Connect to your MySQL server:**

	$ sudo mysql
	Welcome to the MySQL monitor.  Commands end with ; or \g.
	Your MySQL connection id is 11
	Server version: 8.0.25-0ubuntu0.20.04.1 Ubuntu

	Copyright (c) 2000, 2021, Oracle and/or its affiliates.

	Oracle is a registered trademark of Oracle Corporation and/or its
	affiliates. Other names may be trademarks of their respective
	owners.

	Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

	mysql>
	mysql> quit
	Bye
	$
**Use “container-on-demand” to run MySQL**
In the container, credentials are root/root

- Ask for container Ubuntu 20.04
- Connect via SSH
- OR connect via the Web terminal
- In the container, you should start MySQL before playing with it:

here >>

	$ sudo mysql
	$ service mysql start                                                   
	 * Starting MySQL database server mysqld 
	$
	$ cat 0-list_databases.sql | mysql -uroot -p                               
	Database                                                                                   
	information_schema                                                                         
	mysql                                                                                      
	performance_schema                                                                         
	sys                      
	$
