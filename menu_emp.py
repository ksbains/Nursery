import nursery
import inquirer
import mysql.connector

mydb = mysql.connector.connect(
	host="127.0.0.1",
	user="root",
	passwd="password",
	database="nursery"
)

cursor = mydb.cursor()

def mainMenu(empID, storeID):
    questions = [inquirer.List(
                'userType', 
                message="What would you like to do?",
                choices=['Employee Management', 'Inventory Management'],),]
    answer = inquirer.prompt(questions)
    if answer["userType"] == "Employee Management":
            empManMenu(empID, storeID)
    else:
            invManMenu(empID, storeID)

def empManMenu(empID, storeID):
    questions = [inquirer.List(
                'userType', 
                message="What would you like to do?",
                choices=['Hire Employee', 'Fire Employee', 'Promote Employee'],),]
    answer = inquirer.prompt(questions)
    if answer["userType"] == "Hire Employee":
        print("hireEmpMenu()")
    elif answer["userType"] == "Fire Employee":
        print("fireEmpMenu()")
    else:
        print("promEmpMenu()")
def invManMenu(empID, storeID):
    questions = [inquirer.List(
                'userType', 
                message="What would you like to do?",
                choices=['Add Plants', 'Delete Plants', 'Update Plants', 'Show Plants'],),]
    answer = inquirer.prompt(questions)
    if answer["userType"] == "Add Plants":
        addPlantsMenu(empID, storeID)
    elif answer["userType"] == "Delete Plants":
        deletePlantsMenu(empID, storeID)
    elif answer["userType"] == "Update Plants":
        updatePlantsMenu(empID, storeID)
    elif answer["userType"] == "Show Plants":
        showPlantsMenu(empID, storeID)

def addPlantsMenu(empID, storeID):
    questions = [
        inquirer.Text('name', message="What's the plant name?"),
        inquirer.Text('price', message="What's the plant price?"),
        inquirer.Text('description', message="What's the plant description?"),
        inquirer.Text('age', message="What's the plant age?"),]
    answers = inquirer.prompt(questions)
    nursery.add_plant(answers["name"], answers["price"], answers["description"], answers["age"])
    print(answers["name"], "added!")
    invManMenu(empID, storeID)

def deletePlantsMenu(empID, storeID):
    print("hi")
    invManMenu(empID, storeID)
    

def updatePlantsMenu(empID, storeID):
    print("hi")
    invManMenu(empID, storeID)

def showPlantsMenu(empID, storeID):
    sql = "SELECT p.name, p.price, p.description, p.age FROM plant p"#, plants_locator l WHERE l.store_id = %s"
    try:
        cursor.execute(sql) #, storeID)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print("MYSQL ERROR: {}".format(err))
    invManMenu(empID, storeID)
