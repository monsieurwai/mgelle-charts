
# Libs
from flask import Flask
from flask import jsonify
from flask import request
# Imports
from stockMarket import StockMarket

# API Init
app = Flask(__name__)

# Routes


@app.route('/api/v0/routes')
def getAllRoutes():
    allRoutes = [
        {
            "routePath": "/api/v0/informations",
            "methods": ["GET"],
            "Params": [],
            "description": "Get informations about api"
        },
        {
            "routePath": "/api/v0/routes",
            "methods": ["GET"],
            "Params": [],
            "description": "Get all routes of the api"
        },

    ]
    return jsonify(allRoutes)


@app.route('/api/v0/informations')
def informations():
    informations = {
        "apiVersion": 0,
        "creator": "Gellé Matthieu",
    }
    return jsonify(informations)


@app.route('/api/v0/quotations')
def quotations():
    quote = request.args.get('quote')
    period = request.args.get('period')
    interval = request.args.get('interval')
    data = StockMarket(quote,period,interval).getData()
    return data


# API start
if __name__ == "__main__":
    app.run()
