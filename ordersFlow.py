import mysql.connector
import inquirer
from prettytable import PrettyTable


def getConnection():	
	conn = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="password",
		database="nursery"
	)
	#cursor = conn.cursor()
	return conn

#---------------------------- Utility methods ---------------------------------------------

#process order into json format
def processOrderResult(orderResult):
	ordersDict = []
	for row in orderResult:
			record={
				'order_id' : row[0],
				'store_id' : row[1],
				'cust_id' : row[2],
				'order_type' : row[4],
				'order_date' : row[3],
				'order_status' : row[5],
				'payment_status' : row[6],
				'price' : row[7],
				'expected_delivery' : row[8],
				'delivered_on' : row[9],				
				'address' : row[10]
			}
			ordersDict.append(record)
	return ordersDict


#process order items into json format
def processItemResult(itemResult):
	itemDict = []
	for row in itemResult:
			record={
				'item_id' : row[0],
				'name' : row[1],
				'type_name' : row[2],				
				'quantity' : row[3],
				'price' : row[4],
				'rating' : row[5]
			}
			itemDict.append(record)
	return itemDict

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[32m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))

#--------------------------------- SQL Queries ------------------------------------------------------

#Get all orders
def getAllOrders():
	sql = "SELECT * FROM orders"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql)
		orders = cursor.fetchall()
		ordersDict = processOrderResult(orders)
		cursor.close()
		conn.close()
		return ordersDict
	except mysql.connector.Error as err:
		prRed("Error fetching orders for employee!")
		prRed("MYSQL ERROR: {}".format(err))
		print("\n")


def getOrder(orderId):
	sql = "SELECT * FROM orders WHERE order_id = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (orderId,))
		orderDetails = cursor.fetchone()
		cursor.close()
		conn.close()
		return orderDetails
	except mysql.connector.Error as err:
		prRed("Error fetching order for id")
		prRed("MYSQL ERROR: {}".format(err))
		print("\n")


#update order by employee to delivered
def updateDeliveredOrder(orderId, status, date):
	sql = "UPDATE orders SET order_status = %s, delivered_on = %s WHERE order_id = %s"
	parameters = (status, date, orderId)
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, parameters)
		conn.commit()
		cursor.close()
		conn.close()
	except mysql.connector.Error as err:
		prRed("Error updating order status and delivered on date!")
		prRed("MYSQL ERROR: {}".format(err))
		print("\n")


#update order by employee to delivered
def updateCurrentOrder(orderId, status, date):
	sql = "UPDATE orders SET order_status = %s, expected_delivery_date = %s WHERE order_id = %s"
	parameters = (status, date, orderId)
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, parameters)
		conn.commit()
		cursor.close()
		conn.close()
	except mysql.connector.Error as err:
		prRed("Error updating order status and expected date!")
		prRed("MYSQL ERROR: {}".format(err))
		print("\n")


#Get orders for given customer id
def getOrderForGivenCust(cust_id):
	sql = "SELECT * FROM orders WHERE cust_id = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (cust_id,))
		result = cursor.fetchall()		
		ordersDict = processOrderResult(result)
		cursor.close()
		conn.close()
		return ordersDict
	except mysql.connector.Error as err:
		prRed("Error fetching orders for customer!")
		prRed("MYSQL ERROR: {}".format(err))
		print("\n")


#Get orders for given customer id and order status
def getOrderForGivenCustAndStatus(cust_id, orderStatus):
	sql = "SELECT * FROM orders WHERE cust_id = %s AND order_status = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		parameters = (cust_id, orderStatus)
		cursor.execute(sql, parameters)
		result = cursor.fetchall()
		ordersDict = processOrderResult(result)
		cursor.close()
		conn.close()
		return ordersDict
	except mysql.connector.Error as err:
		prRed("Error fetching orders for customer with given order status!")
		prRed("MYSQL ERROR: {}".format(err))
		print("\n")


#Order item menu for given order id and customer
def getItemsForGivenOrderId(order_id):
	sql = '''SELECT i.item_id, p.name, t.type_name, i.quantity, i.price, i.rating
			FROM order_item i JOIN plant p ON p.plant_id = i.plant_id 
			JOIN plant_type t ON t.type_id = p.p_type_id
			WHERE i.order_id = %s'''
	try:
		conn = getConnection()
		cursor = conn.cursor()
		parameters = (order_id,)
		cursor.execute(sql, parameters)
		result = cursor.fetchall()	
		cursor.close()
		conn.close()
		return result
	except mysql.connector.Error as err:
		prRed("Error fetching order items for customer of given order id!")
		prRed("MYSQL ERROR: {}".format(err))
		print("\n")


#Update rating for given order item
def updateItemRating(itemId, rating):
	sql = "UPDATE order_item SET rating = %s WHERE item_id = %s"
	try:
		conn = getConnection()
		cursor = conn.cursor()
		parameters = (rating, itemId)
		cursor.execute(sql, parameters)
		conn.commit()
		cursor.close()
		conn.close()
	except mysql.connector.Error as err:
		prRed("Error updating order item rating!")
		prRed("MYSQL ERROR: {}".format(err))
		print("\n")

# ------------------------------------------ Printing methods ---------------------------------------------

#Print orders given customer id
def printOrderForCust(ordersDict):
	order_table = PrettyTable(['Order Id', 'Order Date', 'Store Id', 'Order Type', 'Order Status', 'Payment Status', 'Price', 'Expected Delivery Date', 'Delivered On', 'Delivery Address'])
	for x in ordersDict:
		order_table.add_row([x["order_id"], x["order_date"], x["store_id"], x["order_type"], x["order_status"], x["payment_status"], x["price"], x["expected_delivery"], x["delivered_on"], x["address"]])		
	print(order_table)
	print("\n")


#Print orders of given status and customer id
def printOrderForCustGivenStatus(ordersDict, orderStatus):
	if orderStatus == 'Current' or orderStatus == 'Dispatched' or orderStatus == 'New':
		order_table = PrettyTable(['Order Id', 'Order Date', 'Store Id', 'Order Type', 'Payment Status', 'Price', 'Expected Delivery Date', 'Delivery Address'])
		for x in ordersDict:
			order_table.add_row([x["order_id"], x["order_date"], x["store_id"], x["order_type"], x["payment_status"], x["price"], x["expected_delivery"], x["address"]])		
		print(order_table)
		print("\n")
	elif orderStatus == 'Completed':
		order_table = PrettyTable(['Order Id', 'Order Date', 'Store Id', 'Order Type', 'Payment Status', 'Price', 'Delivered On', 'Delivery Address'])
		for x in ordersDict:
			order_table.add_row([x["order_id"], x["order_date"], x["store_id"], x["order_type"], x["payment_status"], x["price"], x["delivered_on"], x["address"]])		
		print(order_table)
		print("\n")


#Print orders of given status and customer id
def printItems(itemDict):
	item_table = PrettyTable(['Item Id', 'Plant Name', 'Plant Type', 'Quantity', 'Price', 'Rating'])	
	for x in itemDict:
		item_table.add_row([x["item_id"], x["name"], x["type_name"], x["quantity"], x["price"], x["rating"]])
	print(item_table)
	print("\n")


#print all orders
def printAllOrders(orders):
	order_table = PrettyTable(['Order Id', 'Order Date', 'Customer Id', 'Store Id', 'Order Type', 'Order Status', 'Payment Status', 'Price','Expected Delivery Date', 'Delivered On', 'Delivery Address'])
	for x in orders:
		order_table.add_row([x["order_id"], x["order_date"], x["cust_id"], x["store_id"], x["order_type"], x["order_status"], x["payment_status"], x["price"], x["expected_delivery"], x["delivered_on"], x["address"]])		
	print(order_table)
	print("\n")
		  



########################################## Customer menu flow #################################################################

#show order menu for customer id
def showCustOrderMenu(custId):
	showOrderStatusMenu(custId)
	

#Orders menu by status for customer
def showOrderStatusMenu(custId):
	questions = [
		inquirer.List(
			'orderstatus',
			message ='Choose orders to be viewed',
			choices = ['New', 'Current', 'Completed', 'All', 'Back'],
			default= 'All')
	]
	answers = inquirer.prompt(questions)
	orderStatus = answers.get("orderstatus")	
	if orderStatus == 'Current'or orderStatus == 'Completed' or orderStatus == 'New':
		orders = getOrderForGivenCustAndStatus(custId, orderStatus)
		if len(orders) == 0:
			prYellow("You have no orders!\n")
			showOrderStatusMenu(custId)
		else:
			printOrderForCustGivenStatus(orders, orderStatus)
			showOrderIdMenu(orders, custId)
	elif orderStatus == 'All':
		orders = getOrderForGivenCust(custId)
		if len(orders) == 0:
			prYellow("You have no orders!\n")
			showOrderStatusMenu(custId)
		else:
			printOrderForCust(orders)
			showOrderIdMenu(orders, custId)
		
    
#Orders by id for customer
def showOrderIdMenu(orders, custId):
	aOrderIds = []
	for x in orders:
		aOrderIds.append(x["order_id"])
	aOrderIds.append('Back')
	questions = [
		inquirer.List(
			'orderId',
			message = 'Which order do you want to view?',
			choices = aOrderIds,
			default = aOrderIds[0]
			)
	]
	answers = inquirer.prompt(questions)
	orderIdAnswer = answers.get('orderId')
	if orderIdAnswer != 'Back':
		items = getItemsForGivenOrderId(orderIdAnswer)
		items = processItemResult(items)
		printItems(items)
		showItemsMenu(items, orders, custId)
	else:
		showOrderStatusMenu(custId)


#Show items menu chosen from order items
def showItemsMenu(items, orders, custId):
	aItemsId = []
	for x in items:
		aItemsId.append(x["item_id"])
	aItemsId.append('Back')
	questions = [
		inquirer.List(
			'itemId',
			message = 'Choose the item you want to give feedback',
			choices = aItemsId,
			default = aItemsId[0]
			)
	]
	answers = inquirer.prompt(questions)
	itemIdAnswer = answers.get('itemId')
	if itemIdAnswer == 'Back':
		printOrderForCust(orders)
		showOrderIdMenu(orders, custId)
	else:
		questions = [
			inquirer.List(
				'rating',
				message = 'Choose a rating from 0 - 5',
				choices = [0, 1, 2, 3, 4, 5],
				default = 5
				)
		]
		answers = inquirer.prompt(questions)
		updateItemRating(itemIdAnswer, answers.get('rating'))
		showItemsMenu(items, orders, custId)
		

#----------------------------------------------- Employee main menu -------------------------------------

def showEmployeeOrders():
	question = [
		inquirer.List(
			'option',
			message='Do you want to view or update an order?',
			choices=['View', 'Update', 'Back']
			)
	]
	answer = inquirer.prompt(question)
	ans = answer.get('option')

	orders = getAllOrders()
	printAllOrders(orders)

	if ans == 'Update':
		aOrderIds = []
		for x in orders:
			aOrderIds.append(x["order_id"])
		aOrderIds.append('Back')
		questions = [
			inquirer.List(
				'orderId',
				message = 'Which order do you want to update?',
				choices = aOrderIds
				)
		]
		answers = inquirer.prompt(questions)
		orderIdAnswer = answers.get('orderId')
		updateOrderMenu(orderIdAnswer)



def updateOrderMenu(orderId):
	print("Enter values for the attributes you want to update")
	question = [
		inquirer.List(
			'status',
			message='Choose the new status of order',
			choices=['Current', 'Completed', 'Dispatched', 'Back']
			)
	]
	answer = inquirer.prompt(question)
	status = answer.get('status')
	if status == 'Completed':
		question2 = [
			inquirer.Text('date', 'Enter the delivered date')    		
		]
		ans = inquirer.prompt(question2)
		date = ans.get('date')
		updateDeliveredOrder(orderId, status, date)		
	elif status == 'Current' or status == 'Dispatched':
		question2 = [
			inquirer.Text('date', 'Enter the expected date of delivery')    		
		]
		ans = inquirer.prompt(question2)
		date = ans.get('date')
		updateCurrentOrder(orderId, status, date)
	prGreen("Order has been successfully updated!\n")
	showEmployeeOrders()







