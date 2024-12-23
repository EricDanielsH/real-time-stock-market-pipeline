import yfinance as yf

def fetch_stock_data(ticker: str, interval: str = "1m", period: str = "1d"):
    """
    Fetch stock data from Yahoo Finance.

    Args:
        ticker (str): Stock ticker symbol (e.g., "AAPL").
        interval (str): Data interval (e.g., "1m", "5m", "1h", "1d").
        period (str): Data period (e.g., "1d", "5d", "1mo").

    Returns:
        pandas.DataFrame: Stock market data as a DataFrame.
    """
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(interval=interval, period=period)
        print(f"Fetched data for {ticker}: {data.tail(1)}")  # Print the last row as a sample
        return data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    data = fetch_stock_data(ticker="AAPL", interval="1m", period="1d")
    print(data)
