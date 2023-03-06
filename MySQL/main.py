import mysql.connector

class Core:

    def __init__(self):
        self.__connectDb()
        self.createTable()

    def __connectDb(self):
        try:
            self.conn = mysql.connector.connect(
                host = "localhost",
                database = "chatdb",
                user = "root",
                password = "root"
            )
        except Exception as error:
            print(error)
        else:
            print("Databasaga ulandi")


    def createTable(self):
        try:
            with self.conn.cursor() as cursor:
                sql = """CREATE TABLE IF NOT EXISTS user (
                                    id SERIAL, 
                                    username VARCHAR(32) UNIQUE,
                                    password VARCHAR(32),
                                    delete_date DATETIME,
                                    update_date DATETIME
                                );"""
                cursor.execute(sql)
        except Exception as error:
            print(error)
        else:
            print("Jadval yasaldi")

    def insertUser(self):
        try:
            with self.conn.cursor() as cursor:
                query = """INSERT INTO user (username, password) VALUES ("seniorAli", "123456789")"""
                cursor.execute(query)
        except Exception as error:
            print(error)
        else:
            print("Foydalanuvchi ro'yhatdan o'tdi")




c = Core()
c.insertUser()
