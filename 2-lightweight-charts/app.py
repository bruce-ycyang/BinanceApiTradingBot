from flask import Flask, render_template, request, flash, redirect, jsonify
import config
from binance.client import Client
from binance.enums import *

client = Client(config.API_KEY, config.API_SECRET)

app = Flask(__name__)
app.secret_key = b"assdfsdfsjfkljklsjdlkfjlwernojfas;dklflsdlsdf"


@app.route("/")
def index():
    title = "Coinview"

    info = client.get_account()

    my_balances = info["balances"]

    exchange_info = client.get_exchange_info()

    symbols = exchange_info["symbols"]

    return render_template(
        "index.html", title=title, my_balances=my_balances, symbols=symbols
    )


@app.route("/buy", methods=["POST"])
def buy():
    print(request.form)
    try:
        order = client.create_order(
            symbol=request.form["symbol"],
            side=SIDE_BUY,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=request.form["quantity"],
            price=request.form["price"],
        )
    except Exception as e:
        flash(e.message, "error")

    return redirect("/")


@app.route("/sell", methods=["POST"])
def sell():
    print(request.form)
    try:
        order = client.create_order(
            symbol="BNBUSDT",
            side=SIDE_SELL,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=request.form["quantity"],
            price=request.form["price"],
        )
    except Exception as e:
        flash(e.message, "error")

    return redirect("/")


@app.route("/settings")
def setting():
    return "settings"


@app.route("/history")
def history():
    candlesticks = client.get_historical_klines(
        "BNBUSDT", Client.KLINE_INTERVAL_1MINUTE, "1 Nov, 2021", "16 Nov, 2021"
    )

    process_candlesticks = []

    for data in candlesticks:
        candlesticks = {
            "time": data[0] / 1000,
            "open": data[1],
            "high": data[2],
            "low": data[3],
            "close": data[4],
        }
        process_candlesticks.append(candlesticks)

    return jsonify(process_candlesticks)
