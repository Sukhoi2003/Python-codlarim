CREATE TABLE IF NOT EXISTS user (
    id SERIAL, 
    username VARCHAR(32) UNIQUE,
    password VARCHAR(32),
    delete_date DATETIME,
    update_date DATETIME
);

INSERT INTO user (user, password) VALUES ('drAziz', '12345678');

SELECT * FROM user;

SELECT username, password FROM user WHERE username = username;

UPDATE user SET delete_date = now() WHERE username = username AND password = password;