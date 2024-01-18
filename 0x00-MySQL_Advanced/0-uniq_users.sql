-- SQL script that creates a table `users` following these requirements:
-- `id` - integer, never null, auto increment and primary key
-- `email` -  string (255 characters), never null and unique
-- `name` - string (255 characters)

CREATE TABLE IF NOT EXISTS users (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
email varchar(255) UNIQUE NOT NULL,
name varchar(255)
);
