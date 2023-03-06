import mysql.connector


class Coree:

    def __init__(self) -> None:
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
            print("Databazaga ulandi")

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
        except Exception as err:
            print(err)
        else:
            print("Jadval yasaldi")

    def insertUser(self, username, password):
            try:
                with self.conn.cursor() as cursor:
                    query = f"""INSERT INTO user (username, password) VALUES ("{username}", "{password}")"""
                    cursor.execute(query)
            except Exception as err:
                print(err)
            else:
                print("""Foydalanuvchi ro'yhatdan o'tdi""")
                self.conn.commit()

        
    def getAllUsers(self):
        try:
            with self.conn.cursor() as cursor:
                query = f"""SELECT *FROM user;"""
                cursor.execute(query)
                result = cursor.fetchall()
        except Exception as err:
            print(err)
        else:
            return result
        

    def getUser(self, username):
        try:
            with self.conn.cursor() as cursor:
                query = f"""SELECT username, password FROM user WHERE "{username}" = username;"""
                cursor.execute(query)
                result = cursor.fetchone()
        except Exception as err:
            print(err)
        else:
            return result


     def deleteUser(self, username, password):
        try:
            with self.conn.cursor() as cursor:
                query = f"""UPDATE user SET delete_date = now() WHERE "{username}" = username
                  AND "{password}" = password;"""
                cursor.execute(query)
                result = cursor.fetchone()
        except Exception as err:
            print(err)
        else:
            return result



c = Coree()
# c.insertUser("Muhammadkarim", "11114144")
print(c.getAllUsers())
print(c.getUser("drAziz"))