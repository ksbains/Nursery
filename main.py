import nursery
import inquirer



def mainMenu():
        questions = [inquirer.List(
                'userType', 
                message="Are you an Employee or Customer?",
                choices=['Employee', 'Customer'],
        ),]
        answer = inquirer.prompt(questions)
        if answer["userType"] == "Employee":
                employeeStart()
        else:
                customerStart()

def employeeStart():
        # ask Employee if they want to sign up or sign in
        questions = [inquirer.List(
                'userType', 
                message="Sign in, or create a new account and join today!",
                choices=['Sign In', 'Sign Up', 'Back'],
        ),]
        answer = inquirer.prompt(questions)
        if answer["userType"] == "Sign In":
                employeeSignIn()
        elif answer["userType"] == "Sign Up":
                employeeSignUp()
        else:
                mainMenu()

def employeeSignIn():
        questions = [
          inquirer.Text('username', message="What's your username"),
          inquirer.Text('password', message="What's your password")
        ]
        
        answers = inquirer.prompt(questions)
        empUsername = answers['username']
        empPassword = answers['password']

        # check if the employee is in the DB
        result = nursery.inEmployee(empUsername)
        if not result:
                print("You are an IMPOSTER!!")
                employeeStart()
        
        if result[3] == empPassword:
                if not result[8]:
                        employeeManagerMainMenu(result[0], result[4])
                else:
                        employeeCommonMainMenu(result[0], result[4])

        else:
                print("Incorrect Password!!! Try again")
                employeeSignIn()

def employeeManagerMainMenu(empID, storeID):
        questions = [inquirer.List(
                'employeeMain', 
                message="Select an option:",
                choices=['Inventory', 'Manage Employees', 'Logout'],
        ),]
        answer = inquirer.prompt(questions)
        if answer["employeeMain"] == "Inventory": 
                inventory(empID)
        elif answer["employeeMain"] == "Manage Employees":
                manageEmp(empID)
        elif answer["employeeMain"] == "Logout":
                 employeeStart()
        else:
                print("ERROR!!! SHOULD NOT HIT THIS")

def employeeCommonMainMenu(empID, storeID):
        questions = [inquirer.List(
                'employeeMain', 
                message="Select an option:",
                choices=['Orders', 'Logout'],
        ),]
        answer = inquirer.prompt(questions)
        

        if answer["employeeMain"] == "Orders": 
                orders(empID, storeID)
        elif answer["employeeMain"] == "Logout":
                 employeeStart()
        else:
                print("ERROR!!! SHOULD NOT HIT THIS")
        

def employeeSignUp():
        questions = [
          inquirer.Text('name', message="What's your Name"),
          inquirer.Text('username', message="What's your username"),
          inquirer.Text('password', message="What's your password"),
          inquirer.Text('phone_no', message="What's your Phone #")
        ]
        answers = inquirer.prompt(questions)
        
        employeeName = answers['name']
        employeeUsername = answers['username']
        employeePassword = answers['password']
        employeePhone_no = answers['phone_no']
        employeeStart = "2020-04-27"
        employeeJob = "Sales Associate"
        employeeStoreID = 1
        employeeManager = 4
        
        # insert_employee(store_id, supervisor_id)
        nursery.insert_employee(employeeName, employeeUsername, employeePassword,employeeStoreID, employeeStart, employeePhone_no, employeeJob, employeeManager)

        print("You have signed up! go ahead and sign in now!")
        employeeSignIn()

def customerStart():
        # ask customer if they want to sign up or sign in
        questions = [inquirer.List(
                'userType', 
                message="Sign in, or create a new account and join today!",
                choices=['Sign In', 'Sign Up','Back'],
        ),]
        answer = inquirer.prompt(questions)
        if answer["userType"] == "Sign In":
                customerSignIn()
        elif answer["userType"] == "Sign Up":
                customerSignUp()
        else:
                mainMenu()

def customerSignIn():
        questions = [
          inquirer.Text('username', message="What's your username"),
          inquirer.Text('password', message="What's your password")
        ]
        
        answers = inquirer.prompt(questions)
        custUsername = answers['username']
        custPassword = answers['password']

        # check if the customer is in the DB
        result = nursery.inCustomer(custUsername)
        if not result:
                print("You are an IMPOSTER!!")
                customerStart()
        
        if result[3] == custPassword:
                customerMainMenu(result[0])
        else:
                print("Incorrect Password!!! Try again")
                customerSignIn()

def customerMainMenu(custID):
        questions = [inquirer.List(
                'customerMain', 
                message="Select an option:",
                choices=['Store', 'MyOrders', 'Trending', "SearchPlant", 'Logout'],
        ),]
        answer = inquirer.prompt(questions)

        if answer["customerMain"] == "Store":
                 store(custID)
        elif answer["customerMain"] == "MyOrders": 
                myOrders(custID)
        elif answer["customerMain"] == "Trending": 
                trendingPlants(custID)
        elif answer["customerMain"] == "SearchPlant": 
                searchPlant(custID)
        elif answer["customerMain"] == "Logout":
                 customerStart()
        else:
                print("ERROR!!! SHOULD NOT HIT THIS")
        

def customerSignUp():
        questions = [
          inquirer.Text('name', message="What's your Name"),
          inquirer.Text('username', message="What's your username"),
          inquirer.Text('password', message="What's your password"),
          inquirer.Text('phone_no', message="What's your Phone #"),
          inquirer.Text('address', message="What's your Address"),
          inquirer.Text('email_id', message="What's your email_id")
        ]
        answers = inquirer.prompt(questions)
        
        customerName = answers['name']
        customerUsername = answers['username']
        customerPassword = answers['password']
        customerPhone_no = answers['phone_no']
        customerAddress = answers['address']
        customerEmail = answers['email_id']
        
        nursery.insert_customer(customerName, customerUsername, customerPassword, customerPhone_no, customerAddress, customerEmail)

        print("You have signed up! go ahead and sign in now!")
        customerSignIn()
        

        


def orders(empID, storeID):
        print("orders needs to be implmented here")
        print("The parameters passed in are EmpID: " + str(empID) + " and  storeID: " + str(storeID))
        employeeCommonMainMenu(empID, storeID)

def inventory(empID, storeID):
        print("orders needs to be implmented here")
        print("The parameters passed in are EmpID: " + str(empID) + " and storeID: " + str(storeID))
        employeeManagerMainMenu(empID, storeID)

def manageEmp(empID):
        print("manageEmp needs to be implmented here")
        print("The parameters passed in are EmpID: " + str(empID))
        employeeManagerMainMenu(empID, storeID)

def myOrders(custID):
        print("myOrders needs to be implmented here")
        print("The parameters passed in are CustID: " + str(custID))
        customerMainMenu(custID)


def trendingPlants(custID):
        print("trendingPlants needs to be implmented here")
        print("The parameters passed in are CustID: " + str(custID))
        customerMainMenu(custID)


def searchPlant(custID):
        print("searchPlant needs to be implmented here")        
        print("The parameters passed in are CustID: " + str(custID))
        customerMainMenu(custID)

def store(custID):
        print("store needs to be implmented here")
        print("The parameters passed in are CustID: " + str(custID))
        customerMainMenu(custID)

def startScript():
        # nursery.startup()
        # nursery.main()
        mainMenu()

startScript()


