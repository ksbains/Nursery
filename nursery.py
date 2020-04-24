
import mysql.connector
import hashlib
import binascii
import os

def getConnection():	
	conn = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="password",
		database="nursery"
	)
	return conn
	
#-----------------------------------------------INSERT into TABLES------------------------------------------------------------
def insert_plant(name, price, description, age):
	conn = getConnection()
	cursor = conn.cursor()
	sql = "INSERT INTO plant(name, price, description, age) VALUES(%s,%s,%s,%s)"
	cursor.execute(sql, (name, price, description, age))
	conn.commit()
	cursor.close()
	conn.close()

def insert_plant_type(name, description):
	conn = getConnection()
	cursor = conn.cursor()
	sql = "INSERT INTO plant_type(type_name, description) VALUES(%s,%s)"
	cursor.execute(sql, (name, description))
	conn.commit()
	cursor.close()
	conn.close()

def insert_store(number_of_lots, phone_no, address):
	conn = getConnection()
	cursor = conn.cursor()
	sql = "INSERT INTO store(number_of_lots, phone_no, address) VALUES(%s,%s,%s)"
	data = (number_of_lots, phone_no, address)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()

def insert_lot(store_id):
	conn = getConnection()
	cursor = conn.cursor()
	sql = "INSERT INTO lot(store_id) VALUES(%s)"
	cursor.execute(sql, (store_id,))
	conn.commit()
	cursor.close()
	conn.close()

def insert_customer(cust_name, cust_username, cust_password, phone_no, address, email_id):
	conn = getConnection()
	cursor = conn.cursor()
	hashed_password = hash_password(cust_password)
	sql = "INSERT INTO customer(cust_name,cust_username, cust_password, phone_no, address, email_id) VALUES(%s,%s,%s, %s,%s,%s)"
	data = (cust_name, cust_username, hashed_password, phone_no, address, email_id)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()

def insert_orders(store_id, cust_id, order_type, payment_status, price, delivery_address):
	conn = getConnection()
	cursor = conn.cursor()
	sql = "INSERT INTO orders(store_id, cust_id, order_type, payment_status, price, delivery_address) VALUES(%s, %s, %s, %s, %s, %s)"
	data = (store_id, cust_id, order_type, payment_status, price, delivery_address)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()

def insert_order_item(order_id, plant_id, price, rating):
	conn = getConnection()
	cursor = conn.cursor()
	sql = "INSERT INTO order_item(order_id, plant_id,  price, rating) VALUES(%s,%s,%s,%s)"
	data = (order_id, plant_id,  price, rating)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()

def insert_employee(emp_name, emp_username, emp_password, store_id, doj, phone_no, designation, supervisor_id):
	conn = getConnection()
	cursor = conn.cursor()
	hashed_password = hash_password(emp_password)
	sql = "INSERT INTO employee(emp_name, emp_username, emp_password, store_id, doj, phone_no, designation, supervisor_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
	data = (emp_name, emp_username, hashed_password, store_id, doj, phone_no, designation, supervisor_id)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()

def insert_manager(emp_name, emp_username, emp_password, store_id, doj, phone_no):
	conn = getConnection()
	cursor = conn.cursor()
	hashed_password = hash_password(emp_password)
	designation = "Manager"
	sql = "INSERT INTO employee(emp_name, emp_username, emp_password, store_id, doj, phone_no, designation) VALUES(%s,%s,%s,%s,%s,%s,%s)"
	data = (emp_name, emp_username, hashed_password, store_id, doj, phone_no, designation)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()

#---------------------------------------------------------UPDATE Tables---------------------------------------------------------------------------
def update_plant(id, name, price, description, age):
	conn = getConnection()
	cursor = conn.cursor()
	sql = "UPDATE plant SET name = %s, price = %s, description = %s, age = %s WHERE plant_id = %s"
	cursor.execute(sql, (name, price, description, age, id))
	conn.commit()
	cursor.close()
	conn.close()

def update_plant_type (type_id,type_name, description):
	conn = getConnection()
	cursor = conn.cursor()
	sql = "UPDATE plant_type SET type_name = %s, description = %s WHERE type_id = %s"
	data = (type_name, description,type_id)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()

def update_lot(lot_id, store_id):
	conn = getConnection()
	cursor = conn.cursor()
	sql = "UPDATE lot SET store_id = %s WHERE lot_id = %s"
	data = (store_id, lot_id)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()

def update_store(store_id, number_of_lots, phone_no, address):
	conn = getConnection()
	cursor = conn.cursor()
	sql = "UPDATE store SET number_of_lots = %s, phone_no = %s, address = %s WHERE store_id = %s"
	data = (number_of_lots, phone_no, address, store_id)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()

def update_customer(cust_id, cust_name, cust_username, cust_password, phone_no, address, email_id):
	conn = getConnection()
	cursor = conn.cursor()
	hashed_password = hash_password(cust_password)
	sql = "UPDATE customer SET cust_name = %s, cust_username = %s, cust_password = %s, phone_no = %s, address = %s, email_id = %s WHERE cust_id = %s"
	data = (cust_name, cust_username, hashed_password, phone_no, address, email_id, cust_id)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()

def update_orders(order_id, store_id, cust_id, order_type, payment_status, price, delivery_address):
	conn = getConnection()
	cursor = conn.cursor()
	sql = "UPDATE orders SET store_id = %s, cust_id = %s, order_type = %s, payment_status = %s, price = %s, delivery_address = %s WHERE order_id = %s"
	data = (store_id, cust_id, order_type, payment_status, price, delivery_address, order_id)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()

def update_order_item(item_id, order_id,  plant_id, price, rating,):
	conn = getConnection()
	cursor = conn.cursor()
	sql = "UPDATE order_item SET order_id = %s, plant_id = %s, price = %s, rating = %s WHERE item_id = %s "
	data = (order_id, plant_id,price, rating,  item_id)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()

def update_employee(emp_id, emp_name, emp_username, emp_password, store_id, doj, phone_no, designation, supervisor_id):
	conn = getConnection()
	cursor = conn.cursor()
	hashed_password = hash_password(emp_password)
	sql = "UPDATE employee SET emp_name = %s, emp_username = %s, emp_password = %s, store_id = %s, doj = %s, phone_no = %s, designation = %s, supervisor_id = %s WHERE emp_id = %s"
	data = (emp_name, emp_username, hashed_password, store_id, doj, phone_no, designation, supervisor_id, emp_id)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()

#-------------------------------------------------------------------------------------DELETE from Tables-----------------------------------------------
def delete_plant(id):
	conn = getConnection()
	cursor = conn.cursor()
	sql = "DELETE FROM plant WHERE plant_id = %s"
	cursor.execute(sql, (id,))
	conn.commit()
	cursor.close()
	conn.close()

def delete_plant_type(type_id):
	conn = getConnection()
	cursor = conn.cursor()
	sql = "DELETE FROM plant_type WHERE type_id = %s"
	cursor.execute(sql, (type_id,))
	conn.commit()
	cursor.close()
	conn.close()

def delete_lot(lot_id):
	conn = getConnection()
	cursor = conn.cursor()
	sql = "DELETE FROM lot WHERE lot_id = %s"
	cursor.execute(sql, (lot_id,))
	conn.commit()
	cursor.close()
	conn.close()


def delete_store(store_id):
	conn = getConnection()
	cursor = conn.cursor()
	sql = "DELETE FROM store WHERE store_id = %s"
	cursor.execute(sql, (store_id,))
	conn.commit()
	cursor.close()
	conn.close()

def delete_customer(cust_id):
	conn = getConnection()
	cursor = conn.cursor()
	sql = "DELETE FROM customer WHERE cust_id = %s"
	cursor.execute(sql, (cust_id,))
	conn.commit()
	cursor.close()
	conn.close()

def delete_orders(order_id):
	conn = getConnection()
	cursor = conn.cursor()
	sql = "DELETE FROM orders WHERE order_id = %s"
	cursor.execute(sql, (order_id,))
	conn.commit()
	cursor.close()
	conn.close()

def delete_order_item(item_id):
	conn = getConnection()
	cursor = conn.cursor()
	sql = "DELETE FROM order_item WHERE item_id = %s"
	cursor.execute(sql, (item_id,))
	conn.commit()
	cursor.close()
	conn.close()

def delete_employee(emp_id):
	conn = getConnection()
	cursor = conn.cursor()
	sql = "DELETE FROM employee WHERE emp_id = %s"
	cursor.execute(sql, (emp_id,))
	conn.commit()
	cursor.close()
	conn.close()

#---------------------------------------SELECT from Tables---------------------------------------------------
def getPlant(id, field):
	sql = "SELECT * FROM plant WHERE plant_id = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (id,))
		result = cursor.fetchone()
		switch={
		"name": result[1],
		"price": result[2],
		"description": result[3],
		"age": result[4]
		}
		cursor.close()
		conn.close()
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def getPlantName(name, field):
	sql = "SELECT * FROM plant WHERE name = %s"
	try:
		cursor.execute(sql, (name,))
		result = cursor.fetchone()
		switch={
		"plant_id": result[0],
		"price": result[2],
		"description": result[3],
		"age": result[4]
		}
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def getPlantType(type_id, field):
	sql = "SELECT * FROM plant_type WHERE type_id = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (type_id,))
		result = cursor.fetchone()
		switch={
		"type_name": result[1],
		"description": result[2]
		}
		cursor.close()
		conn.close()
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def getLot(lot_id, field):
	sql = "SELECT * FROM lot WHERE lot_id = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (lot_id,))
		result = cursor.fetchone()
		switch={
		"store_id": result[1],
		}
		cursor.close()
		conn.close()
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def getStore(store_id, field):
	sql = "SELECT * FROM store WHERE store_id = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (store_id,))
		result = cursor.fetchone()
		switch={
		"number_of_lots": result[1],
		"phone_no": result[2],
		"address": result[3]
		}
		cursor.close()
		conn.close()
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def getCustomer(cust_id, field):
	sql = "SELECT * FROM customer WHERE cust_id = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (cust_id,))
		result = cursor.fetchone()
		switch={
		"cust_name": result[1],
		"cust_username": result[2],
		"cust_password": result[3],
		"phone_no": result[4],
		"address": result[5],
		"email_id": result[6]
		}
		cursor.close()
		conn.close()
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def getCustomerLogin(username, field):
	sql = "SELECT * FROM customer WHERE username = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (username,))
		result = cursor.fetchone()
		switch={
		"cust_name": result[1],
		"cust_username": result[2],
		"cust_password": result[3],
		"phone_no": result[4],
		"address": result[5],
		"email_id": result[6]
		}
		cursor.close()
		conn.close()
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def getOrders(order_id, field):
	sql = "SELECT * FROM orders WHERE order_id = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (order_id,))
		result = cursor.fetchone()
		switch={
		"store_id": result[1],
		"cust_id": result[2],
		"order_type": result[3],
		"payment_status": result[4],
		"price": result[5],
		"delivery_address": result[6]
		}
		cursor.close()
		conn.close()
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def getOrderItem(item_id, field):
	sql = "SELECT * FROM order_item WHERE item_id = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (item_id,))
		result = cursor.fetchone()
		switch={
		"order_id": result[1],
		"plant_id": result[2],
		"price": result[3],
		"rating": result[4]
		}
		cursor.close()
		conn.close()
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def getEmployee(emp_id, field):
	sql = "SELECT * FROM employee WHERE emp_id = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (emp_id,))
		result = cursor.fetchone()
		switch={
		"emp_name": result[1],
		"emp_username": result[2],
		"emp_password": result[3],
		"store_id": result[4],
		"doj": result[5],
		"phone_no": result[6],
		"designation": result[7],
		"supervisor_id": result[8]
		}
		cursor.close()
		conn.close()
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

# Jasper's changes
def getEmployees(storeID):
	sql = "SELECT * FROM employee WHERE store_id = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (storeID,))
		result = cursor.fetchall()
		cursor.close()
		conn.close()
		return result
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))


# Jasper's changes
def update_supID(emp_id, supervisor_id):
	sql = "UPDATE employee SET supervisor_id = %s, designation = %s WHERE emp_id = %s"
	data = (supervisor_id,"Manager",emp_id)
	conn = getConnection()
	cursor = conn.cursor()
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()

def getEmployeeLogin(username, field):
	sql = "SELECT * FROM employee WHERE emp_username = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (username,))
		result = cursor.fetchone()
		switch={
		"emp_name": result[1],
		"emp_username": result[2],
		"emp_password": result[3],
		"store_id": result[4],
		"doj": result[5],
		"phone_no": result[6],
		"designation": result[7],
		"supervisor_id": result[8]
		}
		cursor.close()
		conn.close()
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))


def getEmployeeLogin(username, field):
	sql = "SELECT * FROM employee WHERE emp_username = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (username,))
		result = cursor.fetchone()
		switch={
		"emp_name": result[1],
		"emp_username": result[2],
		"emp_password": result[3],
		"store_id": result[4],
		"doj": result[5],
		"phone_no": result[6],
		"designation": result[7],
		"supervisor_id": result[8]
		}
		cursor.close()
		conn.close()
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))


#---------------------------------------------------------------------------------Database Operations--------------------------------------------------------
def plants():
	sql = "SELECT * FROM plant"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			print(row)
		cursor.close()
		conn.close()
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def plantTypes():
	sql = "SELECT * FROM plant_type"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			print(row)
		cursor.close()
		conn.close()
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def lots():
	sql = "SELECT * FROM lot"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			print(row)
		cursor.close()
		conn.close()
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def stores():
	sql = "SELECT * FROM store"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			print(row)
		cursor.close()
		conn.close()
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def customers():
	sql = "SELECT * FROM customer"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			print(row)
		cursor.close()
		conn.close()
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def orders():
	sql = "SELECT * FROM orders"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			print(row)
		cursor.close()
		conn.close()
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def orderItems():
	sql = "SELECT * FROM order_item"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			print(row)
		cursor.close()
		conn.close()
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def employees():
	sql = "SELECT * FROM employee"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			print(row)
		cursor.close()
		conn.close()
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def inEmployee(username):
	sql = "SELECT * FROM employee WHERE emp_username = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (username,))
		result = cursor.fetchone()
		cursor.close()
		conn.close()
		return result
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def inCustomer(username):
	sql = "SELECT * FROM customer WHERE cust_username = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (username,))
		result = cursor.fetchone()
		cursor.close()
		conn.close()
		return result
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
 
def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

def startup():
	#EMPLOYEE
	EmployeeName = "Bee"
	EmployeeUserName = "killabee"
	EmployeePassword = "password"
	EmployeeStoreId = 1
	EmployeeDOJ = "2000-01-25"
	EmployeePhoneNo = "0123456789"
	EmployeeDesignation = "Worker"

	
	
	insert_employee(EmployeeName, EmployeeUserName, EmployeePassword, EmployeeStoreId, EmployeeDOJ, EmployeePhoneNo, EmployeeDesignation, None)
	
	#insert_manager(Name, username, password, storeID, DOJ, phone_no)
	insert_manager("Lebron James","lbj", "password", 1, "2020-01-26", "9876543210")
	insert_manager("Kobe","kobe", "password", 2, "2020-01-26", "9876543210")
	insert_manager("James Harden","jh", "password", 3, "2020-01-26", "9876543210") 
	insert_manager("Wardell Curry","sc", "password", 4, "2020-01-26", "9876543210")
	insert_manager("Klay Thompson","kt", "password", 5, "2020-01-26", "9876543210")
	insert_manager("Draymond Green","dg", "password", 6, "2020-01-26", "9876543210")
	insert_manager("Javale Mcgee","jm", "password", 7, "2020-01-26", "9876543210")
# =======
# import mysql.connector

# mydb = mysql.connector.connect(
# 	host="localhost",
# 	user="root",
# 	passwd="password",
# 	database="nursery"
# )

# cursor = mydb.cursor()
# #-----------------------------------------------INSERT into TABLES------------------------------------------------------------
# def insert_plant(name, price, description, age, lot_id):
# 	sql = "INSERT INTO plant(name, price, description, age, lot_id) VALUES(%s,%s,%s,%s, %s)"
# 	cursor.execute(sql, (name, price, description, age, lot_id))
# 	mydb.commit()

# def insert_plant_type(name, description):
# 	sql = "INSERT INTO plant_type(type_name, description) VALUES(%s,%s)"
# 	cursor.execute(sql, (name, description))
# 	mydb.commit()

# def insert_store(number_of_lots, phone_no, address):
# 	sql = "INSERT INTO store(number_of_lots, phone_no, address) VALUES(%s,%s,%s)"
# 	data = (number_of_lots, phone_no, address)
# 	cursor.execute(sql, data)
# 	mydb.commit()

# def insert_lot(store_id):
# 	sql = "INSERT INTO lot(store_id) VALUES(%s)"
# 	cursor.execute(sql, (store_id,))
# 	mydb.commit()

# def insert_customer(cust_name, cust_username, cust_password, phone_no, address, email_id):
# 	sql = "INSERT INTO customer(cust_name,cust_username, cust_password, phone_no, address, email_id) VALUES(%s,%s,%s, %s,%s,%s)"
# 	data = (cust_name, cust_username, cust_password, phone_no, address, email_id)
# 	cursor.execute(sql, data)
# 	mydb.commit()

# def insert_orders(store_id, cust_id, order_type, payment_status, price, delivery_address):
# 	sql = "INSERT INTO orders(store_id, cust_id, order_type, payment_status, price, delivery_address) VALUES(%s, %s, %s, %s, %s, %s)"
# 	data = (store_id, cust_id, order_type, payment_status, price, delivery_address)
# 	cursor.execute(sql, data)
# 	mydb.commit()

# def insert_order_item(order_id, plant_id, price, rating):
# 	sql = "INSERT INTO order_item(order_id, plant_id,  price, rating) VALUES(%s,%s,%s,%s)"
# 	data = (order_id, plant_id,  price, rating)
# 	cursor.execute(sql, data)
# 	mydb.commit()

# def insert_employee(emp_name, emp_username, emp_password, store_id, doj, phone_no, designation, supervisor_id):
# 	sql = "INSERT INTO employee(emp_name, emp_username, emp_password, store_id, doj, phone_no, designation, supervisor_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
# 	data = (emp_name, emp_username, emp_password, store_id, doj, phone_no, designation, supervisor_id)
# 	cursor.execute(sql, data)
# 	mydb.commit()

# #---------------------------------------------------------UPDATE Tables---------------------------------------------------------------------------
# def update_plant(id, name, price, description, age):
# 	sql = "UPDATE plant SET name = %s, price = %s, description = %s, age = %s WHERE id = %s"
# 	cursor.execute(sql, (name, price, description, age, id))
# 	mydb.commit()

# def update_plant_type (type_id,type_name, description):
# 	sql = "UPDATE plant_type SET type_name = %s, description = %s WHERE type_id = %s"
# 	data = (type_name, description,type_id)
# 	cursor.execute(sql, data)
# 	mydb.commit()

# def update_lot(lot_id, store_id):
# 	sql = "UPDATE lot SET store_id = %s WHERE lot_id = %s"
# 	data = (store_id, lot_id)
# 	cursor.execute(sql, data)
# 	mydb.commit()

# def update_store(store_id, number_of_lots, phone_no, address):
# 	sql = "UPDATE store SET number_of_lots = %s, phone_no = %s, address = %s WHERE store_id = %s"
# 	data = (number_of_lots, phone_no, address, store_id)
# 	cursor.execute(sql, data)
# 	mydb.commit()

# def update_customer(cust_id, cust_name, cust_username, cust_password, phone_no, address, email_id):
# 	sql = "UPDATE customer SET cust_name = %s, cust_username = %s, cust_password = %s, phone_no = %s, address = %s, email_id = %s WHERE cust_id = %s"
# 	data = (cust_id, cust_name, cust_username, cust_password, phone_no, address, email_id)
# 	cursor.execute(sql, data)
# 	mydb.commit()

# def update_orders(order_id, store_id, cust_id, order_type, payment_status, price, delivery_address):
# 	sql = "UPDATE orders SET store_id = %s, cust_id = %s, order_type = %s, payment_status = %s, price = %s, delivery_address = %s WHERE order_id = %s"
# 	data = (store_id, cust_id, order_type, payment_status, price, delivery_address, order_id)
# 	cursor.execute(sql, data)
# 	mydb.commit()

# def update_order_item(item_id, order_id,  plant_id, price, rating,):
# 	sql = "UPDATE order_item SET order_id = %s, plant_id = %s, price = %s, rating = %s WHERE item_id = %s "
# 	data = (order_id, plant_id,price, rating,  item_id)
# 	cursor.execute(sql, data)
# 	mydb.commit()

# def update_employee(emp_id, emp_name, emp_username, emp_password, store_id, doj, phone_no, designation, supervisor_id):
# 	sql = "UPDATE employee SET emp_name = %s, emp_username = %s, emp_password = %s, store_id = %s, doj = %s, phone_no = %s, designation = %s, supervisor_id = %s WHERE emp_id = %s"
# 	data = (emp_id, emp_name, emp_username, emp_password, store_id, doj, phone_no, designation, supervisor_id)
# 	cursor.execute(sql, data)
# 	mydb.commit()

# # Jasper's changes
# def update_supID(emp_id, supervisor_id):
# 	sql = "UPDATE employee SET supervisor_id = %s WHERE emp_id = %s"
# 	data = (supervisor_id, emp_id)
# 	cursor.execute(sql, data)
# 	mydb.commit()

# #-------------------------------------------------------------------------------------DELETE from Tables-----------------------------------------------
# def delete_plant(id):
# 	sql = "DELETE FROM plant WHERE id = %s"
# 	cursor.execute(sql, (id,))
# 	mydb.commit()

# def delete_plant_type(type_id):
# 	sql = "DELETE FROM plant_type WHERE type_id = %s"
# 	cursor.execute(sql, (type_id,))
# 	mydb.commit()

# def delete_lot(lot_id):
# 	sql = "DELETE FROM lot WHERE lot_id = %s"
# 	cursor.execute(sql, (lot_id,))
# 	mydb.commit()


# def delete_store(store_id):
# 	sql = "DELETE FROM store WHERE store_id = %s"
# 	cursor.execute(sql, (store_id,))
# 	mydb.commit()

# def delete_customer(cust_id):
# 	sql = "DELETE FROM customer WHERE cust_id = %s"
# 	cursor.execute(sql, (cust_id,))
# 	mydb.commit()

# def delete_orders(order_id):
# 	sql = "DELETE FROM orders WHERE order_id = %s"
# 	cursor.execute(sql, (order_id,))
# 	mydb.commit()

# def delete_order_item(item_id):
# 	sql = "DELETE FROM order_item WHERE item_id = %s"
# 	cursor.execute(sql, (item_id,))
# 	mydb.commit()

# def delete_employee(emp_id):
# 	sql = "DELETE FROM employee WHERE emp_id = %s"
# 	cursor.execute(sql, (emp_id,))
# 	mydb.commit()

# #---------------------------------------SELECT from Tables---------------------------------------------------
# def getPlant(id, field):
# 	sql = "SELECT * FROM plant WHERE id = %s"
# 	try:
# 		cursor.execute(sql, (id,))
# 		result = cursor.fetchone()
# 		switch={
# 		"name": result[1],
# 		"price": result[2],
# 		"description": result[3],
# 		"age": result[4]
# 		}
# 		return switch.get(field, "NOT FOUND")
# 	except mysql.connector.Error as err:
# 		print("MYSQL ERROR: {}".format(err))

# def getPlantType(type_id, field):
# 	sql = "SELECT * FROM plant_type WHERE type_id = %s"
# 	try:
# 		cursor.execute(sql, (type_id,))
# 		result = cursor.fetchone()
# 		switch={
# 		"type_name": result[1],
# 		"description": result[2]
# 		}
# 		return switch.get(field, "NOT FOUND")
# 	except mysql.connector.Error as err:
# 		print("MYSQL ERROR: {}".format(err))

# def getLot(lot_id, field):
# 	sql = "SELECT * FROM lot WHERE lot_id = %s"
# 	try:
# 		cursor.execute(sql, (lot_id,))
# 		result = cursor.fetchone()
# 		switch={
# 		"store_id": result[1],
# 		}
# 		return switch.get(field, "NOT FOUND")
# 	except mysql.connector.Error as err:
# 		print("MYSQL ERROR: {}".format(err))

# def getStore(store_id, field):
# 	sql = "SELECT * FROM store WHERE store_id = %s"
# 	try:
# 		cursor.execute(sql, (store_id,))
# 		result = cursor.fetchone()
# 		switch={
# 		"number_of_lots": result[1],
# 		"phone_no": result[2],
# 		"address": result[3]
# 		}
# 		return switch.get(field, "NOT FOUND")
# 	except mysql.connector.Error as err:
# 		print("MYSQL ERROR: {}".format(err))

# def getCustomer(cust_id, field):
# 	sql = "SELECT * FROM customer WHERE cust_id = %s"
# 	try:
# 		cursor.execute(sql, (cust_id,))
# 		result = cursor.fetchone()
# 		switch={
# 		"cust_name": result[1],
# 		"cust_username": result[2],
# 		"cust_password": result[3],
# 		"phone_no": result[4],
# 		"address": result[5],
# 		"email_id": result[6]
# 		}
# 		return switch.get(field, "NOT FOUND")
# 	except mysql.connector.Error as err:
# 		print("MYSQL ERROR: {}".format(err))

# def getCustomerLogin(username, field):
# 	sql = "SELECT * FROM customer WHERE username = %s"
# 	try:
# 		cursor.execute(sql, (username,))
# 		result = cursor.fetchone()
# 		switch={
# 		"cust_name": result[1],
# 		"cust_username": result[2],
# 		"cust_password": result[3],
# 		"phone_no": result[4],
# 		"address": result[5],
# 		"email_id": result[6]
# 		}
# 		return switch.get(field, "NOT FOUND")
# 	except mysql.connector.Error as err:
# 		print("MYSQL ERROR: {}".format(err))

# def getOrders(order_id, field):
# 	sql = "SELECT * FROM orders WHERE order_id = %s"
# 	try:
# 		cursor.execute(sql, (order_id,))
# 		result = cursor.fetchone()
# 		switch={
# 		"store_id": result[1],
# 		"cust_id": result[2],
# 		"order_type": result[3],
# 		"payment_status": result[4],
# 		"price": result[5],
# 		"delivery_address": result[6]
# 		}
# 		return switch.get(field, "NOT FOUND")
# 	except mysql.connector.Error as err:
# 		print("MYSQL ERROR: {}".format(err))

# def getOrderItem(item_id, field):
# 	sql = "SELECT * FROM order_item WHERE item_id = %s"
# 	try:
# 		cursor.execute(sql, (item_id,))
# 		result = cursor.fetchone()
# 		switch={
# 		"order_id": result[1],
# 		"plant_id": result[2],
# 		"price": result[3],
# 		"rating": result[4]
# 		}
# 		return switch.get(field, "NOT FOUND")
# 	except mysql.connector.Error as err:
# 		print("MYSQL ERROR: {}".format(err))

# def getEmployee(emp_id, field):
# 	sql = "SELECT * FROM employee WHERE emp_id = %s"
# 	try:
# 		cursor.execute(sql, (emp_id,))
# 		result = cursor.fetchone()
# 		switch={
# 		"emp_name": result[1],
# 		"emp_username": result[2],
# 		"emp_password": result[3],
# 		"store_id": result[4],
# 		"doj": result[5],
# 		"phone_no": result[6],
# 		"designation": result[7],
# 		"supervisor_id": result[8]
# 		}
# 		return switch.get(field, "NOT FOUND")
# 	except mysql.connector.Error as err:
# 		print("MYSQL ERROR: {}".format(err))

# # Jasper's changes
# def getEmployees(storeID):
# 	sql = "SELECT * FROM employee WHERE store_id = %s"
# 	try:
# 		cursor.execute(sql, (storeID,))
# 		result = cursor.fetchall()
# 		return result
# 	except mysql.connector.Error as err:
# 		print("MYSQL ERROR: {}".format(err))

# def getEmployeeLogin(username, field):
# 	sql = "SELECT * FROM employee WHERE emp_username = %s"
# 	try:
# 		cursor.execute(sql, (username,))
# 		result = cursor.fetchone()
# 		switch={
# 		"emp_name": result[1],
# 		"emp_username": result[2],
# 		"emp_password": result[3],
# 		"store_id": result[4],
# 		"doj": result[5],
# 		"phone_no": result[6],
# 		"designation": result[7],
# 		"supervisor_id": result[8]
# 		}
# 		return switch.get(field, "NOT FOUND")
# 	except mysql.connector.Error as err:
# 		print("MYSQL ERROR: {}".format(err))


# #---------------------------------------------------------------------------------Database Operations--------------------------------------------------------
# def plants():
# 	sql = "SELECT * FROM plant"
# 	try:
# 		cursor.execute(sql)
# 		result = cursor.fetchall()
# 		for row in result:
# 			print(row)
# 	except mysql.connector.Error as err:
# 		print("MYSQL ERROR: {}".format(err))

# def plantTypes():
# 	sql = "SELECT * FROM plant_type"
# 	try:
# 		cursor.execute(sql)
# 		result = cursor.fetchall()
# 		for row in result:
# 			print(row)
# 	except mysql.connector.Error as err:
# 		print("MYSQL ERROR: {}".format(err))

# def lots():
# 	sql = "SELECT * FROM lot"
# 	try:
# 		cursor.execute(sql)
# 		result = cursor.fetchall()
# 		for row in result:
# 			print(row)
# 	except mysql.connector.Error as err:
# 		print("MYSQL ERROR: {}".format(err))

# def stores():
# 	sql = "SELECT * FROM store"
# 	try:
# 		cursor.execute(sql)
# 		result = cursor.fetchall()
# 		for row in result:
# 			print(row)
# 	except mysql.connector.Error as err:
# 		print("MYSQL ERROR: {}".format(err))

# def customers():
# 	sql = "SELECT * FROM customer"
# 	try:
# 		cursor.execute(sql)
# 		result = cursor.fetchall()
# 		for row in result:
# 			print(row)
# 	except mysql.connector.Error as err:
# 		print("MYSQL ERROR: {}".format(err))

# def orders():
# 	sql = "SELECT * FROM orders"
# 	try:
# 		cursor.execute(sql)
# 		result = cursor.fetchall()
# 		for row in result:
# 			print(row)
# 	except mysql.connector.Error as err:
# 		print("MYSQL ERROR: {}".format(err))

# def orderItems():
# 	sql = "SELECT * FROM order_item"
# 	try:
# 		cursor.execute(sql)
# 		result = cursor.fetchall()
# 		for row in result:
# 			print(row)
# 	except mysql.connector.Error as err:
# 		print("MYSQL ERROR: {}".format(err))

# def employees():
# 	sql = "SELECT * FROM employee"
# 	try:
# 		cursor.execute(sql)
# 		result = cursor.fetchall()
# 		for row in result:
# 			print(row)
# 	except mysql.connector.Error as err:
# 		print("MYSQL ERROR: {}".format(err))

# def inEmployee(username):
# 	sql = "SELECT * FROM employee WHERE emp_username = %s"
# 	try:
# 		cursor.execute(sql, (username,))
# 		result = cursor.fetchone()
# 		return result
# 	except mysql.connector.Error as err:
# 		print("MYSQL ERROR: {}".format(err))

# def inCustomer(username):
# 	sql = "SELECT * FROM customer WHERE cust_username = %s"
# 	try:
# 		cursor.execute(sql, (username,))
# 		result = cursor.fetchone()
# 		return result
# 	except mysql.connector.Error as err:
# 		print("MYSQL ERROR: {}".format(err))

# def startup():
# 	#STORE
# 	storeLots = 50
# 	storePhoneNo = "0123456789"
# 	storeAddress = "2341 Redneck Dr."

# 	#LOT
# 	lotStoreId = 1

# 	#PLANTS
# 	plantName = "queenPalm"
# 	plantPrice = 25.50
# 	plantDescription = "YAASSS QUEEEN!!"
# 	plantAge = 21
# 	plantLotId = 1

# 	#PLANT TYPES
# 	plantTypeName = "tree"
# 	plantTypeDescription = "tall plant"

# 	#CUSTOMER
# 	customerName = "jeff"
# 	customerUserName = "jefe"
# 	customerPassword = "myNameJeff"
# 	customerPhoneNo = "0123456789"
# 	customerAddress = "1234 Robin Wy."
# 	customerEmail = "jeff@gmail.com"

# 	#ORDERS
# 	OrderStoreId = 1
# 	OrderCustId = 1
# 	OrderType = "single"
# 	OrderPaymentStatus = "Paid"
# 	OrderPrice = 120.99
# 	OrderDeliveryAddress = "5738 Applegate Ave."

# 	#ORDER_ITEM
# 	OrderID = 1
# 	OrderPlantID = 1
# 	OrderItemPrice = 123.67
# 	OrderRating = 4.5

# 	#EMPLOYEE
# 	EmployeeName = "Bee"
# 	EmployeeUserName = "killabee"
# 	EmployeePassword = "password"
# 	EmployeeStoreId = 1
# 	EmployeeDOJ = "2000-01-25"
# 	EmployeePhoneNo = "0123456789"
# 	EmployeeDesignation = "Worker"
# 	EmployeeSupervisor = 4


# 	insert_store(storeLots, storePhoneNo, storeAddress)
# 	insert_lot(lotStoreId)
# 	insert_plant(plantName, plantPrice, plantDescription, plantAge, plantLotId)
# 	insert_plant_type(plantTypeName, plantTypeDescription)
# 	insert_customer(customerName, customerUserName, customerPassword, customerPhoneNo, customerAddress, customerEmail)
# 	insert_orders(OrderStoreId, OrderCustId, OrderType, OrderPaymentStatus, OrderPrice, OrderDeliveryAddress)
# 	insert_order_item(OrderID, OrderPlantID, OrderItemPrice, OrderRating)
# 	insert_employee(EmployeeName, EmployeeUserName, EmployeePassword, EmployeeStoreId, EmployeeDOJ, EmployeePhoneNo, EmployeeDesignation, EmployeeSupervisor)

# #---------------------------------------------------------------------------------TEST SCRIPTS--------------------------------------------------------
# def main():
# 	print("------------------STORE---------------------------")
# 	print("Store Number of Lots is: " + str(getStore(1, "number_of_lots")))
# 	print("Store Phone Number is: " + getStore(1, "phone_no"))
# 	print("Store Address is: " + getStore(1, "address"))

# 	print("-----------------------LOT---------------------------")
# 	print("Lot StoreId is: " + str(getLot(1, "store_id")))

# 	print("-----------------PLANT TABLE-----------------")
# 	print("Plant name is: " + getPlant(1, "name"))
# 	print("Plant price is: " + str(getPlant(1, "price")))
# 	print("Plant description is: " + getPlant(1, "description"))
# 	print("Plant age is: " + str(getPlant(1, "age")))

# 	print("------------------PLANT TYPE------------------")
# 	print("PlantType name is: " + getPlantType(1, "type_name"))
# 	print("PlantType description is: " + getPlantType(1, "description"))

# 	print("------------------CUSTOMER---------------------------")
# 	print("Customer Name is: " + getCustomer(1, "cust_name"))
# 	print("Customer UserName is: " + getCustomer(1, "cust_username"))
# 	print("Customer Password is: " + getCustomer(1, "cust_password"))
# 	print("Customer Phone Number is: " + getCustomer(1, "phone_no"))
# 	print("Customer Address is: " + getCustomer(1, "address"))
# 	print("Customer Email is: " + getCustomer(1, "email_id"))

# 	print("-------------------------ORDERS-------------------------")
# 	print("Orders StoreId is: " + str(getOrders(1, "store_id")))
# 	print("Orders CustomerId is: " + str(getOrders(1, "cust_id")))
# 	print("Orders Order Type is: " + getOrders(1, "order_type"))
# 	print("Orders Payment Status is: " + getOrders(1, "payment_status"))
# 	print("Orders Price is: " + str(getOrders(1, "price")))
# 	print("Orders Delivery Address is: " + getOrders(1, "delivery_address"))

# 	print("-------------------------ORDER ITEM-------------------------")
# 	print("OrderItem OrderId is: " + str(getOrderItem(1, "order_id")))
# 	print("OrderItem PlantId is: " + str(getOrderItem(1, "plant_id")))
# 	print("OrderItem Price is: " + str(getOrderItem(1, "price")))
# 	print("OrderItem Rating is: " + str(getOrderItem(1, "rating"))	)

# 	print("-------------------------EMPLOYEE-------------------------")
# 	print("Employee Name is: " + getEmployee(1, "emp_name"))
# 	print("Employee UserName is: " + getEmployee(1, "emp_username"))
# 	print("Employee Password is: " + getEmployee(1, "emp_password"))
# 	print("Employee Store Id is: " + str(getEmployee(1, "store_id")))
# 	print("Employee DOJ is: " + str(getEmployee(1, "doj")))
# 	print("Employee Phone Number is: " + getEmployee(1, "phone_no"))
# 	print("Employee Designation is: " + getEmployee(1, "designation"))
# 	print("Employee Supervisor Id is: " + str(getEmployee(1, "supervisor_id")))

# 	# -----------------------------------------------UPDATE--------------------------------------------------------

# 	update_store(1, 49, "9876543210", "3241 Bobcat St.")
# 	update_lot(1, 1)
# 	update_plant(1, "King Plam", 47, "Royal Palm", 24)
# 	update_plant_type(1, "StillTree",  "TallTree")

# 	update_customer(1, "Bob", "Bobdat", "pass", "9876543210", "4321 Batman Cv", "Bob@yahoo.com")
# 	update_orders(1,1,1, "double", "Payment Due", 666.21, "57312 treeapple Wy.")
# 	update_order_item(1,1,1, 432, 6.7)
# 	update_employee(1, "Lebron James","KingLBJ", "bronny", 1, "2020-01-26", "9876543210", "KingJames", 7)

# 	#------------------------------------AFTER UPDATE----------------------------------------------------

# 	print("------------------------------------AFTER UPDATE----------------------------------------------------")

# 	print("------------------STORE---------------------------")
# 	print("Store Number of Lots is: " + str(getStore(1, "number_of_lots")))
# 	print("Store Phone Number is: " + getStore(1, "phone_no"))
# 	print("Store Address is: " + getStore(1, "address"))

# 	print("-----------------------LOT---------------------------")
# 	print("Lot StoreId is: " + str(getLot(1, "store_id")))

# 	print("-----------------PLANT TABLE-----------------")
# 	print("Plant name is: " + getPlant(1, "name"))
# 	print("Plant price is: " + str(getPlant(1, "price")))
# 	print("Plant description is: " + getPlant(1, "description"))
# 	print("Plant age is: " + str(getPlant(1, "age")))

# 	print("------------------PLANT TYPE------------------")
# 	print("PlantType name is: " + getPlantType(1, "type_name"))
# 	print("PlantType description is: " + getPlantType(1, "description"))

# 	print("------------------CUSTOMER---------------------------")
# 	print("Customer Name is: " + getCustomer(1, "cust_name"))
# 	print("Customer UserName is: " + getCustomer(1, "cust_username"))
# 	print("Customer Password is: " + getCustomer(1, "cust_password"))
# 	print("Customer Phone Number is: " + getCustomer(1, "phone_no"))
# 	print("Customer Address is: " + getCustomer(1, "address"))
# 	print("Customer Email is: " + getCustomer(1, "email_id"))

# 	print("-------------------------ORDERS-------------------------")
# 	print("Orders StoreId is: " + str(getOrders(1, "store_id")))
# 	print("Orders CustomerId is: " + str(getOrders(1, "cust_id")))
# 	print("Orders Order Type is: " + getOrders(1, "order_type"))
# 	print("Orders Payment Status is: " + getOrders(1, "payment_status"))
# 	print("Orders Price is: " + str(getOrders(1, "price")))
# 	print("Orders Delivery Address is: " + getOrders(1, "delivery_address"))

# 	print("-------------------------ORDER ITEM-------------------------")
# 	print("OrderItem OrderId is: " + str(getOrderItem(1, "order_id")))
# 	print("OrderItem PlantId is: " + str(getOrderItem(1, "plant_id")))
# 	print("OrderItem Price is: " + str(getOrderItem(1, "price")))
# 	print("OrderItem Rating is: " + str(getOrderItem(1, "rating"))	)

# 	print("-------------------------EMPLOYEE-------------------------")
# 	print("Employee Name is: " + getEmployee(1, "emp_name"))
# 	print("Employee UserName is: " + getEmployee(1, "emp_username"))
# 	print("Employee Password is: " + getEmployee(1, "emp_password"))
# 	print("Employee Store Id is: " + str(getEmployee(1, "store_id")))
# 	print("Employee DOJ is: " + str(getEmployee(1, "doj")))
# 	print("Employee Phone Number is: " + getEmployee(1, "phone_no"))
# 	print("Employee Designation is: " + getEmployee(1, "designation"))
# 	print("Employee Supervisor Id is: " + str(getEmployee(1, "supervisor_id")))

# 	delete_plant(1)
# 	delete_plant_type(1)
# 	delete_store(1)
# 	delete_store(1)
# 	delete_customer(1)
# 	delete_orders(1)
# 	delete_order_item(1)
# 	delete_employee(1)


# 	print("------------------------------------AFTER DELETE----------------------------------------------------")

# 	print("------------------STORE---------------------------")
# 	stores()

# 	print("------------------LOT---------------------------")
# 	lots()

# 	print("-----------------PLANT TABLE-----------------")
# 	plants()

# 	print("------------------PLANT TYPE------------------")
# 	plantTypes()

# 	print("------------------CUSTOMER---------------------------")
# 	customers()

# 	print("-------------------------ORDERS-------------------------")
# 	orders()

# 	print("-------------------------ORDER ITEM-------------------------")
# 	orderItems()

# 	print("-------------------------EMPLOYEE-------------------------")
# 	employees()
# >>>>>>> Jasper
