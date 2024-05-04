import requests
from bs4 import BeautifulSoup
import re

company_name = "Xylo Technologies Ltd. American Depositary Shares"
pattern = re.compile(r"\b([A-Z]{1,5}\.?\-?[A-Z]{1,3}):?\(?(NASDAQ|NYSE)\)?")
fall_back_pattern = re.compile(r"\(([A-Z]{1,5})\)")

url = "https://www.google.com/search?q=" + "symbol of " + company_name + " stock"
html = requests.get(url).content


soup = BeautifulSoup(html, 'html.parser')
stock_symbol = soup.text
# print(stock_symbol)

result = pattern.search(stock_symbol)

if result:
    print(result.group(1))
else:
    result = fall_back_pattern.search(stock_symbol)
    if result:
        print(result.group(1))
    else:
        print("Not found")