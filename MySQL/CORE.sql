CREATE TABLE IF NOT EXISTS user (
    id SERIAL,
    username VARCHAR(32) UNIQUE,
    password VARCHAR(32),
    delete_date DATETIME,
    update_date DATETIME
)