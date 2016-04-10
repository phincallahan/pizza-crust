import json

def newOrder():
	#Choose crust
	while True:
		try:
			crust = int(raw_input("What crust would you like?  Enter 1 for hand-tossed, 2 for Homemade Pan, 3 for Crunchy Thin, or 4 for Brooklyn Style: "))
		except ValueError:
			print("That wasn't an option!")
		if crust > 0 and crust < 5:
			if crust == 2:
				sizeOpt = "The crust you've selected is only available in medium.  Press return to continue: "
			elif crust == 4:
				sizeOpt = "The crust you've selected is only available in large.  Press return to continue: "
			else:
				sizeOpt = "Enter 1 for small, 2 for medium, or 3 for large: "
			break
		print("That wasn't an option!")
	#Choose size
	while True:
		try:
			size = int(raw_input("\nWhat size pizza would you like?  " + sizeOpt))
		except ValueError:
			print("That wasn't an option!")
		if size > 0 and size < 4:
			break		
		print("That wasn't an option!")
	#Choose sauce
	while True:
		try:
			sauce = int(raw_input("\nWhat sauce would you like?  Enter 1 for Robust Tomato, 2 for BBQ, 3 for Garlic Parmesan, 4 for Alfredo, or 5 for None: "))
		except ValueError:
			print("That wasn't an option!")
		if size > 0 and size < 6:
			break		
		print("That wasn't an option!")
	#Choose toppings
	while True:
		toppings1 = raw_input("\nWhat toppings would you like?  Separate your selections using spaces.  Enter 0 for None, 1 for Cheddar Cheese, 2 for Pepperoni, 3 for Ham, 4 for Bacon, 5 for Feta Cheese, 6 for Pineapple, or 7 for Mushrooms: ")
		toppings2 = list(map(int,toppings1.split(' ')))
		for topping in toppings2:
			if topping < 0 or topping > 7:
				toppings2.remove(topping)
			elif topping == 0 and len(toppings2) != 1:
				toppings2.remove(topping)
		break
	order = {}
	order['crust'] = crust
	order['size'] = size
	order['sauce'] = sauce
	order['toppings'] = toppings2
	saveOrder(order)

# def setFav(favOrder):	
# def getFav():

def saveOrder(order):
	with open('order.txt', 'w') as outfile:
		json.dumps(order, outfile)
	print("Your order was saved.")
	
newOrder()