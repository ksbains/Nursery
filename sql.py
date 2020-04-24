<<<<<<< HEAD
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
	sql = "INSERT INTO plant_type(type_name, description) VALUES(%s,%s)"
	cursor.execute(sql, (name, description))
	mydb.commit()

def insert_store(number_of_lots, phone_no, address):
	sql = "INSERT INTO store(number_of_lots, phone_no, address) VALUES(%s,%s,%s)"
	data = (number_of_lots, phone_no, address)
	cursor.execute(sql, data)
	mydb.commit()

def insert_customer(cust_name, phone_no, address, email_id):
	sql = "INSERT INTO customer(cust_name, phone_no, address, email_id) VALUES(%s,%s,%s,%s)"
	data = (cust_name, phone_no, address, email_id)
	cursor.execute(sql, data)
	mydb.commit()

def insert_orders(store_id, cust_id, order_type, payment_status, price, delivery_address):
	sql = "INSERT INTO orders(store_id, cust_id, order_type, payment_status, price, delivery_address) VALUES(%s, %s, %s, %s, %s, %s)"
	data = (store_id, cust_id, order_type, payment_status, price, delivery_address)
	cursor.execute(sql, data)
	mydb.commit()

def insert_order_item(order_id, plant_id, price, rating):
	sql = "INSERT INTO order_item(order_id, plant_id,  price, rating) VALUES(%s,%s,%s,%s)"
	data = (order_id, plant_id,  price, rating)
	cursor.execute(sql, data)
	mydb.commit()

def insert_employee(emp_name, store_id, doj, phone_no, designation, supervisor_id):
	sql = "INSERT INTO employee(emp_name, store_id, doj, phone_no, designation, supervisor_id) VALUES(%s,%s,%s,%s,%s,%s)"
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
	sql = "UPDATE store SET number_of_lots = %s, phone_no = %s, address = %s WHERE store_id = %s"
	data = (number_of_lots, phone_no, address, store_id)
	cursor.execute(sql, data)
	mydb.commit()

def update_customer(cust_id, cust_name, phone_no, address, email_id):
	sql = "UPDATE customer SET cust_name = %s, phone_no = %s, address = %s, email_id = %s WHERE cust_id = %s"
	data = (cust_name, phone_no, address, email_id, cust_id)
	cursor.execute(sql, data)
	mydb.commit()

def update_orders(order_id, store_id, cust_id, order_type, payment_status, price, delivery_address):
	sql = "UPDATE orders SET store_id = %s, cust_id = %s, order_type = %s, payment_status = %s, price = %s, delivery_address = %s WHERE order_id = %s"
	data = (store_id, cust_id, order_type, payment_status, price, delivery_address, order_id)
	cursor.execute(sql, data)
	mydb.commit()

def update_order_item(item_id, order_id,  plant_id, price, rating,):
	sql = "UPDATE order_item SET order_id = %s, plant_id = %s, price = %s, rating = %s WHERE item_id = %s "
	data = (order_id, plant_id,price, rating,  item_id)
	cursor.execute(sql, data)
	mydb.commit()

def update_employee(emp_id, emp_name, store_id, doj, phone_no, designation, supervisor_id):
	sql = "UPDATE employee SET emp_name = %s, store_id = %s, doj = %s, phone_no = %s, designation = %s, supervisor_id = %s WHERE emp_id = %s"
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
def getPlant(id, field):
	sql = "SELECT * FROM plant WHERE id = %s"
	try:
		cursor.execute(sql, (id,))
		result = cursor.fetchone()
		switch={
		"name": result[1],
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
		cursor.execute(sql, (type_id,))
		result = cursor.fetchone()
		switch={
		"type_name": result[1],
		"description": result[2]
		}
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def getStore(store_id, field):
	sql = "SELECT * FROM store WHERE store_id = %s"
	try:
		cursor.execute(sql, (store_id,))
		result = cursor.fetchone()
		switch={
		"number_of_lots": result[1],
		"phone_no": result[2],
		"address": result[3]
		}
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def getCustomer(cust_id, field):
	sql = "SELECT * FROM customer WHERE cust_id = %s"
	try:
		cursor.execute(sql, (cust_id,))
		result = cursor.fetchone()
		switch={
		"cust_name": result[1],
		"phone_no": result[2],
		"address": result[3],
		"email_id": result[4]
		}
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def getOrders(order_id, field):
	sql = "SELECT * FROM orders WHERE order_id = %s"
	try:
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
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def getOrderItem(item_id, field):
	sql = "SELECT * FROM order_item WHERE item_id = %s"
	try:
		cursor.execute(sql, (item_id,))
		result = cursor.fetchone()
		switch={
		"order_id": result[1],
		"plant_id": result[2],
		"price": result[3],
		"rating": result[4]
		}
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def getEmployee(emp_id, field):
	sql = "SELECT * FROM employee WHERE emp_id = %s"
	try:
		cursor.execute(sql, (emp_id,))
		result = cursor.fetchone()
		switch={
		"emp_name": result[1],
		"store_id": result[2],
		"doj": result[3],
		"phone_no": result[4],
		"designation": result[5],
		"supervisor_id": result[6]
		}
		return switch.get(field, "NOT FOUND")
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

def plantTypes():
	sql = "SELECT * FROM plant_type"
	try:
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			print(row)
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def stores():
	sql = "SELECT * FROM store"
	try:
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			print(row)
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def customers():
	sql = "SELECT * FROM customer"
	try:
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			print(row)
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def orders():
	sql = "SELECT * FROM orders"
	try:
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			print(row)
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def orderItems():
	sql = "SELECT * FROM order_item"
	try:
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			print(row)
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def employees():
	sql = "SELECT * FROM employee"
	try:
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			print(row)
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def startup():
		#PLANTS
	plantName = "queenPalm"
	plantPrice = 25.50
	plantDescription = "YAASSS QUEEEN!!"
	plantAge = 21

	#PLANT TYPES
	plantTypeName = "tree"
	plantTypeDescription = "tall plant"

	#STORE
	storeLots = 50
	storePhoneNo = "0123456789"
	storeAddress = "2341 Redneck Dr."

	#CUSTOMER
	customerName = "jeff"
	customerPhoneNo = "0123456789"
	customerAddress = "1234 Robin Wy."
	customerEmail = "jeff@gmail.com"
	
	#ORDERS
	OrderStoreId = 1
	OrderCustId = 1
	OrderType = "single"
	OrderPaymentStatus = "Paid"
	OrderPrice = 120.99
	OrderDeliveryAddress = "5738 Applegate Ave."

	#ORDER_ITEM
	OrderID = 1
	OrderPlantID = 1
	OrderItemPrice = 123.67
	OrderRating = 4.5

	#EMPLOYEE
	EmployeeName = "Bee"
	EmployeeStoreId = 1
	EmployeeDOJ = "2000-01-25"
	EmployeePhoneNo = "0123456789"
	EmployeeDesignation = "Worker"
	#EmployeeSupervisor = 4

	insert_plant(plantName, plantPrice, plantDescription, plantAge)
	insert_plant_type(plantTypeName, plantTypeDescription)
	insert_store(storeLots, storePhoneNo, storeAddress)
	insert_customer(customerName, customerPhoneNo, customerAddress, customerEmail)
	insert_orders(OrderStoreId, OrderCustId, OrderType, OrderPaymentStatus, OrderPrice, OrderDeliveryAddress)
	insert_order_item(OrderID, OrderPlantID, OrderItemPrice, OrderRating)
	insert_employee(EmployeeName, EmployeeStoreId, EmployeeDOJ, EmployeePhoneNo, EmployeeDesignation, EmployeeSupervisor)

#---------------------------------------------------------------------------------TEST SCRIPTS--------------------------------------------------------
def main():
	startup()
	print("-----------------PLANT TABLE-----------------")
	print("Plant name is: " + getPlant(1, "name"))
	print("Plant price is: " + str(getPlant(1, "price")))
	print("Plant description is: " + getPlant(1, "description"))
	print("Plant age is: " + str(getPlant(1, "age")))
	print("------------------PLANT TYPE------------------")
	print("PlantType name is: " + getPlantType(1, "type_name"))
	print("PlantType description is: " + getPlantType(1, "description"))
	print("------------------STORE---------------------------")
	print("Store Number of Lots is: " + str(getStore(1, "number_of_lots")))
	print("Store Phone Number is: " + getStore(1, "phone_no"))
	print("Store Address is: " + getStore(1, "address"))
	print("------------------CUSTOMER---------------------------")
	print("Customer Name is: " + getCustomer(1, "cust_name"))
	print("Customer Phone Number is: " + getCustomer(1, "phone_no"))
	print("Customer Address is: " + getCustomer(1, "address"))
	print("Customer Email is: " + getCustomer(1, "email_id"))
	print("-------------------------ORDERS-------------------------")
	print("Orders StoreId is: " + str(getOrders(1, "store_id")))
	print("Orders CustomerId is: " + str(getOrders(1, "cust_id")))
	print("Orders Order Type is: " + getOrders(1, "order_type"))
	print("Orders Payment Status is: " + getOrders(1, "payment_status"))
	print("Orders Price is: " + str(getOrders(1, "price")))
	print("Orders Delivery Address is: " + getOrders(1, "delivery_address"))
	print("-------------------------ORDER ITEM-------------------------")
	print("OrderItem OrderId is: " + str(getOrderItem(1, "order_id")))
	print("OrderItem PlantId is: " + str(getOrderItem(1, "plant_id")))
	print("OrderItem Price is: " + str(getOrderItem(1, "price")))
	print("OrderItem Rating is: " + str(getOrderItem(1, "rating"))	)
	print("-------------------------EMPLOYEE-------------------------")	
	print("Employee Name is: " + getEmployee(1, "emp_name"))
	print("Employee Store Id is: " + str(getEmployee(1, "store_id")))
	print("Employee DOJ is: " + str(getEmployee(1, "doj")))
	print("Employee Phone Number is: " + getEmployee(1, "phone_no"))
	print("Employee Designation is: " + getEmployee(1, "designation"))
	print("Employee Supervisor Id is: " + str(getEmployee(1, "supervisor_id")))


	update_plant(1, "King Plam", 47, "Royal Palm", 24)
	update_plant_type(1, "StillTree",  "TallTree")
	update_store(1, 49, "9876543210", "3241 Bobcat St.")
	update_customer(1, "Bob", "9876543210", "4321 Batman Cv", "Bob@yahoo.com")
	update_orders(1,1,1, "double", "Payment Due", 666.21, "57312 treeapple Wy.")
	update_order_item(1,1,1, 432, 6.7)
	update_employee(1, "Lebron James", 1, "2020-01-26", "9876543210", "KingJames", 7)

	print("------------------------------------AFTER UPDATE----------------------------------------------------")
	print("-----------------PLANT TABLE-----------------")
	plants()
	print("Plant name is: " + getPlant(1, "name"))
	print("Plant price is: " + str(getPlant(1, "price")))
	print("Plant description is: " + getPlant(1, "description"))
	print("Plant age is: " + str(getPlant(1, "age")))
	print("------------------PLANT TYPE------------------")
	plantTypes()
	print("PlantType name is: " + getPlantType(1, "type_name"))
	print("PlantType description is: " + getPlantType(1, "description"))
	print("------------------STORE---------------------------")
	print("Store Number of Lots is: " + str(getStore(1, "number_of_lots")))
	print("Store Phone Number is: " + getStore(1, "phone_no"))
	print("Store Address is: " + getStore(1, "address"))
	print("------------------CUSTOMER---------------------------")
	print("Customer Name is: " + getCustomer(1, "cust_name"))
	print("Customer Phone Number is: " + getCustomer(1, "phone_no"))
	print("Customer Address is: " + getCustomer(1, "address"))
	print("Customer Email is: " + getCustomer(1, "email_id"))
	print("-------------------------ORDERS-------------------------")
	print("Orders StoreId is: " + str(getOrders(1, "store_id")))
	print("Orders CustomerId is: " + str(getOrders(1, "cust_id")))
	print("Orders Order Type is: " + getOrders(1, "order_type"))
	print("Orders Payment Status is: " + getOrders(1, "payment_status"))
	print("Orders Price is: " + str(getOrders(1, "price")))
	print("Orders Delivery Address is: " + getOrders(1, "delivery_address"))
	print("-------------------------ORDER ITEM-------------------------")
	print("OrderItem OrderId is: " + str(getOrderItem(1, "order_id")))
	print("OrderItem PlantId is: " + str(getOrderItem(1, "plant_id")))
	print("OrderItem Price is: " + str(getOrderItem(1, "price")))
	print("OrderItem Rating is: " + str(getOrderItem(1, "rating"))	)
	print("-------------------------EMPLOYEE-------------------------")	
	print("Employee Name is: " + getEmployee(1, "emp_name"))
	print("Employee Store Id is: " + str(getEmployee(1, "store_id")))
	print("Employee DOJ is: " + str(getEmployee(1, "doj")))
	print("Employee Phone Number is: " + getEmployee(1, "phone_no"))
	print("Employee Designation is: " + getEmployee(1, "designation"))
	print("Employee Supervisor Id is: " + str(getEmployee(1, "supervisor_id")))

	delete_plant(1)
	delete_plant_type(1)
	delete_store(1)
	delete_store(1)
	delete_customer(1)
	delete_orders(1)
	delete_order_item(1)
	delete_employee(1)


	print("------------------------------------AFTER DELETE----------------------------------------------------")
	print("-----------------PLANT TABLE-----------------")
	plants()
	print("------------------PLANT TYPE------------------")
	plantTypes()
	print("------------------STORE---------------------------")
	stores()
	print("------------------CUSTOMER---------------------------")
	customers()
	print("-------------------------ORDERS-------------------------")
	orders()
	print("-------------------------ORDER ITEM-------------------------")
	orderItems()
	print("-------------------------EMPLOYEE-------------------------")	
	employees()

main()
=======
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
	sql = "INSERT INTO plant_type(type_name, description) VALUES(%s,%s)"
	cursor.execute(sql, (name, description))
	mydb.commit()

def insert_store(number_of_lots, phone_no, address):
	sql = "INSERT INTO store(number_of_lots, phone_no, address) VALUES(%s,%s,%s)"
	data = (number_of_lots, phone_no, address)
	cursor.execute(sql, data)
	mydb.commit()

def insert_customer(cust_name, phone_no, address, email_id):
	sql = "INSERT INTO customer(cust_name, phone_no, address, email_id) VALUES(%s,%s,%s,%s)"
	data = (cust_name, phone_no, address, email_id)
	cursor.execute(sql, data)
	mydb.commit()

def insert_orders(store_id, cust_id, order_type, payment_status, price, delivery_address):
	sql = "INSERT INTO orders(store_id, cust_id, order_type, payment_status, price, delivery_address) VALUES(%s, %s, %s, %s, %s, %s)"
	data = (store_id, cust_id, order_type, payment_status, price, delivery_address)
	cursor.execute(sql, data)
	mydb.commit()

def insert_order_item(order_id, plant_id, price, rating):
	sql = "INSERT INTO order_item(order_id, plant_id,  price, rating) VALUES(%s,%s,%s,%s)"
	data = (order_id, plant_id,  price, rating)
	cursor.execute(sql, data)
	mydb.commit()

def insert_employee(emp_name, store_id, doj, phone_no, designation, supervisor_id):
	sql = "INSERT INTO employee(emp_name, store_id, doj, phone_no, designation, supervisor_id) VALUES(%s,%s,%s,%s,%s,%s)"
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
	sql = "UPDATE store SET number_of_lots = %s, phone_no = %s, address = %s WHERE store_id = %s"
	data = (number_of_lots, phone_no, address, store_id)
	cursor.execute(sql, data)
	mydb.commit()

def update_customer(cust_id, cust_name, phone_no, address, email_id):
	sql = "UPDATE customer SET cust_name = %s, phone_no = %s, address = %s, email_id = %s WHERE cust_id = %s"
	data = (cust_name, phone_no, address, email_id, cust_id)
	cursor.execute(sql, data)
	mydb.commit()

def update_orders(order_id, store_id, cust_id, order_type, payment_status, price, delivery_address):
	sql = "UPDATE orders SET store_id = %s, cust_id = %s, order_type = %s, payment_status = %s, price = %s, delivery_address = %s WHERE order_id = %s"
	data = (store_id, cust_id, order_type, payment_status, price, delivery_address, order_id)
	cursor.execute(sql, data)
	mydb.commit()

def update_order_item(item_id, order_id,  plant_id, price, rating,):
	sql = "UPDATE order_item SET order_id = %s, plant_id = %s, price = %s, rating = %s WHERE item_id = %s "
	data = (order_id, plant_id,price, rating,  item_id)
	cursor.execute(sql, data)
	mydb.commit()

def update_employee(emp_id, emp_name, store_id, doj, phone_no, designation, supervisor_id):
	sql = "UPDATE employee SET emp_name = %s, store_id = %s, doj = %s, phone_no = %s, designation = %s, supervisor_id = %s WHERE emp_id = %s"
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
def getPlant(id, field):
	sql = "SELECT * FROM plant WHERE id = %s"
	try:
		cursor.execute(sql, (id,))
		result = cursor.fetchone()
		switch={
		"name": result[1],
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
		cursor.execute(sql, (type_id,))
		result = cursor.fetchone()
		switch={
		"type_name": result[1],
		"description": result[2]
		}
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def getStore(store_id, field):
	sql = "SELECT * FROM store WHERE store_id = %s"
	try:
		cursor.execute(sql, (store_id,))
		result = cursor.fetchone()
		switch={
		"number_of_lots": result[1],
		"phone_no": result[2],
		"address": result[3]
		}
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def getCustomer(cust_id, field):
	sql = "SELECT * FROM customer WHERE cust_id = %s"
	try:
		cursor.execute(sql, (cust_id,))
		result = cursor.fetchone()
		switch={
		"cust_name": result[1],
		"phone_no": result[2],
		"address": result[3],
		"email_id": result[4]
		}
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def getOrders(order_id, field):
	sql = "SELECT * FROM orders WHERE order_id = %s"
	try:
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
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def getOrderItem(item_id, field):
	sql = "SELECT * FROM order_item WHERE item_id = %s"
	try:
		cursor.execute(sql, (item_id,))
		result = cursor.fetchone()
		switch={
		"order_id": result[1],
		"plant_id": result[2],
		"price": result[3],
		"rating": result[4]
		}
		return switch.get(field, "NOT FOUND")
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def getEmployee(emp_id, field):
	sql = "SELECT * FROM employee WHERE emp_id = %s"
	try:
		cursor.execute(sql, (emp_id,))
		result = cursor.fetchone()
		switch={
		"emp_name": result[1],
		"store_id": result[2],
		"doj": result[3],
		"phone_no": result[4],
		"designation": result[5],
		"supervisor_id": result[6]
		}
		return switch.get(field, "NOT FOUND")
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

def plantTypes():
	sql = "SELECT * FROM plant_type"
	try:
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			print(row)
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def stores():
	sql = "SELECT * FROM store"
	try:
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			print(row)
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def customers():
	sql = "SELECT * FROM customer"
	try:
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			print(row)
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def orders():
	sql = "SELECT * FROM orders"
	try:
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			print(row)
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def orderItems():
	sql = "SELECT * FROM order_item"
	try:
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			print(row)
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def employees():
	sql = "SELECT * FROM employee"
	try:
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			print(row)
	except mysql.connector.Error as err:
		print("MYSQL ERROR: {}".format(err))

def startup():
		#PLANTS
	plantName = "queenPalm"
	plantPrice = 25.50
	plantDescription = "YAASSS QUEEEN!!"
	plantAge = 21

	#PLANT TYPES
	plantTypeName = "tree"
	plantTypeDescription = "tall plant"

	#STORE
	storeLots = 50
	storePhoneNo = "0123456789"
	storeAddress = "2341 Redneck Dr."

	#CUSTOMER
	customerName = "jeff"
	customerPhoneNo = "0123456789"
	customerAddress = "1234 Robin Wy."
	customerEmail = "jeff@gmail.com"
	
	#ORDERS
	OrderStoreId = 1
	OrderCustId = 1
	OrderType = "single"
	OrderPaymentStatus = "Paid"
	OrderPrice = 120.99
	OrderDeliveryAddress = "5738 Applegate Ave."

	#ORDER_ITEM
	OrderID = 1
	OrderPlantID = 1
	OrderItemPrice = 123.67
	OrderRating = 4.5

	#EMPLOYEE
	EmployeeName = "Bee"
	EmployeeStoreId = 1
	EmployeeDOJ = "2000-01-25"
	EmployeePhoneNo = "0123456789"
	EmployeeDesignation = "Worker"
	EmployeeSupervisor = 4

	insert_plant(plantName, plantPrice, plantDescription, plantAge)
	insert_plant_type(plantTypeName, plantTypeDescription)
	insert_store(storeLots, storePhoneNo, storeAddress)
	insert_customer(customerName, customerPhoneNo, customerAddress, customerEmail)
	insert_orders(OrderStoreId, OrderCustId, OrderType, OrderPaymentStatus, OrderPrice, OrderDeliveryAddress)
	insert_order_item(OrderID, OrderPlantID, OrderItemPrice, OrderRating)
	insert_employee(EmployeeName, EmployeeStoreId, EmployeeDOJ, EmployeePhoneNo, EmployeeDesignation, EmployeeSupervisor)

#---------------------------------------------------------------------------------TEST SCRIPTS--------------------------------------------------------
def main():
	startup()
	print("-----------------PLANT TABLE-----------------")
	print("Plant name is: " + getPlant(1, "name"))
	print("Plant price is: " + str(getPlant(1, "price")))
	print("Plant description is: " + getPlant(1, "description"))
	print("Plant age is: " + str(getPlant(1, "age")))
	print("------------------PLANT TYPE------------------")
	print("PlantType name is: " + getPlantType(1, "type_name"))
	print("PlantType description is: " + getPlantType(1, "description"))
	print("------------------STORE---------------------------")
	print("Store Number of Lots is: " + str(getStore(1, "number_of_lots")))
	print("Store Phone Number is: " + getStore(1, "phone_no"))
	print("Store Address is: " + getStore(1, "address"))
	print("------------------CUSTOMER---------------------------")
	print("Customer Name is: " + getCustomer(1, "cust_name"))
	print("Customer Phone Number is: " + getCustomer(1, "phone_no"))
	print("Customer Address is: " + getCustomer(1, "address"))
	print("Customer Email is: " + getCustomer(1, "email_id"))
	print("-------------------------ORDERS-------------------------")
	print("Orders StoreId is: " + str(getOrders(1, "store_id")))
	print("Orders CustomerId is: " + str(getOrders(1, "cust_id")))
	print("Orders Order Type is: " + getOrders(1, "order_type"))
	print("Orders Payment Status is: " + getOrders(1, "payment_status"))
	print("Orders Price is: " + str(getOrders(1, "price")))
	print("Orders Delivery Address is: " + getOrders(1, "delivery_address"))
	print("-------------------------ORDER ITEM-------------------------")
	print("OrderItem OrderId is: " + str(getOrderItem(1, "order_id")))
	print("OrderItem PlantId is: " + str(getOrderItem(1, "plant_id")))
	print("OrderItem Price is: " + str(getOrderItem(1, "price")))
	print("OrderItem Rating is: " + str(getOrderItem(1, "rating"))	)
	print("-------------------------EMPLOYEE-------------------------")	
	print("Employee Name is: " + getEmployee(1, "emp_name"))
	print("Employee Store Id is: " + str(getEmployee(1, "store_id")))
	print("Employee DOJ is: " + str(getEmployee(1, "doj")))
	print("Employee Phone Number is: " + getEmployee(1, "phone_no"))
	print("Employee Designation is: " + getEmployee(1, "designation"))
	print("Employee Supervisor Id is: " + str(getEmployee(1, "supervisor_id")))


	update_plant(1, "King Plam", 47, "Royal Palm", 24)
	update_plant_type(1, "StillTree",  "TallTree")
	update_store(1, 49, "9876543210", "3241 Bobcat St.")
	update_customer(1, "Bob", "9876543210", "4321 Batman Cv", "Bob@yahoo.com")
	update_orders(1,1,1, "double", "Payment Due", 666.21, "57312 treeapple Wy.")
	update_order_item(1,1,1, 432, 6.7)
	update_employee(1, "Lebron James", 1, "2020-01-26", "9876543210", "KingJames", 7)

	print("------------------------------------AFTER UPDATE----------------------------------------------------")
	print("-----------------PLANT TABLE-----------------")
	plants()
	print("Plant name is: " + getPlant(1, "name"))
	print("Plant price is: " + str(getPlant(1, "price")))
	print("Plant description is: " + getPlant(1, "description"))
	print("Plant age is: " + str(getPlant(1, "age")))
	print("------------------PLANT TYPE------------------")
	plantTypes()
	print("PlantType name is: " + getPlantType(1, "type_name"))
	print("PlantType description is: " + getPlantType(1, "description"))
	print("------------------STORE---------------------------")
	print("Store Number of Lots is: " + str(getStore(1, "number_of_lots")))
	print("Store Phone Number is: " + getStore(1, "phone_no"))
	print("Store Address is: " + getStore(1, "address"))
	print("------------------CUSTOMER---------------------------")
	print("Customer Name is: " + getCustomer(1, "cust_name"))
	print("Customer Phone Number is: " + getCustomer(1, "phone_no"))
	print("Customer Address is: " + getCustomer(1, "address"))
	print("Customer Email is: " + getCustomer(1, "email_id"))
	print("-------------------------ORDERS-------------------------")
	print("Orders StoreId is: " + str(getOrders(1, "store_id")))
	print("Orders CustomerId is: " + str(getOrders(1, "cust_id")))
	print("Orders Order Type is: " + getOrders(1, "order_type"))
	print("Orders Payment Status is: " + getOrders(1, "payment_status"))
	print("Orders Price is: " + str(getOrders(1, "price")))
	print("Orders Delivery Address is: " + getOrders(1, "delivery_address"))
	print("-------------------------ORDER ITEM-------------------------")
	print("OrderItem OrderId is: " + str(getOrderItem(1, "order_id")))
	print("OrderItem PlantId is: " + str(getOrderItem(1, "plant_id")))
	print("OrderItem Price is: " + str(getOrderItem(1, "price")))
	print("OrderItem Rating is: " + str(getOrderItem(1, "rating"))	)
	print("-------------------------EMPLOYEE-------------------------")	
	print("Employee Name is: " + getEmployee(1, "emp_name"))
	print("Employee Store Id is: " + str(getEmployee(1, "store_id")))
	print("Employee DOJ is: " + str(getEmployee(1, "doj")))
	print("Employee Phone Number is: " + getEmployee(1, "phone_no"))
	print("Employee Designation is: " + getEmployee(1, "designation"))
	print("Employee Supervisor Id is: " + str(getEmployee(1, "supervisor_id")))

	delete_plant(1)
	delete_plant_type(1)
	delete_store(1)
	delete_store(1)
	delete_customer(1)
	delete_orders(1)
	delete_order_item(1)
	delete_employee(1)


	print("------------------------------------AFTER DELETE----------------------------------------------------")
	print("-----------------PLANT TABLE-----------------")
	plants()
	print("------------------PLANT TYPE------------------")
	plantTypes()
	print("------------------STORE---------------------------")
	stores()
	print("------------------CUSTOMER---------------------------")
	customers()
	print("-------------------------ORDERS-------------------------")
	orders()
	print("-------------------------ORDER ITEM-------------------------")
	orderItems()
	print("-------------------------EMPLOYEE-------------------------")	
	employees()

main()
>>>>>>> Jasper
