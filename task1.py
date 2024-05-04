import pandas as pd
import requests
        

class RestClient:
    """
    A class to interact with a REST API.
    """

    def __init__(self, url):
        """
        Initializes the RestClient with the base URL of the API.
    
        Parameters:
        url (str): The base URL of the API.
        """
        self.url = url

    def download_json(self):
        """
        Downloads JSON data from the specified URL.

        Returns:
        dict: The JSON data.
        """
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to download JSON data. Status code: {response.status_code}")
            return None

    def convert_to_dataframe(self, json_data):
        """
        Converts JSON data into a pandas DataFrame.

        Parameters:
        json_data (dict): The JSON data.

        Returns:
        pandas.DataFrame: The DataFrame.
        """
        return pd.DataFrame(json_data)

    def save_to_csv(self, dataframe, filename):
        """
        Saves DataFrame to a CSV file.

        Parameters:
        dataframe (pandas.DataFrame): The DataFrame to be saved.
        filename (str): The name of the CSV file.
        """
        dataframe.to_csv(filename, index=False)
        print(f"Data saved to {filename}")

    def get_info_by_symbol(self, symbol, dataframe):
        """
        Retrieves information by symbol from the DataFrame.

        Parameters:
        symbol (str): The symbol to filter by.
        dataframe (pandas.DataFrame): The DataFrame to search.

        Returns:
        dict: The information corresponding to the symbol, if found.
        """
        filtered_data = dataframe[dataframe['symbol'] == symbol]
        if not filtered_data.empty:
            return filtered_data.iloc[0].to_dict()
        else:
            print(f"No data found for symbol: {symbol}")
            return None

def main():
    # Create an instance of RestClient
    rest_client = RestClient("https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json")

    # Download JSON data
    json_data = rest_client.download_json()

    if json_data:
        # Convert JSON data to DataFrame
        dataframe = rest_client.convert_to_dataframe(json_data)

        # Save DataFrame to CSV
        rest_client.save_to_csv(dataframe, "instruments.csv")

        # Get information by symbol
        symbol = "AAPL"  # Example symbol
        info = rest_client.get_info_by_symbol(symbol, dataframe)
        if info:
            print("Information for symbol", symbol)
            print(info)

if __name__ == "__main__":
    main()
