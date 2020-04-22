import inquirer
# from pyfiglet import figlet_format
from prettytable import PrettyTable
import mysql.connector

# print(figlet_format('Green Ivy', font='slant'))
# print("---------------WELCOME TO GREEN IVY NURSERY-------------- \n\n")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="nursery",
    database="nursery",
    auth_plugin='mysql_native_password'
)

cursor = mydb.cursor()

# -------------------------------------GET PLANT TYPES FROM LOCATION-------------------------------------------

def getAllPlantTypes(custID, store_location):
    questions = [
        inquirer.Checkbox('p_type',
                          message="Plant Types: <space> to select, and <space> again to toggle",
                          choices=fetchPlantTypes(),
                          )
    ]
    answers = inquirer.prompt(questions)
    plant_type = answers.get('p_type')

    if not plant_type:
        prRed("Please select a type!! \n")
        getAllPlantTypes(custID, store_location)

    else:
        types = tuple(plant_type)
        #plants = fetchPlantsByType(store_location, plant_type)
        plants = fetchPlantsByType(store_location, types)

        plant_type_table = PrettyTable(['PlantID', 'Name', 'Price', 'Plant Age', 'Type', 'Description'])

        if not plants:
            prRed("All plants are sold!! \n")
            searchPlants(custID)

        else:
            for i in plants:
                plant_type_table.add_row([i[0], i[1], i[2], i[3], i[4], i[5]])
            print(plant_type_table)
            checkForOrders(custID, store_location, plants)

# -----------------------------GET PLANT BELOW PRICE RANGE FROM LOCATION----------------------------------
def getAllPriceRanges(custID, store_location):
    questions = [
        inquirer.List('price_r',
                      message="Price range",
                      choices=['Upto 40$', 'Upto 50$', 'Upto 60$', 'Upto 70$', 'Upto 80$', 'Any range'],
                      )
    ]
    answers = inquirer.prompt(questions)
    price_range = answers.get('price_r')

    price = ""
    for i in price_range:
        if i.isdigit():
            price = "".join([price, i])

    if price == "":
        price = "0"

    plants = fetchPlantsByPrice(store_location, price)
    plant_type_table = PrettyTable(['PlantID', 'Name', 'Price', 'Plant Age', 'Type', 'Description'])

    if not plants:
        prRed("All plants are sold!! \n")
        searchPlants(custID)
    else:
        for i in plants:
            plant_type_table.add_row([i[0], i[1], i[2], i[3], i[4], i[5]])
        print(plant_type_table)
        checkForOrders(custID, store_location, plants)

# ---------------------------------------GET ALL PLANTS FROM LOCATION--------------------------------------
def getAllPlants(custID, store_location):
    # print("Method definition: location:"+store_location)
    plants = fetchAllPlants(store_location)

    plant_type_table = PrettyTable(['PlantID', 'Name', 'Price', 'Plant Age', 'Type', 'Description'])

    if not plants:
        prRed("All plants are sold!!\n")
        searchPlants(custID)
    else:
        for i in plants:
            plant_type_table.add_row([i[0], i[1], i[2], i[3], i[4], i[5]])
        print(plant_type_table)
        checkForOrders(custID, store_location, plants)


# -------------------------------------GET PLANTS FROM LOCATION-------------------------------------------
def getPlantsFromLocation(custID, store_location):
    print("Pick a category and we'l show you our best collection")
    questions = [
        inquirer.List('categry',
                      message="Shop By Category",
                      choices=['Plant Type', 'Price Range', 'Show all varities from the Location'],
                      )
    ]
    answers = inquirer.prompt(questions)
    category = answers.get('categry')

    if category == 'Plant Type':
        getAllPlantTypes(custID, store_location)
    elif category == 'Price Range':
        getAllPriceRanges(custID, store_location)
    elif category == 'Show all varities from the Location':
        getAllPlants(custID, store_location)


# ------------------------------------INITIAL STORE LIST AND PLANT TYPE LIST--------------------------------------

def fetchStores():
    sql = "SELECT address FROM store"
    try:
        cursor.execute(sql)
        result = [item[0] for item in cursor.fetchall()]
        return (result)
    except mysql.connector.Error as err:
        print("MYSQL ERROR: {}".format(err))


def fetchStoreId(store_location):
    sql = "SELECT store_id FROM store where address = %s"
    try:
        cursor.execute(sql, (store_location,))
        result = [item[0] for item in cursor.fetchall()]
        return (result)
    except mysql.connector.Error as err:
        print("MYSQL ERROR: {}".format(err))


def fetchPlants(plant_ids):
    t = tuple(plant_ids)
    if len(plant_ids) == 1:
        sql = "SELECT plant_id,name,price FROM plant WHERE plant_id = %s"
        cursor.execute(sql, (plant_ids[0],))
    elif len(plant_ids) > 1:
        sql = "SELECT plant_id,name,price FROM plant WHERE plant_id IN {}".format(t)
        cursor.execute(sql)
    try:
        result = cursor.fetchall()
        return (result)
    except mysql.connector.Error as err:
        print("MYSQL ERROR: {}".format(err))


def fetchPlantTypes():
    sql = "SELECT type_name FROM plant_type"
    try:
        cursor.execute(sql)
        result = [item[0] for item in cursor.fetchall()]
        return (result)
    except mysql.connector.Error as err:
        print("MYSQL ERROR: {}".format(err))


def fetchPlantsByType(store_location, plant_type):

    if not plant_type:
        return None
    else:
        if len(plant_type) == 1:
            sql = "select distinct p.plant_id, p.name, p.price, p.age, t.type_name, p.description from plant p join plant_locator l on p.plant_id = l.plant_id join store s on s.store_id = l.store_id join plant_type t on p.p_type_id = t.type_id where s.address = %s and t.type_name = %s"
            cursor.execute(sql, (store_location,plant_type[0]))
        elif len(plant_type) > 1:
            sql = "select distinct p.plant_id, p.name, p.price, p.age, t.type_name, p.description from plant p join plant_locator l on p.plant_id = l.plant_id join store s on s.store_id = l.store_id join plant_type t on p.p_type_id = t.type_id where s.address = %s and t.type_name IN {}".format(plant_type)
            cursor.execute(sql, (store_location,))
        try:
            result = cursor.fetchall()
            return (result)
        except mysql.connector.Error as err:
            print("MYSQL ERROR: {}".format(err))


def fetchPlantsByPrice(store_location, price):
    if price == "0":
        result = fetchAllPlants(store_location)
        return (result)
    else:
        sql = "select distinct p.plant_id, p.name, p.price, p.age, t.type_name, p.description from plant p join plant_locator l on p.plant_id = l.plant_id join store s on s.store_id = l.store_id join plant_type t on p.p_type_id = t.type_id where s.address = %s and p.price <= %s"
        try:
            cursor.execute(sql, (store_location, price))
            result = cursor.fetchall()
            return (result)
        except mysql.connector.Error as err:
            print("MYSQL ERROR: {}".format(err))


def fetchAllPlants(store_location):
    sql = "select distinct p.plant_id, p.name, p.price, p.age, t.type_name, p.description from plant p join plant_locator l on p.plant_id = l.plant_id join store s on s.store_id = l.store_id join plant_type t on p.p_type_id = t.type_id where s.address = %s"
    try:
        cursor.execute(sql, (store_location,))
        result = cursor.fetchall()
        return (result)
    except mysql.connector.Error as err:
        print("MYSQL ERROR: {}".format(err))


def fetchCustomerAddress(custID):
    sql = "select address from customer where cust_id = %s"
    try:
        cursor.execute(sql, (custID,))
        result = [item[0] for item in cursor.fetchall()]
        return (result)
    except mysql.connector.Error as err:
        print("MYSQL ERROR: {}".format(err))

# ---------------------------- STORING ORDER DETAILS --------------------------------------
def saveOrderDetails(custID, store_location, order_type, payment_status, order_amount, address, plants):

    store_id = fetchStoreId(store_location)
    store_id = store_id[0]

    sql = "INSERT INTO orders(store_id, cust_id, order_date, order_type, payment_status, price, delivery_address) VALUES(%s, %s, CURDATE(), %s, %s, %s, %s)"
    cursor.execute(sql, (store_id, custID, order_type, payment_status, order_amount, address))
    mydb.commit()

    order_id = cursor.lastrowid

    for i in plants:
        sql = "INSERT INTO order_item(order_id, quantity, plant_id, price) VALUES(%s, %s, %s, %s)"
        cursor.execute(sql, (order_id, "1", i[0], i[2]))
        mydb.commit()
    #print("order id is:",order_id)


# ------------------------------MAIN METHOD - SELECT STORE LOCATION-----------------------------------
def searchPlants(custID):
    print("Locate your nearby Store")
    questions = [
        inquirer.List('store_loc',
                      message="Store Locations",
                      choices=fetchStores()
                      )
    ]
    answers = inquirer.prompt(questions)
    store_location = answers.get('store_loc')

    if answers is not None:
        getPlantsFromLocation(custID, store_location)

def makeOrders(custID, store_location, plant_ids):

    orders = fetchPlants(plant_ids)
    order_amount = 0;
    for i in orders:
        order_amount = order_amount+i[2];

    print("Great! Let's get you through the final steps of your order!")
    print("You have ordered for", ", ".join(item[1] for item in orders), "and the total order amount is $"+str(order_amount)+"\n" )
    #print("and the total order amount is", order_amount, "\n")

    questions = [
        inquirer.List('odr_typ',
                      message="How do you want us to deliver?",
                      choices=['Home Delivery', 'Store Pickup'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    order_type = answers.get('odr_typ')

    if order_type == "Home Delivery":
        questions = [
            inquirer.List('odr_adr',
                          message="Would you like us to deliver the items to the registered address?",
                          choices=['Yes', 'No'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        order_address = answers.get('odr_adr')

        if order_address == "Yes":
            addr1 = fetchCustomerAddress(custID)
            address = addr1[0]

        elif order_address == "No":
            questions = [
                inquirer.Text('addr', message="Enter the Delivery Address:")
                ]
            answers = inquirer.prompt(questions)
            address = answers.get('addr')

        payment_status = "Paid"
        saveOrderDetails(custID, store_location, order_type, payment_status, order_amount, address, orders)

        prGreen("Great! Your order is confirmed and you can expect it in 2-3 business days \n")

    elif order_type == "Store Pickup":

        payment_status = "Cash on Delivery"
        address = store_location+" store"
        saveOrderDetails(custID, store_location, order_type, payment_status, order_amount, address, orders)

        prGreen("Your order will be ready for pick-up in our "+store_location+" store in 4 hours.")
        prGreen("Checkout our hot selling plants section! \n")

def checkForOrders(custID, store_location, plant):
    questions = [
        inquirer.List('order_req',
                      message="Want to make an order?",
                      choices=['Yes', 'No']
                      )
    ]
    answers = inquirer.prompt(questions)
    order = answers.get('order_req')

    if order == "Yes":
        plants = []
        for p in plant:
            plants.append(tuple(["{} - ${}".format(p[1], p[2]), p[0]]))

        plant_ids = choiceForOrders(custID, store_location, plants)
        makeOrders(custID, store_location, plant_ids)

    elif order == "No":
        print("Cool! Check out on our other collections! \n")
        getPlantsFromLocation(custID, store_location)

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[32m {}\033[00m" .format(skk))

def choiceForOrders(custID, store_location, plants):
    questions = [
        inquirer.Checkbox('order_yes',
                          message="Please go ahead and select your favourites",
                          choices=plants
                          )
    ]
    answers = inquirer.prompt(questions)
    orders = answers.get('order_yes')

    if not orders:
        prRed("Please select a plant to order!! \n")
        choiceForOrders(custID, store_location, plants)
    else:
        order_size = len(orders)
        if order_size > 5:
            prRed("You can select only upto 5 plants!")
            choiceForOrders(custID, store_location, plants)

    return orders

#searchPlants("1")