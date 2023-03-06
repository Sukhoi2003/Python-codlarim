import mysql.connector


class Core:

    def __init__(self) -> None:
        self.dbConnection()
        self.createTable()


    def dbConnection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                database="chatdb",
                user="root",
                password="root"
            )
        except Exception as err:
            print(err)
        else:
            print('Database connection is successful')

    def createTable(self):
        try:
            with self.connection.cursor() as cursor:
                sql = """
                    CREATE TABLE IF NOT EXISTS user (
                        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
                        username VARCHAR(32) NOT NULL UNIQUE,
                        password VARCHAR(32) NOT NULL,
                        delete_date DATETIME
                    )"""
                cursor.execute(sql)            
        except Exception as err:
            print(err)
        else:
            print('Table created successfully')

    def createUser(self, username, password):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""
                    INSERT INTO user (username, password) VALUES
                    ('{username}', '{password}')
                """
                cursor.execute(sql) 
        except Exception as err:
            print(err)
        else:
            self.connection.commit()
            print('New user created successfully')

    def getAllUsers(self):
        try:
            with self.connection.cursor() as cursor:
                query = f"""SELECT username, password FROM user;"""
                cursor.execute(query) 
                result = cursor.fetchall()
        except Exception as err:
            print(err)
        else:
            print('Data received')
        finally:
            return result
    
    def getUser(self, username):
        try:
            with self.connection.cursor() as cursor:
                query = f"""SELECT username, password 
                    FROM user WHERE username = '{username}';"""
                cursor.execute(query) 
                result = cursor.fetchone()
        except Exception as err:
            print(err)
        else:
            print('Data received')
        finally:
            return result
        
    def updateUser(self, username, password, newusername):
        try:
            with self.connection.cursor() as cursor:
                query = f"""UPDATE user SET username = "{newusername}" WHERE "{username}" = username AND "{password}" = password;"""
                cursor.execute(query) 
        except Exception as err:
            print(err)
        else:
            print('Update user successfully')
            self.connection.commit()
    
    def deleteUser(self, username, password):
        try:
            with self.connection.cursor() as cursor:
                query = f"""UPDATE user SET delete_date = NOW() WHERE "{username}" = username AND "{password}" = password;"""
                cursor.execute(query) 
        except Exception as err:
            print(err)
        else:
            print('Delete user successfully')
            self.connection.commit()

    def getActiveUsers(self):
        try:
            with self.connection.cursor() as cursor:
                query = f"""SELECT username, password FROM user WHERE delete_date IS NULL;"""
                cursor.execute(query) 
                result = cursor.fetchall()
        except Exception as err:
            print(err)
        else:
            print('Data received')
        finally:
            return result

d = Core()

# d.createUser('aziz1985', '212105585o4il')
# print(d.getAllUsers())
# d.updateUser('aziz1985', '212105585o4il', 'zormi')
d.deleteUser('zormi', '212105585o4il')