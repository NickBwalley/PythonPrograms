"""
Create Connection
Start by creating a connection to the database.

Use the username and password from your MySQL database:
"""
import mysql.connector
my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nickbiiy.mysql099"
)

# print(my_db)

my_cursor = my_db.cursor()

my_cursor.execute("CREATE DATABASE testdb")







