import sys

#Runs setup in order to get personal info.
import setup

#Runs order in order to record your order.
import order

#If in demo mode (any argument in command line), does not continue with this
if len(sys.argv) < 1:
	#Runs send in order to send your order to Dominos.
	import send

#In demo mode (any argument in command line)
else:
	print("You are using crust in demo mode, your order was not sent.")