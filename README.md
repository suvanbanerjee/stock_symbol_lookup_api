# Stock ticker lookup API

This is a simple stock symbol or ticker lookup API that converts a company name to a stock symbol. It is build using FastAPI and is free to use (no keys attached :D). moreover it's typo proof, that means you dont have to write the exact name of the company, it will try to find the closest match. (like `Apple Inc`. and `appul` will return the same `AAPL`)

## Usage

Simply send a GET request to the following endpoint:

```
https://stock-symbol-lookup-api.onrender.com/COMPANY_NAME
```

Where `COMPANY_NAME` is the name of the company you want to lookup. For example, to lookup the stock symbol for Apple, you would send a GET request to:
```
https://stock-symbol-lookup-api.onrender.com/apple
```

The response will be a JSON object with the following format:
```json
{
  "stock_symbol": "AAPL"
}
```

## Caution 

This tool is not perfect and may not return the correct stock symbol for all companies. It has a problem of false positives, meaning it may return a stock symbol that is not the one you are looking for. Use at your own risk!

### PS: Dont spam and if you like it, consider giving a star to the repo :)