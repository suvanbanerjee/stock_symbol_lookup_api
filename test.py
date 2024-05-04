import requests
from bs4 import BeautifulSoup
import re

company_name = "jpmc"
pattern = re.compile(r"\b[A-Z]{1,5}\.?[A-Z]{1,3}\((NASDAQ|NYSE)\)")

url = "https://www.google.com/search?q=" + "symbol of " + company_name + " stock"
html = requests.get(url).content


soup = BeautifulSoup(html, 'html.parser')
stock_symbol = soup.text
# print(stock_symbol)

result = pattern.search(stock_symbol)

if result:
    result = result.group()
    result = result.split("(")
    print(result[0])
else:
    print("Not found")