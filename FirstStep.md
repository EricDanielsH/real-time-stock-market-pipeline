# Data Flow and Requirements
1.	Yahoo Finance API (via yfinance Python library)
- Fetch stock data from Yahoo Finance at regular intervals (e.g., every minute).
2.	Data Processing (Python)
- Process and format the stock data.
- Optionally, perform technical analysis or transformations (e.g., calculate moving averages).
3.	Kafka Producer (Python)
- Send the processed stock data into Kafka topics for real-time streaming.
4.	Kafka (Real-time Streaming)
- Kafka will act as a message broker, distributing the stock data in real-time to consumers.
5.	Consumer (e.g., Dashboard or Trading System)
- Kafka consumers will retrieve the stock data from Kafka and process/display it (e.g., through a dashboard or trading system).
