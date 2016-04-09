
def sentence_order(args):
	confirmation = ['order']
	crust = ['hand-tossed']
	size = ['small', 'medium', 'large']
	sauce = ['robust inspired tomato sauce']
	toppings = ['cheese', 'pepperoni', 'sausage']
	number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

	options = [confirmation, crust, size, sauce, toppings, number]
	string_options = ['confirmation', 'crust', 'size', 'sauce', 'toppings', 'number']

	final_order = {}

	for option in options:
		for word in option:
			if((string_options[options.index(option)] != 'confirmation') and (word in args)):
				final_order[string_options[options.index(option)]] = word	

	return final_order

print(sentence_order(['order', 'me', '3', 'large', 'pepperoni', 'pizzas']))
