-- creates the database db_medreminder and the user user_medreminder
-- create database db_medreminder
CREATE DATABASE IF NOT EXISTS db_medreminder;
-- creates user user_medreminder
CREATE USER IF NOT EXISTS 'user_medreminder'@'localhost' IDENTIFIED BY 'pwd_medreminder';
-- grants select privileges
GRANT SELECT ON db_medreminder.* TO 'user_medreminder'@'localhost';
