import pandas as pd


def calculate_sma(data: pd.DataFrame, window: int = 5) -> pd.DataFrame:
    """
    Calculate Simple Moving Average (SMA).

    Args:
        data (pd.DataFrame): Raw stock data (must include 'Close' column).
        window (int): The rolling window size for SMA calculation.

    Returns:
        pd.DataFrame: DataFrame with an additional 'SMA' column.
    """
    if "Close" not in data.columns:
        raise ValueError("Data must contain 'Close' column")
    data["SMA"] = data["Close"].rolling(window=window).mean()
    return data


def calculate_ema(data: pd.DataFrame, span: int = 10) -> pd.DataFrame:
    """
    Calculate Exponential Moving Average (EMA).

    Args:
        data (pd.DataFrame): Raw stock data (must include 'Close' column).
        span (int): The span for EMA calculation.

    Returns:
        pd.DataFrame: DataFrame with an additional 'EMA' column.
    """
    if "Close" not in data.columns:
        raise ValueError("Data must contain 'Close' column")
    data["EMA"] = data["Close"].ewm(span=span, adjust=False).mean()
    return data


def process_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Process raw stock data by calculating additional metrics.

    Args:
        data (pd.DataFrame): Raw stock data.

    Returns:
        pd.DataFrame: Processed stock data with calculated metrics.
    """
    data = calculate_sma(data, window=5)
    data = calculate_ema(data, span=10)
    return data


if __name__ == "__main__":
    # Example usage
    raw_data = pd.DataFrame(
        {"Close": [100, 102, 104, 103, 105, 107, 109, 111, 110, 112]}
    )
    processed_data = process_data(raw_data)
    print(processed_data)
