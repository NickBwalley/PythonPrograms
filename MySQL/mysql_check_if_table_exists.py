import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nickbiiy.mysql099",
    database="testdb"
)

my_cursor = my_db.cursor()

# check how many tables exists and print them out
my_cursor.execute("SHOW TABLES")

for x in my_cursor:
    print(x)

"""
Primary Key
When creating a table, you should also create a column with a unique key for each record.

This can be done by defining a PRIMARY KEY.

We use the statement "INT AUTO_INCREMENT PRIMARY KEY" which will insert a unique number for each 
record. Starting at 1, and increased by one for each record.
"""

my_cursor.execute(
    "create TABLE customers2 (id INT AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(255), "
    "lastname VARCHAR(255))"
)

