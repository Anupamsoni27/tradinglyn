import pandas as pd

def filter_data(data_file, num_months, type_to_filter=None):
    """
    Filters bulk and block trade data from a CSV file based on user-specified criteria.

    Args:
        data_file (str): Path to the CSV file containing the data.
        num_months (int): Number of months to filter (e.g., 2 for last 2 months).
        type_to_filter (str, optional): Type of trade to filter for (e.g., "Purchase").

    Returns:
        pandas.DataFrame: The filtered DataFrame containing relevant records.
    """

    try:
        # Read data from CSV file, handling potential format issues
        data = pd.read_csv(data_file, infer_datetime_format=True)

        # Convert 'Date' column to datetime format with error handling
        try:
            data['Date'] = pd.to_datetime(data['Date'])
        except ValueError:
            print("Error: 'Date' column format might be incorrect. Please check and try again.")
            return None

        # Get today's date
        today = pd.to_datetime(pd.Timestamp.today())

        # Calculate the date range dynamically
        two_months_ago = today - pd.DateOffset(months=num_months)

        # Filter data based on date range and type (if specified)
        filtered_data = data[
            (data['Date'] >= two_months_ago) & (data['Date'] <= today)
        ]

        if type_to_filter:
            filtered_data = filtered_data[filtered_data['action type'] == type_to_filter]

        return filtered_data

    except FileNotFoundError:
        print("Error: File not found. Please check the file path and try again.")
        return None

# Get user input for number of months and optional type filter
num_months = 2

def main():
    # Filter data and display results
    filtered_data = filter_data("latest_data.csv", num_months)
    
    if filtered_data is not None:
    
        # filtered_df = pd.DataFrame(filtered_data)
    
        # Create a new column to count the number of purchases for each stock
        filtered_data['buy count'] = filtered_data['stock'].map(filtered_data['stock'].value_counts())
        filtered_data = filtered_data.sort_values(by='stock')
        print(filtered_data)
        filtered_data.to_csv('report.csv', index=False)
    else:
        print("Data processing failed. Please check for errors.")
