from requests import get
import os
from dotenv import load_dotenv
from pprint import PrettyPrinter

#loads .env file
load_dotenv('.env')

#getting baseurl and api key from .env
baseurl = os.getenv('BASEURL')
apikey = os.getenv('APIKEY')

#sets endpoint of the url
endpoint = f"/latest?access_key={apikey}"
url = baseurl + endpoint
    
#gets data about currencies
data = get(url).json()

#pretty format
printer = PrettyPrinter()

def get_currencies():

    #gets date of update
    date = data['date']
    #gets rates of all currencies
    rate = data['rates']
    
    #converts to list item
    rate = list(rate.items())
    
    #sorts alphabetically
    rate.sort()

    return rate

def compare_currency():
    #based on currency
    base = data['base']
    basechg = input("give currency 1")
    comparecurrency = input("give currency 2")
    
    
    urladdcurrency = f"&symbols={comparecurrency}"
    urladdbase = f"&base={basechg}"
    customurl = url + urladdbase + urladdcurrency
    
    customdata = get(customurl).json()
    
    printer.pprint(customdata)

    
compare_currency()
# rate = get_currencies()
# printer.pprint(rate)