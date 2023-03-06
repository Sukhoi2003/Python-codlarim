    CREATE DATABASE chatdb;
    DROP DATABASE chatdb;


    CREATE TABLE IF NOT EXISTS user (
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
        username VARCHAR(32) NOT NULL UNIQUE,
        password VARCHAR(32) NOT NULL,
        delete_date DATETIME
    ); 

    INSERT INTO user (username, password) VALUES
    ("aziz1234",'214365');

    SELECT *FROM user;

    SELECT username, password FROM user WHERE username = username;

    UPDATE user SET username = newusername WHERE username = username AND password = password;

    SELECT username, password FROM user WHERE delete_date IS NULL;

