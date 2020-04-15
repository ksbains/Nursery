import inquirer
#import nursery



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
	  inquirer.Text('password', message="What's your password"),
	]
	answers = inquirer.prompt(questions)
	
	custUsername = answers['username']
	customerPassword = answers['password']

	# check if the customer is in the DB

def customerSignUp():
	questions = [
	  inquirer.Text('username', message="What's your username"),
	  inquirer.Text('password', message="What's your password"),
	]
	answers = inquirer.prompt(questions)
	
	custUsername = answers['username']
	customerPassword = answers['password']
	

	












def startScript():
	nursery.startup()
	mainMenu()

startScript()



