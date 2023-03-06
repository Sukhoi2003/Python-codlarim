CREATE DATABASE testdb;
DROP DATABASE testdb;

USE testdb; 

DROP TABLE datetest;

CREATE TABLE IF NOT EXISTS  datetest (
    id INT NOT NULL,  
    my_date DATE, 
    my_time TIME, 
    my_datatime DATETIME,
    my_datastamp TIMESTAMP
); 

INSERT INTO datetest (id, my_date, my_time, my_datatime, my_datastamp)
VALUES (1, CURRENT_DATE(), CURRENT_TIME(), NOW(), CURRENT_TIMESTAMP());

INSERT INTO datetest (id, my_date, my_time, my_datatime, my_datastamp)
VALUES (1, NOW(), NOW(), NOW(), NOW());

