
def sentence_order(options):
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

    return final_order
