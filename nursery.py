
import mysql.connector
import hashlib
import binascii
import os
import csv
import logging
logging.basicConfig(filename="nursery.log", level=logging.DEBUG)


def getConnection():
	conn = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="password",
		database="Nursery"
	)
	return conn

#-----------------------------------------------INSERT into TABLES------------------------------------------------------------
def insert_plant(name, price, description, age):
	logging.info("insert_plant(): attempting to insert data into plant table")
	conn = getConnection()
	cursor = conn.cursor()
	sql = "INSERT INTO plant(name, price, description, age) VALUES(%s,%s,%s,%s)"
	cursor.execute(sql, (name, price, description, age)) #p_type_id
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("insert_plant(): insert into plant table successful")

def insert_plant_with_type(name, price, description, age, p_type_id):
	logging.info("insert_plant_with_type(): attempting to insert data into plant table")
	conn = getConnection()
	cursor = conn.cursor()
	sql = "INSERT INTO plant(name, price, description, age, p_type_id) VALUES(%s,%s,%s,%s,%s)"
	cursor.execute(sql, (name, price, description, age, p_type_id))
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("insert_plant_with_type(): insert into plant table successful")

def insert_plant_type(name, description):
	logging.info("insert_plant_type(): attempting to insert data into plant_type table")
	conn = getConnection()
	cursor = conn.cursor()
	sql = "INSERT INTO plant_type(type_name, description) VALUES(%s,%s)"
	cursor.execute(sql, (name, description))
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("insert_plant_type(): attempting to insert data into plant_type table")

def insert_store(number_of_lots, phone_no, address):
	logging.info("insert_store(): attempting to insert data into store table")
	conn = getConnection()
	cursor = conn.cursor()
	sql = "INSERT INTO store(number_of_lots, phone_no, address) VALUES(%s,%s,%s)"
	data = (number_of_lots, phone_no, address)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("insert_store(): insert into store table successful")


def insert_lot(store_id):
	logging.info("insert_lot(): attempting to insert data into lot table")
	conn = getConnection()
	cursor = conn.cursor()
	sql = "INSERT INTO lot(store_id) VALUES(%s)"
	cursor.execute(sql, (store_id,))
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("insert_lot(): insert into lot table successful")


def insert_customer(cust_name, cust_username, cust_password, phone_no, address, email_id):
	logging.info("insert_customer(): attempting to insert data into customer table")
	conn = getConnection()
	cursor = conn.cursor()
	hashed_password = hash_password(cust_password)
	sql = "INSERT INTO customer(cust_name,cust_username, cust_password, phone_no, address, email_id) VALUES(%s,%s,%s, %s,%s,%s)"
	data = (cust_name, cust_username, hashed_password, phone_no, address, email_id)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("insert_customer(): insert into customer table successful")


def insert_orders(store_id, cust_id, order_type, payment_status, price, delivery_address):
	logging.info("insert_orders(): attempting to insert data into orders table")
	conn = getConnection()
	cursor = conn.cursor()
	sql = "INSERT INTO orders(store_id, cust_id, order_type, payment_status, price, delivery_address) VALUES(%s, %s, %s, %s, %s, %s)"
	data = (store_id, cust_id, order_type, payment_status, price, delivery_address)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("insert_orders(): insert into orders table successful")


def insert_order_item(order_id, plant_id, price, rating):
	logging.info("insert_order_item(): attempting to insert data into order_item table")
	conn = getConnection()
	cursor = conn.cursor()
	sql = "INSERT INTO order_item(order_id, plant_id,  price, rating) VALUES(%s,%s,%s,%s)"
	data = (order_id, plant_id,  price, rating)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("insert_order_item(): insert into order_item table successful")


def insert_employee(emp_name, emp_username, emp_password, store_id, doj, phone_no, designation, supervisor_id):
	logging.info("insert_employee(): attempting to insert data into employee table")
	conn = getConnection()
	cursor = conn.cursor()
	hashed_password = hash_password(emp_password)
	sql = "INSERT INTO employee(emp_name, emp_username, emp_password, store_id, doj, phone_no, designation, supervisor_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
	data = (emp_name, emp_username, hashed_password, store_id, doj, phone_no, designation, supervisor_id)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("insert_employee(): insert into employee table successful")


def insert_manager(emp_name, emp_username, emp_password, store_id, doj, phone_no):
	logging.info("insert_manager(): attempting to insert data into employee table")
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
	logging.info("insert_manager(): insert into employee table successful")

#---------------------------------------------------------UPDATE Tables---------------------------------------------------------------------------
def update_plant(plant_id, name, price, description, age):
	logging.info("update_plant(): attempting to update data for plant id '%s'", plant_id)
	conn = getConnection()
	cursor = conn.cursor()
	sql = "UPDATE plant SET name = %s, price = %s, description = %s, age = %s WHERE plant_id = %s"
	cursor.execute(sql, (name, price, description, age, plant_id))
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("update_plant(): update of plant table successful for id '%s'", plant_id)


def update_plant_type (type_id,type_name, description):
	logging.info("update_plant_type(): attempting to update data for plant_type id '%s'", type_id)
	conn = getConnection()
	cursor = conn.cursor()
	sql = "UPDATE plant_type SET type_name = %s, description = %s WHERE type_id = %s"
	data = (type_name, description,type_id)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("update_plant_type(): update of plant_type table successful for id '%s'", type_id)


def update_lot(lot_id, store_id):
	logging.info("update_lot(): attempting to update data for lot id '%s'", lot_id)
	conn = getConnection()
	cursor = conn.cursor()
	sql = "UPDATE lot SET store_id = %s WHERE lot_id = %s"
	data = (store_id, lot_id)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("update_lot(): update of lot table successful for id '%s'", lot_id)


def update_store(store_id, number_of_lots, phone_no, address):
	logging.info("update_store(): attempting to update data for store id '%s'", store_id)
	conn = getConnection()
	cursor = conn.cursor()
	sql = "UPDATE store SET number_of_lots = %s, phone_no = %s, address = %s WHERE store_id = %s"
	data = (number_of_lots, phone_no, address, store_id)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("update_store(): update of store table successful for id '%s'", store_id)


def update_customer(cust_id, cust_name, cust_username, cust_password, phone_no, address, email_id):
	logging.info("update_customer(): attempting to update data for customer id '%s'", cust_id)
	conn = getConnection()
	cursor = conn.cursor()
	hashed_password = hash_password(cust_password)
	sql = "UPDATE customer SET cust_name = %s, cust_username = %s, cust_password = %s, phone_no = %s, address = %s, email_id = %s WHERE cust_id = %s"
	data = (cust_name, cust_username, hashed_password, phone_no, address, email_id, cust_id)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("update_customer(): update of customer table successful for id '%s'", cust_id)


def update_orders(order_id, store_id, cust_id, order_type, payment_status, price, delivery_address):
	logging.info("update_orders(): attempting to update data for order id '%s'", order_id)
	conn = getConnection()
	cursor = conn.cursor()
	sql = "UPDATE orders SET store_id = %s, cust_id = %s, order_type = %s, payment_status = %s, price = %s, delivery_address = %s WHERE order_id = %s"
	data = (store_id, cust_id, order_type, payment_status, price, delivery_address, order_id)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("update_orders(): update of orders table successful for id '%s'", order_id)


def update_order_item(item_id, order_id,  plant_id, price, rating,):
	logging.info("update_order_item(): attempting to update data for order_item id '%s'", item_id)
	conn = getConnection()
	cursor = conn.cursor()
	sql = "UPDATE order_item SET order_id = %s, plant_id = %s, price = %s, rating = %s WHERE item_id = %s "
	data = (order_id, plant_id,price, rating,  item_id)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("update_order_item(): update of order_item table successful for id '%s'", item_id)


def update_employee(emp_id, emp_name, emp_username, emp_password, store_id, doj, phone_no, designation, supervisor_id):
	logging.info("update_employee(): attempting to update data for employee id '%s'", emp_id)
	conn = getConnection()
	cursor = conn.cursor()
	hashed_password = hash_password(emp_password)
	sql = "UPDATE employee SET emp_name = %s, emp_username = %s, emp_password = %s, store_id = %s, doj = %s, phone_no = %s, designation = %s, supervisor_id = %s WHERE emp_id = %s"
	data = (emp_name, emp_username, hashed_password, store_id, doj, phone_no, designation, supervisor_id, emp_id)
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("update_employee(): update of employee table successful for id '%s'", emp_id)

#-------------------------------------------------------------------------------------DELETE from Tables-----------------------------------------------
def delete_plant(id):
	logging.info("delete_plant(): attempting to delete plant with id '%s'", id)
	conn = getConnection()
	cursor = conn.cursor()
	sql = "DELETE FROM plant WHERE plant_id = %s"
	cursor.execute(sql, (id,))
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("delete_plant(): delete of plant successful for id '%s'", id)


def delete_plant_type(type_id):
	logging.info("delete_plant_type(): attempting to delete plant_type with id '%s'", type_id)
	conn = getConnection()
	cursor = conn.cursor()
	sql = "DELETE FROM plant_type WHERE type_id = %s"
	cursor.execute(sql, (type_id,))
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("delete_plant_type(): delete of plant_type successful for id '%s'", type_id)


def delete_lot(lot_id):
	logging.info("delete_lot(): attempting to delete lot with id '%s'", lot_id)
	conn = getConnection()
	cursor = conn.cursor()
	sql = "DELETE FROM lot WHERE lot_id = %s"
	cursor.execute(sql, (lot_id,))
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("delete_lot(): delete of lot successful for id '%s'", lot_id)


def delete_store(store_id):
	logging.info("delete_store(): attempting to delete store with id '%s'", store_id)
	conn = getConnection()
	cursor = conn.cursor()
	sql = "DELETE FROM store WHERE store_id = %s"
	cursor.execute(sql, (store_id,))
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("delete_store(): delete of store successful for id '%s'", store_id)


def delete_customer(cust_id):
	logging.info("delete_customer(): attempting to delete customer with id '%s'", cust_id)
	conn = getConnection()
	cursor = conn.cursor()
	sql = "DELETE FROM customer WHERE cust_id = %s"
	cursor.execute(sql, (cust_id,))
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("delete_customer(): delete of customer successful for id '%s'", cust_id)


def delete_orders(order_id):
	logging.info("delete_orders(): attempting to delete order with id '%s'", order_id)
	conn = getConnection()
	cursor = conn.cursor()
	sql = "DELETE FROM orders WHERE order_id = %s"
	cursor.execute(sql, (order_id,))
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("delete_orders(): delete of order successful for id '%s'", order_id)


def delete_order_item(item_id):
	logging.info("delete_order_item(): attempting to delete order_item with id '%s'", item_id)
	conn = getConnection()
	cursor = conn.cursor()
	sql = "DELETE FROM order_item WHERE item_id = %s"
	cursor.execute(sql, (item_id,))
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("delete_order_item(): delete of order_item successful for id '%s'", item_id)


def delete_employee(emp_id):
	logging.info("delete_plant(): attempting to delete employee with id '%s'", emp_id)
	conn = getConnection()
	cursor = conn.cursor()
	sql = "DELETE FROM employee WHERE emp_id = %s"
	cursor.execute(sql, (emp_id,))
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("delete_plant(): delete of employee successful for id '%s'", emp_id)


#---------------------------------------SELECT from Tables---------------------------------------------------
def getPlant(id, field):
	logging.info("getPlant(): attempting to fetch plant with id '%s'", id)
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
		logging.info("getPlant(): fetched plant data successfully for id '%s'", id)
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		logging.error("getPlant(): {}".format(err))


def getPlantName(name, field):
	logging.info("getPlantName(): attempting to fetch plant with name '%s'", name)
	sql = "SELECT * FROM plant WHERE name = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (name,))
		result = cursor.fetchone()
		switch={
		"plant_id": result[0],
		"price": result[2],
		"description": result[3],
		"age": result[4]
		}
		cursor.close()
		conn.close()
		logging.info("getPlantName(): fetched plant data successfully for id '%s'", id)
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		logging.error("getPlantName(): {}".format(err))


def getPlantType(type_id, field):
	logging.info("getPlantType(): attempting to fetch plant with type '%s'", type_id)
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
		logging.info("getPlantType(): fetched plant data successfully for type id '%s'", type_id)
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		logging.error("getPlantType(): {}".format(err))


def getLot(lot_id, field):
	logging.info("getLot(): attempting to fetch lot with id '%s'", lot_id)
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
		logging.info("getPlantType(): fetched lot data successfully for lot id '%s'", lot_id)
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		logging.error("MYSQL ERROR: {}".format(err))


def getStore(store_id, field):
	logging.info("getStore(): attempting to fetch store with id '%s'", store_id)
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
		logging.info("getStore(): fetched store data successfully for id '%s'", store_id)
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		logging.error("getStore(): {}".format(err))


def getCustomer(cust_id, field):
	logging.info("getCustomer(): attempting to fetch customer with id '%s'", cust_id)
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
		logging.info("getCustomer(): fetched customer data successfully for id '%s'", cust_id)
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		logging.error("getCustomer(): {}".format(err))


def getCustomerByName(cust_username, field):
	sql = "SELECT * FROM customer WHERE cust_username = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (cust_username,))
		result = cursor.fetchone()
		switch={
		"cust_name": result[1],
		"cust_id": result[0],
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
	logging.info("getCustomerLogin(): attempting to fetch customer with username '%s'", username)
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
		logging.info("getCustomerLogin(): fetched customer data successfully for username '%s'", username)
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		logging.error("getCustomerLogin(): {}".format(err))


def getOrders(order_id, field):
	logging.info("getOrders(): attempting to fetch order with id '%s'", order_id)
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
		logging.info("getOrders(): fetched order data successfully for id '%s'", order_id)
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		logging.error("getOrders(): {}".format(err))


def getOrderItem(item_id, field):
	logging.info("getOrderItem(): attempting to fetch item with id '%s'", item_id)
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
		logging.info("getOrderItem(): fetched order_item data successfully for id '%s'", item_id)
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		logging.error("getOrderItem(): {}".format(err))

def getEmployee(emp_id, field):
	logging.info("getEmployee(): attempting to fetch employee with id '%s'", emp_id)
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
		logging.info("getEmployee(): fetched employee data successfully for id '%s'", emp_id)
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		logging.error("getEmployee(): {}".format(err))

def getEmployeeByName(username, field):
	sql = "SELECT * FROM employee WHERE emp_username = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (username,))
		result = cursor.fetchone()
		switch={
		"emp_name": result[1],
		"emp_id": result[0],
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
	logging.info("getEmployees(): attempting to fetch employee with store id '%s'", storeID)
	sql = "SELECT * FROM employee WHERE store_id = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (storeID,))
		result = cursor.fetchall()
		cursor.close()
		conn.close()
		logging.info("getEmployees(): fetched employees data successfully for store id '%s'", storeID)
		return result
	except mysql.connector.Error as err:
		logging.error("getEmployees(): {}".format(err))


# Jasper's changes
def update_supID(emp_id, supervisor_id):
	logging.info("update_supID(): attempting to update employee of id '%s'", emp_id)
	sql = "UPDATE employee SET supervisor_id = %s, designation = %s WHERE emp_id = %s"
	data = (supervisor_id,"Manager",emp_id)
	conn = getConnection()
	cursor = conn.cursor()
	cursor.execute(sql, data)
	conn.commit()
	cursor.close()
	conn.close()
	logging.info("update_supID(): updated employee data successfully for id '%s'", emp_id)


def getEmployeeLogin(username, field):
	logging.info("getEmployeeLogin(): attempting to fetch employee with username '%s'", username)
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
		logging.info("getEmployeeLogin(): fetched employee data successfully for username '%s'", username)
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		logging.error("getEmployeeLogin(): {}".format(err))


#---------------------------------------------------------------------------------Database Operations--------------------------------------------------------
def plants():
	logging.info("plants(): attempting to fetch all plants")
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
		logging.info("plants(): fetch of plants successful")
	except mysql.connector.Error as err:
		logging.error("plants(): {}".format(err))


def plantTypes():
	logging.info("plantTypes(): attempting to fetch all plant types")
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
		logging.info("plantTypes(): fetch of plant types successful")
	except mysql.connector.Error as err:
		logging.error("plantTypes(): {}".format(err))

def lots():
	logging.info("lots(): attempting to fetch all lots")
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
		logging.info("lots(): fetch of lots successful")
	except mysql.connector.Error as err:
		logging.error("lots(): {}".format(err))

def stores():
	logging.info("stores(): attempting to fetch all stores")
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
		logging.info("stores(): fetch of stores successful")
	except mysql.connector.Error as err:
		logging.error("stores(): {}".format(err))

def customers():
	logging.info("customers(): attempting to fetch all customers")
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
		logging.info("customers(): fetch of customers successful")
	except mysql.connector.Error as err:
		logging.error("customers(): {}".format(err))


def orders():
	logging.info("orders(): attempting to fetch all orders")
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
		logging.info("orders(): fetch of orders successful")
	except mysql.connector.Error as err:
		logging.error("orders(): {}".format(err))


def orderItems():
	logging.info("orderItems(): attempting to fetch all items")
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
		logging.info("orderItems(): fetch of items successful")
	except mysql.connector.Error as err:
		logging.error("orderItems(): {}".format(err))


def employees():
	logging.info("employees(): attempting to fetch all employees")
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
		logging.info("employees(): fetch of employees successful")
	except mysql.connector.Error as err:
		logging.error("employees(): {}".format(err))


def inEmployee(username):
	logging.info("inEmployee(): attempting to fetch employee with username '%s'", username)
	sql = "SELECT * FROM employee WHERE emp_username = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (username,))
		result = cursor.fetchone()
		cursor.close()
		conn.close()
		logging.info("inEmployee(): fetch of employee successful")
		return result
	except mysql.connector.Error as err:
		logging.error("inEmployee(): {}".format(err))


def inCustomer(username):
	logging.info("inCustomer(): attempting to fetch customer with username '%s'", username)
	sql = "SELECT * FROM customer WHERE cust_username = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (username,))
		result = cursor.fetchone()
		cursor.close()
		conn.close()
		logging.info("inCustomer(): fetch of customer successful")
		return result
	except mysql.connector.Error as err:
		logging.error("inCustomer(): {}".format(err))

#------------------------------------------End of SQL queries -----------------------------------------------

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

# Jasper's changes
def initializeEmployee():
	sql = "INSERT INTO employee(emp_name, emp_username, emp_password, store_id, doj, phone_no, designation, supervisor_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		csvFile = csv.reader(open('employee.csv', 'r'))
		for employeeData in csvFile:
			employeeData[2] = hash_password(employeeData[2])
			cursor.execute(sql, employeeData)
		conn.commit()
		cursor.close()
		conn.close()
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))


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

	# Jasper's changes
	initializeEmployee()
