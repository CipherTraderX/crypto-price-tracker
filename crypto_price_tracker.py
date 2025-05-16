# crypto_price_tracker.py

import requests

def get_price(coin_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data[coin_id]['usd']

coins = ['bitcoin', 'ethereum', 'dogecoin']

print("Live Crypto Prices (USD):")
for coin in coins:
    try:
        price = get_price(coin)
        print(f"{coin.title()}: ${price}")
    except Exception as e:
        print(f"Error fetching {coin}: {e}")
