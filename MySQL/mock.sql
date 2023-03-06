CREATE TABLE IF NOT EXISTS user (
    id SERIAL,
    username VARCHAR(32) UNIQUE,
    password VARCHAR(32),
    delete_date DATETIME,
    update_date DATETIME
);

INSERT INTO user (user, password) VALUES ("seniorAli", "123456789")

