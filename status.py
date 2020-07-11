import mysql.connector as mariadb
import sys

mariadb_connection = mariadb.connect(user='root', password='', database='doorlock') ## Connect to db
cursor = mariadb_connection.cursor()
query = "SELECT position FROM status ORDER BY time DESC LIMIT 1;" ## Get the latest position of the lock
cursor.execute(query)
response = cursor.fetchone()[0] ## It automatically returns a tuple, we want the 1st string

print(response) ## Forward the response

