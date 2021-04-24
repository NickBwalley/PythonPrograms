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

