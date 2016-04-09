#!/usr/bin/env python

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('order', nargs='+', help='user\'s order')
args = parser.parse_args()
confirmation = ['order']
crust = ['hand-tossed']
size = ['small', 'medium', 'large']
sauce = ['robust inspired tomato sauce']
toppings = ['cheese', 'pepperoni', 'sausage']
options = [confirmation, crust, size, sauce, toppings]
string_options = ['confirmation', 'crust', 'size', 'sauce', 'toppings']
final_order = {}
for option in options:
	for word in option:
		if((string_options[options.index(option)] != 'confirmation') and (word in args.order)):
			final_order[string_options[options.index(option)]] = word
print final_order 

