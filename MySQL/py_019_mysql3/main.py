import mysql.connector


class Core:
    
    def __init__(self) -> None:
        self.__connectDb()
        self.createTable()



    def __connectDb(self):
        try:
            self.conn = mysql.connector.connect(
                host = 'localhost',
                database = 'chatdb',
                user = 'root',
                password = 'root'
            )
        except Exception as error:
            print(error)
        else:
            print('Databazaga ulandi')

    def createTable(self):
        try:
            with self.conn.cursor() as cursor:
                sql = '''CREATE TABLE IF NOT EXISTS user (
                            id SERIAL, 
                            username VARCHAR(32) UNIQUE,
                            password VARCHAR(32),
                            delete_date DATETIME,
                            update_date DATETIME
                        );'''
                cursor.execute(sql)
        
        except Exception as err:
            print(err)

        else:
            print('Jadval yasaldi')

    def insertUser(self, username, password):
        try:
            with self.conn.cursor() as cursor:
                query = f'''INSERT INTO user (username, password) VALUES ("{username}", "{password}")'''
                cursor.execute(query)
        except Exception as err:
            print(err)
        else:
            print('''Foydalanuchi ro'yxatdan o'tdi.''')
            self.conn.commit()

    def getAllUsers(self):
        try:
            with self.conn.cursor() as cursor:
                query = f'''SELECT * FROM user'''
                cursor.execute(query)
                result = cursor.fetchall()
        except Exception as err:
            print(err)
        else:
            return result
        
    def getUser(self, username):
        try:
            with self.conn.cursor() as cursor:
                query = f'''SELECT username, password FROM user WHERE '{username}' = username;'''
                cursor.execute(query)
                result = cursor.fetchone()
        except Exception as err:
            print(err)
        else:
            print(result)
            return result
    
    def deleteUser(self, username, password):
        try:
            with self.conn.cursor() as cursor:
                query = f'''UPDATE user SET delete_date = now() WHERE '{username}' = username AND "{password}" = password;'''
                cursor.execute(query)

        except Exception as err:
            return err
        else:
            self.conn.commit()
            return 'Ok'
            
    def getActiveUsers(self):
        try:
            with self.conn.cursor() as cursor:
                query = f'''SELECT * FROM user WHERE delete_date IS NULL'''
                cursor.execute(query)
                result = cursor.fetchall()
        except Exception as err:
            print(err)
        else:
            return result
        
    def getDeletedUsers(self):
        try:
            with self.conn.cursor() as cursor:
                query = f'''SELECT * FROM user WHERE delete_date IS NOT NULL'''
                cursor.execute(query)
                result = cursor.fetchall()
        except Exception as err:
            print(err)
        else:
            return result
        
    def getUpdateUsername(self, username, password, newusername):
        data = self.getUser(username)
        print(data)
        if data == None:
            return 'Error'
        if data[0] == username and data[1] == password:
            try:
                with self.conn.cursor() as cursor:
                    query = f'''UPDATE user SET update_date = now(), username = '{newusername}' WHERE '{username}' = username AND "{password}" = password;'''
                    print(cursor.execute(query))
            except Exception as err:
                print(err)
            else:
                self.conn.commit()
                return 'Ok'




c = Core()
# c.insertUser('bekBen', '9555')
# print(c.getAllUsers())
# print(c.deleteUser('aziz1985', '1111111'))
# print(c.getActiveUsers())
# print(c.getDeletedUsers())
print(c.getUpdateUsername('bek1', '9555', 'bek12'))
