import yfinance as yf
import pandas as pd
import pandas_ta as ta

class StockDataAnalyzer:
    """
    A class to analyze stock data.
    """

    def __init__(self, ticker):
        """
        Initializes the StockDataAnalyzer with the ticker symbol.

        Parameters:
        ticker (str): The ticker symbol of the stock.
        """
        self.ticker = ticker

    def download_data(self):
        """
        Downloads OHLCV data of the specified ticker using yfinance.

        Returns:
        pandas.DataFrame: OHLCV data.
        """
        data = yf.download(self.ticker)
        return data

    def preprocess_data(self, data):
        """
        Preprocesses the downloaded data.

        Parameters:
        data (pandas.DataFrame): OHLCV data.

        Returns:
        pandas.DataFrame: Preprocessed data.
        """
        # Rename columns to lowercase
        data.columns = map(str.lower, data.columns)

        # Round columns to 2 decimal points
        data = data.round(2)

        # Add 'color' column based on open and close prices
        data['color'] = ['GREEN' if o <= c else 'RED' for o, c in zip(data['open'], data['close'])]

        # Calculate EMA with length of 9
        data['ema'] = ta.ema(data['close'], length=9)

        return data

    def save_to_csv(self, data):
        """
        Saves DataFrame to a CSV file with the ticker name.

        Parameters:
        data (pandas.DataFrame): The DataFrame to be saved.
        """
        filename = f"{self.ticker}.csv"
        data.to_csv(filename)
        print(f"Data saved to {filename}")

def main():
    # Choose a ticker symbol
    ticker = "NVDA"  # Example ticker

    # Create an instance of StockDataAnalyzer
    analyzer = StockDataAnalyzer(ticker)

    # Download data
    data = analyzer.download_data()

    if not data.empty:
        # Preprocess data
        preprocessed_data = analyzer.preprocess_data(data)

        # Save to CSV
        analyzer.save_to_csv(preprocessed_data)

if __name__ == "__main__":
    main()
