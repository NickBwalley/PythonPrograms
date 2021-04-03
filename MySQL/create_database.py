"""
Create Connection
Start by creating a connection to the database.

Use the username and password from your MySQL database:
"""

import mysql.connector
my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

print(my_db)




