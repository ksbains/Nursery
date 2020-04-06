import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="password",
	database="company"
)

cursor = mydb.cursor()

def read_from_database():
	sql = "SELECT * FROM department"
	cursor.execute(sql)
	myresult= cursor.fetchall()
	for x in myresult:
		print(x)

read_from_database()