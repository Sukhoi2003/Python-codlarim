CREATE TABLE IF NOT EXISTS kompyuter (
    id INT NOT NULL AUTO_INCREMENT,
    brand VARCHAR(32) NOT NULL,
    model VARCHAR(32) NOT NULL,
    cpu VARCHAR(32) NOT NULL,
    frequency FLOAT NOT NULL,
    ram INT NOT NULL,
    os VARCHAR(35),
    price INT NOT NULL,
    PRIMARY KEY (id)
);

DESCRIBE kompyuter;

INSERT INTO kompyuter (brand, model, cpu, frequency, ram, os, price)
VALUES ("Aple", "MacBook Pro", "MacOs", 2.8, 8, "Macda", 5000);

SELECT *FROM talaba;

INSERT INTO kompyuter (brand, model, cpu, frequency, ram, os, price) VALUES
("Aple", "MacBook Pro", "MacOs", 1.5, 16, "Macc", 1200),
("Aple", "MacBook Air", "MacOs", 1.2, 8, "Macc", 1000),
("HP", "", "Intel code i5", 2.5, 8, "Linux ububntu 20.04", 680),
("DELL", "Dell Latitude", "Intel core i5", 2.3, 4, "Windows 11", 650),
("Acer", "Aspire3", "Intel core i3", 1.2, 4, "Windows 7", 450),
("Acer", "Aspire5", "Intel core i5", 1.5, 8, "Windows 10", 680),
("Asus", "Asus", "AMD Ryzen 5", 3.9, 16, "Windows 10", 550),
("Samsung", "Samsung Galaxy Book2 Pro", "Intel Iris Xe Graphics", 2.5, 16, "Windows 11", 1800),
("HP", "HP Probook", "AMD Ryzen 7", 2.5, 8, "Linux ububntu 20.04", 490),
("Lenovo", "Lenovo Flex", "Intel core i7", 2.5, 8, "Windows 7", 1200),
("Acer", "Aspire 3", "Intel core i5", 1.1, 4, "Windows 11", 1300),
("Lenovo", "Lenovo IdeaPad ", "Intel core i5", 1.1, 8, "Windows 11", 1010);

INSERT INTO kompyuter (brand, model, cpu, frequency, ram, os, price) VALUES
("Lenovo", "Lenovo Yoga Slim ", "Intel core i3", 1.5, 8, "Windows 10", 600),
("Acer", "Acer Aspire 3", "Intel core i7", 2.8, 16, "Windows 5", 800),
("DELL", "Dell Latitude 333", "Intel core i3", 1.5, 16, "intel core i3", 1500),
("HP", "HP Envyo", "MacOs", 1.5, 8, "Windows 4", 300),
("MI", "RedmiBook Pro", "MIUI3", 4.4, 32, "MIUI", 3000),
("Nokia", "Yong'oq chaqar", "Bolg'a 500", 5.0, 128, "N333", 3000),
("MI", "Xiaomi", "Redmi", 3.5, 16, "MIUI", 1200);
("Nokia", "Yong'oq chaqar", "Zirx note 3", 3.5, 16, "M333", 1200);

SELECT price FROM kompyuter WHERE os LIKE "Windows%" AND ram = 8 AND brand = "Lenovo";

SELECT price FROM kompyuter WHERE os LIKE "Windows%" AND ram = 8 AND brand = "Lenovo" ORDER BY price ASC;

CREATE TABLE IF NOT EXISTS student (
    id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(32) NOT NULL,
    second_name VARCHAR(32) NOT NULL,
    age INT NOT NULL,
    gender TEXT,
    phone_number VARCHAR(13),
    PRIMARY KEY (id)
);


CREATE TABLE mevalar (
    id INT NOT NULL AUTO_INCREMENT,
    nomi VARCHAR(15) NOT NULL,
    rangi VARCHAR(10) NOT NULL,
    tami VARCHAR(10) NOT NULL,
    miqdori DECIMAL(6, 2),
    PRIMARY KEY (id)
);

INSERT INTO mevalar (nomi, rangi, tami, miqdori) VALUES
("Olma", "Qizil", "Shirin", 1000),
("Shaftoli", "Sariq", "Shirinroq", 1545),
("Mandarin", "Sariq", "Mazza", 4257),
("Limon", "Sariq", "Nordon", 7458),
("Banan", "Sariq", "Shirin", 2000),
("Ananas", "Jigarrang", "Nordonroq", 5245),
("O'rik", "Sariq", "Shirin", 1400),
("Gilos", "Qizil", "Bemaza", 1045),
("Olcha", "Qizil", "Shirin", 1044),
("Olxo'ri", "Qizil", "Achchiq", 4500);
SELECT nomi, count(nomi) from mevalar group by nomi;

CREATE TABLE ovqat (
    id INT NOT NULL AUTO_INCREMENT,
    taom_nomi VARCHAR(50) NOT NULL,
    taom_masaliqlari VARCHAR(60) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO ovqat (taom_nomi, taom_masaliqlari) VALUES
("Palov", "guruch, sabzi, go'sht piyoz"),
("Sho'rva", "piyoz, sabzi, kartoshka"),
("Manti", "un, Qovoq, piyoz, go'sht"),
("Lag'mon", "un, kartoshka, go'sht"),
("Dimlama", "piyoz, kartoshka, go'sht"),
("Mastava", "piyoz, guruch, kartoshka, go'sht"),
("Qovurma", "piyoz, kartoshka, go'sht"),
("Makaron palov", "piyoz, makaron, kartoshka, go'sht"),
("Kabob", "faqat go'sht"),
("Chuchvara", "piyoz, un, kartoshka, sabzi, go'sht");


SELECT *
FROM ovqat
WHERE taom_nomi LIKE "%a";




SELECT *
FROM ovqat
WHERE taom_masaliqlari = "guruch";



SELECT *
FROM student
WHERE taom_masaliqlari IN ('guruch');


SELECT *
FROM ovqat
WHERE taom_masaliqlari LIKE "__uch;


SELECT *
FROM ovqat
WHERE  LIKE "%guruch%";



SELECT *
FROM kompyuter
WHERE model = "HP";


INSERT INTO kompyuter (brand, model, frequency, ram, os, price, email, chiqqan_yili) VALUES
("Aple", "MacBook Pro", "MacOs", 1.5, 16, "Macc", 1200, 2010);

+----+---------+--------------------------+-----------+-----+---------------------+-------+--------------+
| id | brand   | model                    | frequency | ram | os                  | price | chiqqan_yili |
+----+---------+--------------------------+-----------+-----+---------------------+-------+--------------+
|  1 | Aple    | MacBook Pro              |       1.5 |  16 | Macc                |  1200 | NULL         |
|  2 | Aple    | MacBook Air              |       1.2 |   8 | Macc                |  1000 | NULL         |
|  3 | HP      |                          |       2.5 |   8 | Linux ububntu 20.04 |   680 | NULL         |
|  4 | DELL    | Dell Latitude            |       2.3 |   4 | Windows 11          |   650 | NULL         |
|  5 | Acer    | Aspire3                  |       1.2 |   4 | Windows 7           |   450 | NULL         |
|  6 | Acer    | Aspire5                  |       1.5 |   8 | Windows 10          |   680 | NULL         |
|  7 | Asus    | Asus                     |       3.9 |  16 | Windows 10          |   550 | NULL         |
|  8 | Samsung | Samsung Galaxy Book2 Pro |       2.5 |  16 | Windows 11          |  1800 | NULL         |
|  9 | HP      | HP Probook               |       2.5 |   8 | Linux ububntu 20.04 |   490 | NULL         |
| 10 | Lenovo  | Lenovo Flex              |       2.5 |   8 | Windows 7           |  1200 | NULL         |
| 11 | Acer    | Aspire 3                 |       1.1 |   4 | Windows 11          |  1300 | NULL         |
| 12 | Lenovo  | Lenovo IdeaPad           |       1.1 |   8 | Windows 11          |  1010 | NULL         |
| 13 | Lenovo  | Lenovo Yoga Slim         |       1.5 |   8 | Windows 10          |   600 | NULL         |
| 14 | Acer    | Acer Aspire 3            |       2.8 |  16 | Windows 5           |   800 | NULL         |
| 15 | DELL    | Dell Latitude 333        |       1.5 |  16 | intel core i3       |  1500 | NULL         |
| 16 | HP      | HP Envyo                 |       1.5 |   8 | Windows 4           |   300 | NULL         |
| 17 | MI      | RedmiBook Pro            |       4.4 |  32 | MIUI                |  3000 | NULL         |
| 18 | Nokia   | Yong'oq chaqar           |         5 | 128 | Macc                |  3000 | NULL         |
| 19 | MI      | Xiaomi                   |       3.5 |  16 | MIUI                |  1200 | NULL         |
| 20 | Nokia   | Yong'oq chaqar           |       3.5 |  16 | M333                |  1200 | NULL         |
| 21 | Nokia   | Yong'oq chaqar           |       3.5 |  16 | M333                |  1200 | NULL         |
+----+---------+--------------------------+-----------+-----+---------------------+-------+--------------+
21 rows in set (0.00 sec)



INSERT INTO kompyuter (brand, model, frequency, ram, os, price, chiqqan_yili) VALUES
("Aple", "MacBook P", 1.2, 16, "Macc", 3200, '2011');



INSERT INTO student (firs_name, last_name, date_of_birth, course_id) VALUES
    ('Fazliddin', 'Abbosov', '2000-01-05', 1),
    ('Hamid', 'Karimov', '1997-05-21', 4),
    ('Javlon', 'Payonov', '2005-09-11', 5),
    ('Komiljon', 'Allaniyozov', '2001-08-15', 3),
    ('Hadicha', 'Ibroximova', '1998-11-27', 2),
    ('Bekzod', 'Baxromov', '2003-03-18', 1),
    ('Yulduz', 'Mirbabaeva', '2002-07-25', NULL);




