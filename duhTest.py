import hashlib
import binascii
import os
import inquirer
def signin():
	questions = [
	inquirer.Text('username', message="What's your username"),
	inquirer.Text('password', message="What's your password")
	]

	answers = inquirer.prompt(questions)
	empUsername = answers['username']
	empPassword = answers['password']

	hashedPass = hash_password(empPassword)
	print(hashedPass)
	if verify_password(hashedPass, empPassword):
		print(empPassword)

def hash_password(password):
	salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
	pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
	pwdhash = binascii.hexlify(pwdhash)
	return (salt + pwdhash).decode('ascii')

def verify_password(hpswd, pswd):
	salt = hpswd[:64]
	password = hpswd[64:]
	pwdhash = hashlib.pbkdf2_hmac('sha256', pswd.encode('utf-8'), salt.encode('ascii'), 100000)
	pwdhash = binascii.hexlify(pwdhash).decode('ascii')
	return password == pwdhash 

def main():
	signin()
	

main()