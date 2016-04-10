def sentence_order(args):
	crust = ['hand-tossed']
	size = ['small', 'medium', 'large']
	sauce = ['garlic parmesan white sauce', 'alfredo sauce', 'bbq sauce', 'robust inspired tomato sauce', 'hot sauce', 'hearty marinara sauce']
	toppings = ['ham', 'beef', 'spinach', 'banana peppers', 'feta cheese', 'premium chicken', 'salami', 'green olives', 'roasted red peppers', 'philly steak', 'shredded provolone cheese', 'italian sausage', 'pepperoni', 'pineapple', 'jalapeno peppers', 'cheese', 'green peppers', 'cheedar cheese', 'shredded parmesan asiago', 'american cheese', 'bacon', 'diced tomatoes', 'mushrooms', 'black olives', 'onions', 'sliced italian sausage']
	#options = [crust, size, sauce, toppings]
	#string_options = ['crust', 'size', 'sauce', 'toppings']
	options = [size, sauce, toppings]
	string_options = ['size', 'sauce', 'toppings']

	food_dict =  {'garlic parmesan white sauce': u'Xw', 'ham': u'H', 'beef': u'B', 'spinach': u'Si', 'banana peppers': u'Z', 'feta cheese': u'Fe', 'alfredo sauce': u'Xf', 'premium chicken': u'Du', 'bbq sauce': u'Bq', 'salami': u'Sa', 'green olives': u'V', 'roasted red peppers': u'Rr', 'philly steak': 'Pm', 'shredded provolone cheese': u'Cp', 'italian sausage': u'S', 'pepperoni': u'P', 'pineapple': u'N', 'jalapeno peppers': u'J', 'cheese': u'C', 'green peppers': u'G', 'cheddar cheese': u'E', 'shredded parmesan asiago': u'Cs', 'american cheese': u'Ac', 'bacon': u'K', 'diced tomatoes': u'Td', 'mushrooms': u'M', 'robust inspired tomato sauce': u'X', 'black olives': u'R', 'onions': u'O', 'hot sauce': u'Ht', 'hearty marinara sauce': u'Xm', 'sliced italian sausage': u'Sb'}

	final_order = {}

	for x in range(0, len(args)):
		args[x] = args[x].lower()

	for x in range(0, len(args)):
		if args[x] == 'sauce':
			args[x-1] += ' ' + args[x]
			args[x] = 'xxxxx'
			if((args[x-2] == 'parmesan') or (args[x-2] == 'inspired')):
				args[x-3] += ' ' + args[x-2] + ' ' + args[x-1]
				args[x-2] = 'xxxxx'
				args[x-1] = 'xxxxx'
			elif args[x-2] == 'hearty':
				args[x-2] += ' ' + args[x-1]
				args[x-1] = 'xxxxx'
		elif((args[x] == 'chicken') or (args[x] == 'olives') or (args[x] == 'steak') or (args[x] == 'tomatoes')):
			args[x-1] += ' ' + args[x]
			args[x] = 'xxxxx'
		elif args[x] == 'asiago':
			args[x-1] += ' ' + args[x]
			args[x] = 'xxxxx'
			args[x-2] += ' ' + args[x-1]
			args[x-1] = 'xxxxx'
		elif args[x] == 'peppers':
			args[x-1] += ' ' + args[x]
			args[x] = 'xxxxx'
			if args[x-2] == 'roasted':
				args[x-2] += ' ' + args[x-1]
				args[x-1] = 'xxxxx'
		elif args[x] == 'cheese':
			if((args[x-1] == 'feta') or (args[x-1] == 'cheddar') or (args[x-1] == 'american')):
				args[x-1] += ' ' + args[x]
				args[x] = 'xxxxx'
			elif args[x-1] == 'provolone':
				args[x-2] += ' ' + args[x-1] + ' ' + args[x]
				args[x-1] = 'xxxxx'
				args[x] = 'xxxxx'
		elif args[x] == 'sausage':
			args[x-1] += ' ' + args[x]
			args[x] = 'xxxxx'
			if args[x-2] == 'sliced':
				args[x-2] += ' ' + args[x-1]	



	for option in options:
		for word in option:
			if word in args:
				if word in food_dict.keys():
					final_order[string_options[options.index(option)]] = food_dict[word]
				else:
					final_order[string_options[options.index(option)]] = word
	#final_order['crust'] = 'hand-tossed'
	if 'size' not in final_order.keys():
		print "You have opted for the default size or selected a non-eligible size."
		final_order['size'] = 'medium'
	if 'sauce' not in final_order.keys():
		print "You have opted for the default sauce or selected a non-eligible sauce."
		final_order['sauce'] = food_dict[u'robust inspired tomato sauce']
	if 'toppings' not in final_order.keys():
		print "You have opted for the default topping  or selected a non-eligible topping."
		final_order['toppings'] = food_dict[u'cheese']

	return final_order