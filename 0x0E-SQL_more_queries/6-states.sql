-- a script that creates a database and a table in the server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
-- now creating the table
CREATE TABLE IF NOT EXISTS states
(
	id INT AUTO_INCREMENT,
	PRIMARY KEY (id),
	name VARCHAR(256)
);
