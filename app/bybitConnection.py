import ccxt

exchange = ccxt.bybit({
    'apiKey': os.getenv("BYBIT_API_KEY"),
    'secret': os.getenv("BYBIT_SECRET_KEY"),
})

print(exchange.fetch_balance())
