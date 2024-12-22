import requests
import json

class CryptoPrice:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
        self.headers = {
            "X-CMC_PRO_API_KEY": self.api_key,
            "Accept": "application/json"
        }

    def get_crypto_price(self, symbol: str, convert: str = "INR"):
        """
        Fetch the latest price of a cryptocurrency.

        :param symbol: The cryptocurrency symbol (e.g., 'BTC', 'ETH', etc.)
        :param convert: The currency to convert to (default: INR)
        :return: A dictionary with cryptocurrency data or an error message
        """
        params = {
            "start": "1",  # Fetch from the first cryptocurrency (optional)
            "limit": "10",  # Limit the response to top 10 cryptos (optional)
            "convert": convert,  # Set currency to INR
        }

        # Make request to fetch data
        response = self._make_request(params)

        if response:
            # Loop through all cryptocurrencies to find the one matching the symbol
            for crypto in response.get("data", []):
                if crypto["symbol"] == symbol:
                    return crypto  # Return the data of the cryptocurrency
            return {"error": f"{symbol} not found."}
        else:
            return {"error": "Failed to retrieve data from CoinMarketCap."}

    def _make_request(self, params):
        """
        Make an API request to CoinMarketCap.

        :param params: The query parameters for the API request
        :return: Parsed JSON response if the request was successful
        """
        try:
            response = requests.get(self.base_url, headers=self.headers, params=params)  # Pass params here
            print(response.url)  # To see the full URL including params
            response.raise_for_status()  # Raise HTTPError for bad responses
            data = response.json()
            return data  # Return the raw data
        except requests.exceptions.RequestException as e:
            print(f"Error during API request: {e}")
            return None
