"""
    API DOCUMENTATION
    https://bybit-exchange.github.io/docs/linear/#t-introduction
"""

# API Imports
from pybit import HTTP

# CONFIG VARIABLES
mode = "test"
ticker_1 = "LTCUSDT"
ticker_2 = "MINAUSDT"
signal_positive_ticker = ticker_2
signal_negative_ticker = ticker_1
rounding_ticker_1 = 2
rounding_ticker_2 = 3
quantity_rounding_ticker_1 = 1
quantity_rounding_ticker_2 = 1
max_loss_usdt_total = -500

limit_order_basis = False # Will ensure positions (except for Close) will be placed on limit basis

tradeable_capital_usdt = 2000 # total tradeable capital to be split between both pairs
max_trades_per_signal = 6 # total number of trades per ticker
stop_loss_fail_safe = 0.15 # stop loss at market order in case of drastic event
signal_trigger_thresh = 1.1 # Z-Score threshold which determines trade (must be above zero)

timeframe = 60 # make sure matches your strategy
kline_limit = 200 # make sure matches your strategy
z_score_window = 21 # make sure matches your strategy

# LIVE API
api_key_mainnet = ""
api_secret_mainnet = ""

# TESTNET API
api_key_testnet = "Uu05S4GwQuvQemCXcm"
api_secret_testnet = "ohscM8aEKHjUrQbvuw3fMYxRU20u8JmbXmWi"

# SELECTED API
api_key = api_key_testnet if mode == "test" else api_key_mainnet
api_secret = api_secret_testnet if mode == "test" else api_secret_mainnet

# SELECTED API
api_url = "https://api-testnet.bybit.com" if mode == "test" else "https://api.bybit.com"
ws_public_url = "wss://stream-testnet.bybit.com/realtime_public" if mode == "test" else "wss://stream.bybit.com/realtime_public"
ws_private_url = "wss://stream-testnet.bybit.com/realtime_private" if mode == "test" else "wss://stream.bybit.com/realtime_private"

# SESSION Activation
session_public = HTTP(api_url)
session_private = HTTP(api_url, api_key=api_key, api_secret=api_secret)
