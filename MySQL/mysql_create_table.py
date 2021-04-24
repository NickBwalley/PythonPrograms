import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nickbiiy.mysql099",
    database="testdb"
)

my_cursor = my_db.cursor()

my_cursor.execute("CREATE TABLE customers(name VARCHAR(255), address VARCHAR(255))")
