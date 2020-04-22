import mysql.connector
import inquirer
from prettytable import PrettyTable
import nursery_store


mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="password",
	database="nursery"
)

cursor = mydb.cursor()

#--------------------------------------- Utility methods ----------------------------------
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[32m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))

#--------------------------------------- SQL queries -------------------------------------

def getPlantsWithRating():
	sql = """SELECT DISTINCT p.plant_id, p.name, t.type_name, p.price, AVG(i.rating) AS customer_rating 
	      FROM plant p JOIN order_item i ON p.plant_id = i.plant_id 
		  JOIN plant_type t ON p.p_type_id = t.type_id 
		  GROUP BY p.plant_id, p.name, p.price, p.description, t.type_name 
 		  HAVING avg(i.rating) IS NOT NULL
 		  ORDER BY customer_rating DESC"""
	try:
		cursor.execute(sql)
		plants = cursor.fetchall()
		return plants
	except mysql.connector.Error as err:
		prRed("Error in fetching trending plants by rating!")
		prRed("MYSQL ERROR: {}".format(err))
		print("\n")


def getPlantsOrderMost():
	sql = """SELECT p.plant_id, p.name, t.type_name, p.price, COUNT(i.plant_id) AS ordered_count, AVG(i.rating) AS avg_rating 
		  FROM plant p JOIN order_item i ON p.plant_id = i.plant_id 
		  JOIN plant_type t ON p.p_type_id = t.type_id
		  GROUP BY p.plant_id, p.name, t.type_name
		  ORDER BY ordered_count DESC"""
	try:
		cursor.execute(sql)
		plants = cursor.fetchall()
		return plants
	except mysql.connector.Error as err:
		prRed("Error in fetching trending plants by most ordered!")
		prRed("MYSQL ERROR: {}".format(err))
		print("\n")


def getTopPlantGivenType(plantType):
	sql = """SELECT p.plant_id, p.name, p.price, COUNT(i.plant_id) AS ordered_count, AVG(i.rating) AS avg_rating 
		  FROM plant p JOIN order_item i ON p.plant_id = i.plant_id 
		  JOIN plant_type t ON p.p_type_id = t.type_id
		  WHERE t.type_name = %s
		  GROUP BY p.plant_id, p.name, t.type_name
		  ORDER BY ordered_count DESC"""
	try:
		cursor.execute(sql, (plantType,))
		plants = cursor.fetchall()
		return plants
	except mysql.connector.Error as err:
		prRed("Error in fetching trending plants by type!")
		prRed("MYSQL ERROR: {}".format(err))
		print("\n")


def getTopPlantGivenStore(store):
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
		cursor.execute(sql, (store,))
		result = cursor.fetchall()
		return result
	except mysql.connector.Error as err:
		prRed("Error in fetching trending plants by store!")
		prRed("MYSQL ERROR: {}".format(err))
		print("\n")


def getStoresForPlant(plantId):
	sql = """SELECT s.address FROM plant p JOIN plant_locator l
		  ON p.plant_id = l.plant_id
		  JOIN store s ON s.store_id = l.store_id
		  WHERE p.plant_id = %s"""
	try:
		cursor.execute(sql, (plantId,))
		result = cursor.fetchall()
		return result
	except mysql.connector.Error as err:
		prRed("Error in fetching stores for given plant!")
		prRed("MYSQL ERROR: {}".format(err))
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
		plant_table = PrettyTable(['Plant Id', 'Plant Name', 'Plant Type', 'Price', 'Average Rating'])
		for x in plants:
			plant_table.add_row([x[0], x[1], x[2], x[3], x[4]])
		print(plant_table)
		print("\n")
		prYellow("You can place orders by browsing plants from Stores in main menu")
		print("\n")
		showTrendingMainMenu(custID)
	elif selectedAns == 'Most ordered':
		plants  = getPlantsOrderMost()
		plant_table = PrettyTable(['Plant Id', 'Plant Name', 'Plant Type', 'Price', 'Number of customers who bought', 'Average Rating'])
		for x in plants:
			plant_table.add_row([x[0], x[1], x[2], x[3], x[4], x[5]])
		print(plant_table)
		print("\n")
		prYellow("You can place orders by browsing plants from Stores in main menu")
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
		plant_table = PrettyTable(['Plant Id', 'Plant Name', 'Price', 'Number of customers who bought', 'Average Rating'])
		for x in plants:
			plant_table.add_row([x[0], x[1], x[2], x[3], x[4]])
		print(plant_table)
		print("\n")
		prYellow("You can place orders by browsing plants from Stores in main menu")
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
		plant_table = PrettyTable(['Plant Id', 'Plant Name', 'Plant Type', 'Price', 'Number of customers who bought', 'Average Rating'])
		for x in plants:
			plant_table.add_row([x[0], x[1], x[3], x[2], x[4], x[5]])
		print(plant_table)
		nursery_store.checkForOrders(custID, store, plants)


