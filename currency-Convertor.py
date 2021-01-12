---
# Project : Currency Convertor
#Author: Priya Mondal
---


#Bitcoin - A cryptocurrency
#Modules Used : 
#              -> forex-python(Various Features are there)

#importing the required functions we will use in code
from forex_python.converter import CurrencyCodes,CurrencyRates
from forex_python.bitcoin import BtcConverter

#Let's create an instance of CurrencyCodes
test= CurrencyCodes()

#Now fetching the currency Symbol
cur_symbol =test.get_symbol('INR')

#fetching the currency name
cur_name = test.get_currency_name('INR')

print('The currency name is:' + cur_name)
print('The currency symbol is:' + cur_symbol)

#Let's do this for other currencies
print('\n' + test.get_currency_name('USD'))
print(test.get_symbol('USD'))

#Knowing the currency Rates
test1 = CurrencyRates()

#Converting 1USD to Indian Rupees
rate = test1.get_rate('USD','INR')
print(rate)

#Let's convert "any number of USDs to Indian Rupees.Here I am taking 10USD"
res = test1.convert('USD','INR',10)
print(res)

print('------------------------------------------------------------------')
#Bitcoin prices in INR
bitcoin = BtcConverter()
price = bitcoin.get_latest_price('INR')

print(price)
