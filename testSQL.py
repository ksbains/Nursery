#---------------------------------------------------------------------------------TEST SCRIPTS--------------------------------------------------------
def main():
	# startup()
	print("------------------STORE---------------------------")
	print("Store Number of Lots is: " + str(getStore(1, "number_of_lots")))
	print("Store Phone Number is: " + getStore(1, "phone_no"))
	print("Store Address is: " + getStore(1, "address"))

	print("-----------------------LOT---------------------------")
	print("Lot StoreId is: " + str(getLot(1, "store_id")))
	
	print("-----------------PLANT TABLE-----------------")
	print("Plant name is: " + getPlant(1, "name"))
	print("Plant price is: " + str(getPlant(1, "price")))
	print("Plant description is: " + getPlant(1, "description"))
	print("Plant age is: " + str(getPlant(1, "age")))
	
	print("------------------PLANT TYPE------------------")
	print("PlantType name is: " + getPlantType(1, "type_name"))
	print("PlantType description is: " + getPlantType(1, "description"))
	
	print("------------------CUSTOMER---------------------------")
	print("Customer Name is: " + getCustomer(1, "cust_name"))
	print("Customer UserName is: " + getCustomer(1, "cust_username"))
	print("Customer Password is: " + getCustomer(1, "cust_password"))
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
	print("Employee UserName is: " + getEmployee(1, "emp_username"))
	print("Employee Password is: " + getEmployee(1, "emp_password"))
	print("Employee Store Id is: " + str(getEmployee(1, "store_id")))
	print("Employee DOJ is: " + str(getEmployee(1, "doj")))
	print("Employee Phone Number is: " + getEmployee(1, "phone_no"))
	print("Employee Designation is: " + getEmployee(1, "designation"))
	print("Employee Supervisor Id is: " + str(getEmployee(1, "supervisor_id")))

	# -----------------------------------------------UPDATE--------------------------------------------------------
	
	update_store(1, 49, "9876543210", "3241 Bobcat St.")
	update_lot(1, 1)
	update_plant(1, "King Plam", 47, "Royal Palm", 24)
	update_plant_type(1, "StillTree",  "TallTree")

	update_customer(1, "Bob", "Bobdat", "pass", "9876543210", "4321 Batman Cv", "Bob@yahoo.com")
	update_orders(1,1,1, "double", "Payment Due", 666.21, "57312 treeapple Wy.")
	update_order_item(1,1,1, 432, 6.7)
	update_employee(1, "Lebron James","KingLBJ", "bronny", 1, "2020-01-26", "9876543210", "KingJames", 7)

	#------------------------------------AFTER UPDATE----------------------------------------------------

	print("------------------------------------AFTER UPDATE----------------------------------------------------")
	
	print("------------------STORE---------------------------")
	print("Store Number of Lots is: " + str(getStore(1, "number_of_lots")))
	print("Store Phone Number is: " + getStore(1, "phone_no"))
	print("Store Address is: " + getStore(1, "address"))

	print("-----------------------LOT---------------------------")
	print("Lot StoreId is: " + str(getLot(1, "store_id")))

	print("-----------------PLANT TABLE-----------------")
	print("Plant name is: " + getPlant(1, "name"))
	print("Plant price is: " + str(getPlant(1, "price")))
	print("Plant description is: " + getPlant(1, "description"))
	print("Plant age is: " + str(getPlant(1, "age")))

	print("------------------PLANT TYPE------------------")
	print("PlantType name is: " + getPlantType(1, "type_name"))
	print("PlantType description is: " + getPlantType(1, "description"))

	print("------------------CUSTOMER---------------------------")
	print("Customer Name is: " + getCustomer(1, "cust_name"))
	print("Customer UserName is: " + getCustomer(1, "cust_username"))
	print("Customer Password is: " + getCustomer(1, "cust_password"))
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
	print("Employee UserName is: " + getEmployee(1, "emp_username"))
	print("Employee Password is: " + getEmployee(1, "emp_password"))
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
	
	print("------------------STORE---------------------------")
	stores()

	print("------------------LOT---------------------------")
	lots()

	print("-----------------PLANT TABLE-----------------")
	plants()
	
	print("------------------PLANT TYPE------------------")
	plantTypes()

	print("------------------CUSTOMER---------------------------")
	customers()
	
	print("-------------------------ORDERS-------------------------")
	orders()
	
	print("-------------------------ORDER ITEM-------------------------")
	orderItems()
	
	print("-------------------------EMPLOYEE-------------------------")	
	employees()