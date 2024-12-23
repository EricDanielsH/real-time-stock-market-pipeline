import time
import schedule
from fetch_data import fetch_stock_data


def job():
    """
    Job to fetch and process stock data periodically.
    """
    ticker = "AAPL"
    interval = "1m"
    period = "1d"
    data = fetch_stock_data(ticker=ticker, interval=interval, period=period)
    # You can add additional processing or saving logic here
    if data is not None:
        print(f"Data fetched and processed for {ticker}")


def schedule_fetch():
    """
    Schedules the fetch job to run periodically.
    """
    schedule.every(1).minute.do(job)  # Schedule the job to run every minute

    print("Scheduler started. Press Ctrl+C to exit.")
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    schedule_fetch()
