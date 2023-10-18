-- a script that creates a DB and a table on the server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities;
(
	id INT AUTO_INCRIMENT,
	PRIMARY KEY (id),
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE,
	name VARCHAR(256) NOT NULL
);