-- a script that creates a Db and a user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- NOW CREATING THE USER
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
-- now creating the password
IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
