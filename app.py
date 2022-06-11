from flask import Flask, request, jsonify
import requests

key = "J6LWL73D8IGKISLE"
app = Flask(__name__)

stocks = [
    {"symbol": "abc", "company": "this", "open": 136.89, "high": 137.53, "low": 136.89, "close":137.02},
    {"symbol": "def", "company": "that", "open": 136.89, "high": 137.53, "low": 136.89, "close":137.02},
    {"symbol": "ghi", "company": "those", "open": 136.89, "high": 137.53, "low": 136.89, "close":137.02},
]

def find_stock_by_symbol(sym):
    for i in stocks:
        if i["symbol"] == sym:
            return i

def find_stock_by_company(company):
    for i in stocks:
        if i["company"] == company:
            return i["symbol"]

@app.get("/stocks/all")
def get_stocks():
    return jsonify(stocks)

@app.get("/stocks")
def get_stock():
    sym = request.args.getlist("symbol")
    if not sym:
        return "Error: no symbol provided"

    prices = []

    for s in sym:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={s}&apikey={key}"
        r = requests.get(url)
        prices.append(r.json())

    print(prices)
    return jsonify(prices)

@app.get("/search")
def search():
    keyword = request.args["company"]
    url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keyword}&apikey={key}"
    r = requests.get(url)
    
    return r.json()