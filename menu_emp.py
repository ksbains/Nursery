import nursery
import inquirer
import mysql.connector

def getConnection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="***",
        database="nursery"
    )
    return conn

def mainMenu(empID, storeID):
    questions = [inquirer.List(
                'userType', 
                message="What would you like to do?",
                choices=['Employee Management', 'Inventory Management', 'Back'],),]
    answer = inquirer.prompt(questions)
    if answer["userType"] == "Employee Management":
        empManMenu(empID, storeID)
    elif answer["userType"] == "Inventory Management":
        invManMenu(empID, storeID)
    else:
        print("Exited")

def empManMenu(empID, storeID):
    questions = [inquirer.List(
                'userType', 
                message="What would you like to do?",
                choices=['Hire Employee', 'Fire Employee', 'Promote Employee', 'Back'],),]
    answer = inquirer.prompt(questions)
    if answer["userType"] == "Hire Employee":
        print("hireEmpMenu()")
    elif answer["userType"] == "Fire Employee":
        print("fireEmpMenu()")
    elif answer["userType"] == "Promote Employee":
        print("promEmpMenu()")
    else:
        mainMenu(empID, storeID)

def invManMenu(empID, storeID):
    questions = [inquirer.List(
                'userType', 
                message="What would you like to do?",
                choices=['Add Plants', 'Delete Plants', 'Update Plants', 'Show Plants', 'Back'],),]
    answer = inquirer.prompt(questions)
    if answer["userType"] == "Add Plants":
        addPlantsMenu(empID, storeID)
    elif answer["userType"] == "Delete Plants":
        deletePlantsMenu(empID, storeID)
    elif answer["userType"] == "Update Plants":
        updatePlantsMenu(empID, storeID)
    elif answer["userType"] == "Show Plants":
        showPlantsMenu(empID, storeID)
    else:
        mainMenu(empID, storeID)

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
    plantDict={}
    sql = "SELECT * FROM plant"#, plants_locator l WHERE l.store_id = %s"
    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute(sql) #, storeID)
        result = cursor.fetchall()
        for row in result:
            plantDict[row[0]]=row[1]
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("MYSQL ERROR: {}".format(err))
    #plantList=list(plantDict.values())
    #plantList.append("All the Above")
    #plantList.append("None of the Above")
    questions = [
                inquirer.Checkbox('deletions',
                message="What plants do you want to delete?",
                choices=plantDict.values(),
                ),]
    answers = inquirer.prompt(questions)
    answerList=list(answers.values())[0]
    for i in range(len(answerList[0])):
        plant_name = answerList[i]
        for id, name in plantDict.items():
            print(id, name, plant_name)
            if name == plant_name:
                nursery.delete_plant(id)
                break
    print(answerList, "deleted!")
    invManMenu(empID, storeID)

def updatePlantsMenu(empID, storeID):
    plantDict={}
    sql = "SELECT * FROM plant"#, plants_locator l WHERE l.store_id = %s"
    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute(sql) #, storeID)
        result = cursor.fetchall()
        for row in result:
            plantDict[row[0]]=row[1]
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("MYSQL ERROR: {}".format(err))
    '''for i in range(len(plantList)):
        plantNames.append(plantList[i][1])'''
    #plantList.append("All the Above")
    #plantList.append("None of the Above")
    questions = [
                inquirer.Checkbox('updates',
                message="What plants do you want to update?",
                choices=plantDict.values(),
                ),]
    answers = inquirer.prompt(questions)
    answerList=list(answers.values())[0]
    for i in range(len(answerList[0])):
        plant_name = answerList[i]
        for id, name in plantDict.items():
            print(id, name, plant_name)
            if name == plant_name:
                questions = [
                            inquirer.Text('price', message="What's the plant price?"),
                            inquirer.Text('description', message="What's the plant description?"),
                            inquirer.Text('age', message="What's the plant age?"),]
                answers = inquirer.prompt(questions)
                answerList=list(answers.values())[0]
                nursery.update_plant(id, name, price=answerList[0], description=answerList[1], age=answerList[2])
                break
    print(answerList, "updated!")
    invManMenu(empID, storeID)

def showPlantsMenu(empID, storeID):
    sql = "SELECT p.name, p.price, p.description, p.age FROM plant p"#, plants_locator l WHERE l.store_id = %s"
    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute(sql) #, storeID)
        result = cursor.fetchall()
        for row in result:
            print(row)
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("MYSQL ERROR: {}".format(err))
    invManMenu(empID, storeID)

mainMenu(empID, storeID)
