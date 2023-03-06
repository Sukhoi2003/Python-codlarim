CREATE DATABASE ntdb;


USE ntdb;

CREATE TABLE IF NOT EXISTS course (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(64) UNIQUE
);


INSERT INTO course (name) VALUES
    ("FullStack"),
    ("Grafik dizayn"),
    ("Foundation"),
    ("Go"),
    ("Frontent"),
    ("English for IT"),
    ("QA"),
    ("Java");


CREATE TABLE IF NOT EXISTS student (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(32),
    last_name VARCHAR(32),
    date_of_birth DATE,
    course_id INT
);


INSERT INTO student (first_name, last_name, date_of_birth, course_id) VALUES
    ('Fazliddin', 'Abbosov', '2000-01-05', 1),
    ('Hamid', 'Karimov', '1997-05-21', 4),
    ('Javlon', 'Payonov', '2005-09-11', 5),
    ('Komiljon', 'Allaniyozov', '2001-08-15', 3),
    ('Hadicha', 'Ibroximova', '1998-11-27', 2),
    ('Bekzod', 'Baxromov', '2003-03-18', 1),
    ('Yulduz', 'Mirbabaeva', '2002-07-25', NULL);
