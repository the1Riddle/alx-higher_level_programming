-- a script that creates a sever for a user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- grant the user acces to the root
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
