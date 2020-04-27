import mysql.connector
import inquirer
from prettytable import PrettyTable
import nursery_store
import logging
logging.basicConfig(filename="nursery.log", level=logging.DEBUG)

def getConnection():	
	conn = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="password",
		database="nursery"
	)
	return conn

#--------------------------------------- Utility methods ----------------------------------
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[32m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))

#--------------------------------------- SQL queries -------------------------------------

def getPlantsWithRating():
	logging.info("getPlantsWithRating(): Attempting to fetch plants by rating")
	sql = """SELECT DISTINCT p.plant_id, p.name, t.type_name, p.price, AVG(i.rating) AS customer_rating 
	      FROM plant p JOIN order_item i ON p.plant_id = i.plant_id 
		  JOIN plant_type t ON p.p_type_id = t.type_id 
		  GROUP BY p.plant_id, p.name, p.price, p.description, t.type_name 
 		  HAVING avg(i.rating) IS NOT NULL
 		  ORDER BY customer_rating DESC"""
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql)
		plants = cursor.fetchall()
		cursor.close()
		conn.close()
		logging.info("getPlantsWithRating(): Fetched data successfully")
		return plants
	except mysql.connector.Error as err:
		prRed("Error in fetching trending plants by rating!")
		logging.error("getPlantsWithRating(): {}".format(err))
		print("\n")


def getPlantsOrderMost():
	logging.info("getPlantsOrderMost(): Attempting to fetch plants by most ordered")
	sql = """SELECT p.plant_id, p.name, t.type_name, p.price, COUNT(i.plant_id) AS ordered_count, AVG(i.rating) AS avg_rating 
		  FROM plant p JOIN order_item i ON p.plant_id = i.plant_id 
		  JOIN plant_type t ON p.p_type_id = t.type_id
		  GROUP BY p.plant_id, p.name, t.type_name
		  ORDER BY ordered_count DESC"""
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql)
		plants = cursor.fetchall()
		cursor.close()
		conn.close()
		logging.info("getPlantsOrderMost(): Fetched data successfully")
		return plants
	except mysql.connector.Error as err:
		prRed("Error in fetching trending plants by most ordered!")
		logging.error("getPlantsOrderMost(): {}".format(err))
		print("\n")


def getTopPlantGivenType(plantType):
	logging.info("getTopPlantGivenType(): Attempting to fetch plants by type")
	sql = """SELECT p.plant_id, p.name, p.price, COUNT(i.plant_id) AS ordered_count, AVG(i.rating) AS avg_rating 
		  FROM plant p JOIN order_item i ON p.plant_id = i.plant_id 
		  JOIN plant_type t ON p.p_type_id = t.type_id
		  WHERE t.type_name = %s
		  GROUP BY p.plant_id, p.name, t.type_name
		  ORDER BY ordered_count DESC"""
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (plantType,))
		plants = cursor.fetchall()
		cursor.close()
		conn.close()
		logging.info("getTopPlantGivenType(): fetched data successfully")
		return plants
	except mysql.connector.Error as err:
		prRed("Error in fetching trending plants by type!")
		logging.error("getTopPlantGivenType(): {}".format(err))
		print("\n")


def getTopPlantGivenStore(store):
	logging.info("getTopPlantGivenStore(): Attempting to fetch plants by type")
	sql = """SELECT p.plant_id, p.name, p.price, t.type_name,
		  COUNT(i.plant_id) AS ordered_count, AVG(i.rating) AS avg_rating  
		  FROM plant p JOIN order_item i ON p.plant_id = i.plant_id
		  JOIN orders o ON i.order_id = o.order_id
		  JOIN store s ON s.store_id = o.store_id
		  JOIN plant_type t ON t.type_id = p.p_type_id
		  WHERE s.address = %s
		  GROUP BY p.plant_id, p.name, p.price, t.type_name
		  ORDER BY ordered_count DESC"""
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(sql, (store,))
		result = cursor.fetchall()
		cursor.close()
		conn.close()
		logging.info("getTopPlantGivenStore(): fetched data successfully")
		return result
	except mysql.connector.Error as err:
		prRed("Error in fetching trending plants by store!")
		logging.error("getTopPlantGivenStore(): {}".format(err))
		print("\n")


#--------------------------------------- Menu flow ---------------------------------------

def showTrendingMainMenu(custID):
	question = [
		inquirer.List(
				'type',
				message='View trending plants by ',
				choices=['Rating', 'Most ordered', 'Type', 'Store', 'Back'],
				default = 'Rating'
			)
	]
	answer = inquirer.prompt(question)
	selectedAns = answer.get('type')
	plants = []
	
	if selectedAns == 'Rating':
		plants  = getPlantsWithRating()
		if len(plants) != 0:
			plant_table = PrettyTable(['Plant Id', 'Plant Name', 'Plant Type', 'Price', 'Average Rating'])
			for x in plants:
				plant_table.add_row([x[0], x[1], x[2], x[3], x[4]])
			print(plant_table)			
		else:
			prYellow("Plants haven't been rated yet! Be the first to rate!")
			prYellow("You can rate the items from MyOrders")
		prYellow("You can place orders by browsing plants from Stores in main menu\n")
		print("\n")
		showTrendingMainMenu(custID)
	elif selectedAns == 'Most ordered':
		plants  = getPlantsOrderMost()
		if len(plants) != 0:
			plant_table = PrettyTable(['Plant Id', 'Plant Name', 'Plant Type', 'Price', 'Number of customers who bought', 'Average Rating'])
			for x in plants:
				plant_table.add_row([x[0], x[1], x[2], x[3], x[4], x[5]])
			print(plant_table)
		else:
			prYellow("Plants haven't been ordered yet! Be the first to order!")
		prYellow("You can place orders by browsing plants from Stores in main menu\n")
		print("\n")
		showTrendingMainMenu(custID)
	elif selectedAns == 'Type':
		question = [
			inquirer.List(
				'plantType',
				message='Choose the plant type',
				choices=nursery_store.fetchPlantTypes()
				)
		]
		answer = inquirer.prompt(question)
		plantType = answer.get('plantType')
		plants = getTopPlantGivenType(plantType)
		if len(plants) != 0:
			plant_table = PrettyTable(['Plant Id', 'Plant Name', 'Price', 'Number of customers who bought', 'Average Rating'])
			for x in plants:
				plant_table.add_row([x[0], x[1], x[2], x[3], x[4]])
			print(plant_table)
		else:
			prYellow("Plants haven't been ordered yet! Be the first to order!")
		prYellow("You can place orders by browsing plants from Stores in main menu\n")
		print("\n")
		showTrendingMainMenu(custID)
	elif selectedAns == 'Store':
		question = [
			inquirer.List(
				'stores',
				message='Choose the store',
				choices=nursery_store.fetchStores()
				)
		]
		answer = inquirer.prompt(question)
		store = answer.get('stores')
		storeId = nursery_store.fetchStoreId(store)
		plants = getTopPlantGivenStore(store)
		if len(plants) != 0:
			plant_table = PrettyTable(['Plant Id', 'Plant Name', 'Plant Type', 'Price', 'Number of customers who bought', 'Average Rating'])
			for x in plants:
				plant_table.add_row([x[0], x[1], x[3], x[2], x[4], x[5]])
			print(plant_table)
			nursery_store.checkForOrders(custID, store, plants)
		else:
			prYellow("Plants haven't been ordered/rated yet! Be the first to order!")
			prYellow("You can place orders by browsing plants from Stores in main menu\n")


