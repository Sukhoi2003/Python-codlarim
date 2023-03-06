import mysql.connector

class Core:

    def __init__(self):
        self.__connectDb()
        # self.createTable()

    def __connectDb(self):
        try:
            self.conn = mysql.connector.connect(
                host = "localhost",
                database = "storedb",
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
                                    productname VARCHAR(32) UNIQUE,
                                    price VARCHAR(32),
                                    amount VARCHAR(32)
                                );"""
                cursor.execute(sql)
        except Exception as error:
            print(error)
        else:
            print("Jadval yasaldi")

    def insertUser(self, pname, price, amount):
        try:
            with self.conn.cursor() as cursor:
                query = f"""INSERT INTO user (productname, price, amount) VALUES ("{pname}", "{price}", "{amount}")"""
                cursor.execute(query)
        except Exception as error:
            print(error)
        else:
            self.conn.commit()
            print("Malumot yoziladi")




# c = Core()
# c.insertUser()