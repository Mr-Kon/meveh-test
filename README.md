### Setting up flask
```
python3 -m pip install flask
export FLASK_APP=app.py
flask run
```
### /stocks
Returns the open, high, low, price, change, and more for the provided symbols

http://127.0.0.1:5000/stocks?symbol=AAPL

http://127.0.0.1:5000/stocks?symbol=AAPL&symbol=IBM

### /search
Returns a list of matching companies with some details based on a provided string

http://127.0.0.1:5000/search?company=microsoft
