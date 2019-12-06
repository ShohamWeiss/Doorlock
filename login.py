import mysql.connector as mariadb
import sys

trialUser = sys.argv[1] ## Get the user
trialPass = sys.argv[2] ## Get the pass

mariadb_connection = mariadb.connect(user='root', password='hhh', database='doorlock') ## Connect to db
cursor = mariadb_connection.cursor()
query = "SELECT * FROM users WHERE username =" + "'" + trialUser + "'" + "and password =" + "'" + trialPass + "';"
cursor.execute(query) ## Get all user pass that match

correctness = "wrong"
for username, password in cursor: ## If they match
	if ( trialUser == username and trialPass == password):
		correctness = "correct" ## will print correct
print (correctness) ## Send back if things match

