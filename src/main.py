from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import re

app = FastAPI()


@app.get("/{company_name}")
def read_item(company_name: str):
    pattern = re.compile(r"\b[A-Z]{1,5}\.?[A-Z]{1,3}\((NASDAQ|NYSE)\)")

    url = "https://www.google.com/search?q=" + "symbol of " + company_name + " stock"
    html = requests.get(url).content

    soup = BeautifulSoup(html, 'html.parser')
    stock_symbol = soup.text

    result = pattern.search(stock_symbol)

    if result:
        result = result.group()
        result = result.split("(")
        return {"stock_symbol": result[0]}
    else:
        return {"stock_symbol": "Not found"}