import sys
import os.path
import re
import json

#Checks to see if app has been previously used.
#If true, continues to confirmation of personal info.
#If false, continues to setup, then confirmation of personal info.
def begin():
	if os.path.isfile("./profile.txt") and os.path.isfile("./delAddress.txt"):
		print("- - - - - - - - - -\nIt looks like you've used pizza.py before, let's confirm your information.")
		confirm()
	else:
		print("- - - - - - - - - -\nWelcome to pizza.py.")
		if not os.path.isfile("./profile.txt"):
			setup1()
			if os.path.isfile("./delAddress.txt"):
				open("delAddress.txt", "r")
		if not os.path.isfile("./delAddress.txt"):
			setup2()
			if os.path.isfile("./profile.txt"):
				open("profile.txt", "r")
		confirm()

#Stores customer basic information (name, phone, email).
def setup1():
	print("- - - - - - - - - -\nLets set up your personal profile.")
	firstName = raw_input("Enter your first name: ") + '\n'
	lastName = raw_input("Enter your last name: ") + '\n'
	while True:
		try:
			phone = int(raw_input("Enter your phone number: "))
			break
		except ValueError:
			print "That wasn't a number!"
	phone = str(phone) + '\n'
	email = raw_input("Enter your email: ")
	
	#writes profile file
	profile = open("profile.txt", "w")
	profile.write(firstName + lastName + phone + email)
	profile.close()
	
	return profile

#Stores delivery address.
def setup2():
	print("- - - - - - - - - -\nLets set up your delivery address.")
	address1 = raw_input("Enter your address line 1 (e.g. 123 Sunny Street): ") + '\n'
	address2 = raw_input("Enter your address line 2 (e.g. Apartment 12A): ")
	if not address2:
		address2 = "NULL\n"
	city = raw_input("Enter your city (e.g. Los Angeles): ") + '\n'
	state = raw_input("Enter your state (e.g. CA): ") + '\n'
	while True:
		try:
			zip = int(raw_input("Enter your zip code (e.g. 95107): "))
			break
		except ValueError:
			print "That wasn't a number!"
	zip = str(zip)

	#writes delivery address file
	delAddress = open("delAddress.txt", "w")
	delAddress.write(address1 + address2 + city + state + zip)
	delAddress.close()
	
	return delAddress

#Prints all personal info.
#Requests that user confirm all info is correct.
#If any info is wrong, allows user to reset.
#Once all info is correct, parses information into JSON objects, then proceeds to next phase of madness.
def confirm():
	#Prints basic info and requests confirmation.
	while True:
		profile = open("profile.txt", "r")
		firstName = (profile.readline()).rstrip()
		lastName = (profile.readline()).rstrip()
		phone = (profile.readline()).rstrip()
		email = (profile.readline()).rstrip()
		print("- - - - - - - - - -\nFirst name: "+ firstName + "\nLast name: " + lastName + "\nYour phone number: " + phone + "\nYour email: " + email + "\n- - - - - - - - - -")
		try:
			ready1 = int(raw_input("If this information is correct, enter 1, if not, enter 2: "))
		except ValueError:
			print "That wasn't an option!"
		if ready1 == 1:
			break
		elif ready1 == 2:
			os.remove("./profile.txt")
			setup1()
			profile = open("profile.txt", "r")
		else:
			print "That wasn't an option!"
			
	#Prints address and requests confirmation.
	while True:
		delAddress = open("delAddress.txt", "r")
		address1 = (delAddress.readline()).rstrip()
		address2 = (delAddress.readline()).rstrip()
		address2 = str.replace(address2,"NULL","n/a",1)
		city = (delAddress.readline()).rstrip()
		state = (delAddress.readline()).rstrip()
		zip = (delAddress.readline()).rstrip()
		print("- - - - - - - - - -\nAddress Line 1: "+ address1 + "\nAddress Line 2: " + address2 + "\nCity: " + city + "\nState: " + state + "\nZip Code: " + zip + "\n- - - - - - - - - -")
		try:
			ready1 = int(raw_input("If this information is correct, enter 1, if not, enter 2: "))
		except ValueError:
			print "That wasn't an option!"
		if ready1 == 1:
			break
		elif ready1 == 2:
			os.remove("./delAddress.txt")
			setup2()
			delAddress = open("delAddress.txt", "r")
		else:
			print "That wasn't an option!"
	print("- - - - - - - - - -\nInformation confirmed.\n- - - - - - - - - -\n")
	
	#Parses information into two JSON objects.
	data1 = {
		'firstName' : firstName,
		'lastName' : lastName,
		'phone' : phone,
		'email' : email
	}
	data2 = {
		'address1' : address1,
		'address2' : address2,
		'city' : city,
		'state' : state,
		'zip' : zip
	}
	json1 = json.dumps(data1);
	json2 = json.dumps(data2);
	#Proceeds to next phase of madness.

#Begins the whirlwind of madness
begin()