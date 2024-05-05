from fastapi import FastAPI, Response, status, HTTPException
import requests
from bs4 import BeautifulSoup
import re

app = FastAPI(
    title="Stock ticker symbol API",
    description="This API returns the stock ticker symbol of a company given its name. It works for companies listed on NASDAQ and NYSE.",
    version="1.0",
    contact={
        "name": "@suvanbanerjee",
        "url": "https://github.com/suvanbanerjee/stock_symbol_lookup_api"
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://github.com/suvanbanerjee/stock_symbol_lookup_api/blob/main/LICENSE"
    }
)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

@app.get("/")
def read_root() -> None:
    """
    Root request
    """
    return {"message": "Welcome to the Stock ticker symbol API. Please enter the company name in the URL to get the stock ticker symbol."}

@app.get("/{company_name}")
def read_item(company_name: str):
    pattern = re.compile(r"\b([A-Z]{1,5}\.?\-?[A-Z]{1,3}):?\(?(NASDAQ|NYSE)\)?")
    fall_back_pattern = re.compile(r"\(([A-Z]{1,5})\)")
    company_name = company_name.replace(" ", "+")
    url = "https://search.yahoo.com/search?p=" + "symbol+of+" + company_name + "+stock"
    html = requests.get(url,headers=headers).content

    soup = BeautifulSoup(html, 'html.parser')
    stock_symbol = soup.text

    result = pattern.search(stock_symbol)
    # return {"test_log" : stock_symbol, "company_name": company_name, "stock_symbol": result}
    if result:
        result = result.group(1)
        print(result)
        return {"stock_symbol": result}
    else:
        result = fall_back_pattern.search(stock_symbol)
        if result:
            result = result.group(1)
            return {"stock_symbol": result}
        else:
            raise HTTPException(
            status_code=404,
            detail="Ticker not found"
        )