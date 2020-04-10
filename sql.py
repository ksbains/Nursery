import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="password",
	database="nursery"
)

cursor = mydb.cursor()



#-----------------------------------------------INSERT into TABLES------------------------------------------------------------
def insert_plant(name, price, description, age):
	sql = "INSERT INTO plant(name, price, description, age) VALUES(%s,%s,%s,%s)"
	cursor.execute(sql, (name, price, description, age))
	mydb.commit()

def insert_plant_type(name, description):
	sql = "INSERT INTO plant(name, description) VALUES(%s,%s)"
	cursor.execute(sql, (name, description))
	mydb.commit()

def insert_store(number_of_lots, phone_no, address):
	sql = "INSERT INTO store(number_of_lots, phone_no, address) VALUES(%s,%s,%s)"
	data = (number_of_lots, phone_no, address)
	cursor.execute(sql, data)
	mydb.commit()

def insert_customer(cust_name, phone_no, address, email_id):
	sql = "INSERT INTO customer(cust_name, phone_no, address, email_id) VALUES()"
	data = (cust_name, phone_no, address, email_id)
	cursor.execute(sql, data)
	mydb.commit()

def insert_orders(store_id, cust_id, order_type, payment_status, price, delivery_address):
	sql "INSERT INTO orders(store_id, cust_id, order_type, payment_status, price, delivery_address) VALUES(%s,%s,%s,%s,%s,%s)"
	data = (store_id, cust_id, order_type, payment_status, price, delivery_address)
	cursor.execute(sql, data)
	mydb.commit()

def insert_order_item(item_id, price, rating, plant_id):
	sql "INSERT INTO order_item(item_id, price, rating, plant_id) VALUES(%s,%s,%s,%s)"
	data = (item_id, price, rating, plant_id)
	cursor.execute(sql, data)
	mydb.commit()

def insert_employee(emp_name, store_id, doj, phone_no, designation, supervisor_id):
	sql "INSERT INTO employee(emp_name, store_id, doj, phone_no, designation, supervisor_id) VALUES(%s,%s,%s,%s,%s,%s)"
	data = (emp_name, store_id, doj, phone_no, designation, supervisor_id)
	cursor.execute(sql, data)
	mydb.commit()

#---------------------------------------------------------UPDATE Tables---------------------------------------------------------------------------
def update_plant(id, name, price, description, age):
	sql = "UPDATE plant SET name = %s, price = %s, description = %s, age = %s WHERE id = %s"
	cursor.execute(sql, (name, price, description, age, id))
	mydb.commit()

def update_plant_type (type_id,type_name, description):
	sql = "UPDATE plant_type SET type_name = %s, description = %s WHERE type_id = %s"
	data = (type_name, description,type_id)
	cursor.execute(sql, data)
	mydb.commit()

def update_store(store_id, number_of_lots, phone_no, address):
	sql = "UPDATE SET number_of_lots = %s, phone_no = %s, address = %s WHERE store_id = %s "
	data = (number_of_lots, phone_no, address, store_id)
	cursor.execute(sql, data)
	mydb.commit()

def update_customer(cust_id, cust_name, phone_no, address, email_id):
	sql = "UPDATE SET cust_name = %s, phone_no = %s, address = %s, email_id = %s WHERE cust_id = %s"
	data = (cust_name, phone_no, address, email_id, cust_id)
	cursor.execute(sql, data)
	mydb.commit()

def update_orders(order_id, store_id, cust_id, order_type, payment_status, price, delivery_address):
	sql = "UPDATE SET store_id = %s, cust_id = %s, order_type = %s, payment_status = %s, price = %s, delivery_address = %s WHERE order_id = %s"
	data = (store_id, cust_id, order_type, payment_status, price, delivery_address, order_id)
	cursor.execute(sql, data)
	mydb.commit()

def update_order_item(item_id, order_id,  plant_id, price, rating,):
	sql = "UPDATE SET order_id = %s, plant_id = %s, price = %s, rating = %s WHERE item_id = %s "
	data = (order_id, plant_id,price, rating,  item_id)
	cursor.execute(sql, data)
	mydb.commit()

def update_employee(emp_id, emp_name, store_id, doj, phone_no, designation, supervisor_id):
	sql = "UPDATE SET emp_name = %s, store_id = %s, doj = %s, phone_no = %s, designation = %s, supervisor_id = %s WHERE emp_id = %s"
	data = (emp_name, store_id, doj, phone_no, designation, supervisor_id, emp_id)
	cursor.execute(sql, data)
	mydb.commit()

#-------------------------------------------------------------------------------------DELETE from Tables-----------------------------------------------
def delete_plant(id):
	sql = "DELETE FROM plant WHERE id = %s"
	cursor.execute(sql, (id,))
	mydb.commit()

def delete_plant_type(type_id):
	sql = "DELETE FROM plant_type WHERE type_id = %s"
	cursor.execute(sql, (type_id,))
	mydb.commit()

def delete_store(store_id):
	sql = "DELETE FROM store WHERE store_id = %s"
	cursor.execute(sql, (store_id,))
	mydb.commit()

def delete_customer(cust_id):
	sql = "DELETE FROM customer WHERE cust_id = %s"
	cursor.execute(sql, (cust_id,))
	mydb.commit()

def delete_orders(order_id):
	sql = "DELETE FROM orders WHERE order_id = %s"
	cursor.execute(sql, (order_id,))
	mydb.commit()

def delete_order_item(item_id):
	sql = "DELETE FROM order_item WHERE item_id = %s"
	cursor.execute(sql, (item_id,))
	mydb.commit()

def delete_employee(emp_id):
	sql = "DELETE FROM employee WHERE emp_id = %s"
	cursor.execute(sql, (emp_id,))
	mydb.commit()

#---------------------------------------SELECT from Tables---------------------------------------------------
def getPlantName(id):
	sql = "SELECT name FROM palnt WHERE id = %s"
	try:
		cursor.execute(sql, (id,))
		result = cursor.fetchone()[0]
		return result
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))































#---------------------------------------------------------------------------------Database Operations--------------------------------------------------------
def plants():
	sql = "SELECT * FROM plant"
	try:
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			print(row)
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))



#---------------------------------------------------------------------------------TEST SCRIPTS--------------------------------------------------------
def main():
	plantName = "queenPalm"
	plantPrice = 25.50
	plantDescription = "YAASSS QUEEEN!!"
	plantAge = 21

	insert_plant(plantName, plantPrice, plantDescription, plantAge);
	print("-----------------PLANT TABLE-----------------")
	plants()
	update_plant(1, "KingPalm", 4.20, "ye 4/20", 69)
	print("-----------------PLANT TABLE-----------------")
	plants()
	delete_plant(1)
	print("-----------------PLANT TABLE-----------------")
	plants()

#main()
