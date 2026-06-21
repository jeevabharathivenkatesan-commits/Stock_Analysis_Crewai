import yfinance as yf
from crewai.tools import tool

@tool("Live stock information tool")
def get_stock_price(stock_symbol: str) ->str:
    """
        Retrieves the latest stock price and other relevant info for a given stock symbol using Yahoo Finance.

        Parameters:
            stock_symbol (str): The ticker symbol of the stock (e.g., AAPL, TSLA, MSFT).

        Returns:
            str: A summary of the stock's current price, daily change, and other key data.
        """
    stock=yf.Ticker(stock_symbol)
    info=stock.info

    current_price=info.get('regularMarketPrice')
    chagne=info.get('regularMarketChange')
    change_percentage=info.get('regularMarketChangePercent')
    currency=info.get('currency','USD')

    if current_price is None:
        return f"could not retrieve price for {stock_symbol}"

    return (
        f"Stock: {stock_symbol.capitalize()}\n"
        f"Price:{current_price},{currency}\n"
        f"Change:{chagne},({round(change_percentage, 2)}%)"
    )
#print(get_stock_price('AAPL'))