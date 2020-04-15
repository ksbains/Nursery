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
                choices=['Sign In', 'Sign Up'],
        ),]
        answer = inquirer.prompt(questions)
        if answer["userType"] == "Sign In":
                employeeSignIn()
        else:
                employeeSignUp()


def customerStart():
        # ask customer if they want to sign up or sign in
        questions = [inquirer.List(
                'userType', 
                message="Sign in, or create a new account and join today!",
                choices=['Sign In', 'Sign Up'],
        ),]
        answer = inquirer.prompt(questions)
        if answer["userType"] == "Sign In":
                customerSignIn()
        else:
                customerSignUp()

def customerSignIn():
        questions = [
          inquirer.Text('username', message="What's your username"),
          inquirer.Text('password', message="What's your password")
        ]
        
        answers = inquirer.prompt(questions)
        custUsername = answers['username']
        custPassword = answers['password']
        # custUsername = "jefe"
        # custPassword = "myNameJeff"
        # check if the customer is in the DB
        result = nursery.inCustomer(custUsername)
        
        if result == [] :
                # print("You are an IMPOSTER!!")
                customerStart()
        elif result[3] == custPassword :
                print("AYE gotta have that customer main doe")
        else:
                # print("Incorrect Password!!! Try again")
                customerSignIn()



        

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
        
        custUsername = answers['username']
        customerPassword = answers['password']
        

        
def startScript():
        nursery.startup()
        # nursery.main()
        mainMenu()

startScript()


