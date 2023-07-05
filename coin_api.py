import requests
from decouple import config


def crypto_currency_choice(query):
    KEY = config("key")
    url = f"https://rest.coinapi.io/v1/exchangerate/{query}/USD"
    headers = {"X-CoinAPI-Key": KEY}
    response = requests.get(url, headers=headers).json()
    print(round(response["rate"], 2))
