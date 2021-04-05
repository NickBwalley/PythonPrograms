"""
Create Connection
Start by creating a connection to the database.

Use the username and password from your MySQL database:
"""
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="N!ckb!!y.mysql099")
print(mydb)




