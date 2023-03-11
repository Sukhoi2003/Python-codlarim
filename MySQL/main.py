import mysql.connector


class Core:

    def __init__(self) -> None:
        self.__connectDb()

    
    def connectDb(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            databasa = "chatdb ",
            user = "root",
            password = "root"
        )
        print("Ulandi")

c = Core()