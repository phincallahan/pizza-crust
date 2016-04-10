import pizza_senpai
import argparse
import requests

base_url = "https://order.dominos.com/power"
menu_url = base_url + "/store/1970/menu?lang=en&structured=true"

def main():
    headers = { 'Referer': 'https://order.dominos.com/en/pages/order/' }
    menu_request = requests.get(menu_url, headers = headers)
    menu_data = menu_request.json()

    toppings = menu_data['Toppings']['Pizza']
    toppings = {v['Name']:k for k,v in toppings.iteritems()}

    print(toppings)

def getPizza():
    valid_sizes = ['small', 'medium', 'large']

    size = input("Size (small, medium, large): ")
    while( size.toLowerCase() not in valid_sizes ):
        size = input("Size (small, medium, large): ")
   

if __name__=="__main__":
    main()
    
