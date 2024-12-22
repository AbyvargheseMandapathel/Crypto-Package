from crypto_price import CryptoPrice

class CryptoPriceAPIWrapper:
    def __init__(self, api_key: str):
        self.crypto = CryptoPrice(api_key)

    def get_crypto_price(self, symbol: str, convert: str = "USD"):
        """
        Fetch the latest price for a single cryptocurrency.

        :param symbol: The cryptocurrency symbol (e.g., 'BTC', 'ETH')
        :param convert: The currency to convert to (default: USD)
        :return: A user-friendly price result
        """
        result = self.crypto.get_crypto_price(symbol, convert)
        if "error" in result:
            return f"Error: {result['error']}"
        else:
            price = result.get('quote', {}).get(convert, {}).get('price', 'N/A')
            return f"The current price of {symbol} is {price} {convert}."

    def get_multiple_crypto_prices(self, symbols: list, convert: str = "USD"):
        """
        Fetch the latest prices for multiple cryptocurrencies.

        :param symbols: List of cryptocurrency symbols (e.g., ['BTC', 'ETH'])
        :param convert: The currency to convert to (default: USD)
        :return: A dictionary of prices for each cryptocurrency
        """
        result = self.crypto.get_prices(symbols, convert)
        prices = {}
        for symbol, data in result.items():
            if "error" in data:
                prices[symbol] = f"Error: {data['error']}"
            else:
                price = data.get('quote', {}).get(convert, {}).get('price', 'N/A')
                prices[symbol] = price
        return prices
