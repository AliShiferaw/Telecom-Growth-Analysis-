# src/data_loader.py

import pandas as pd

def load_csv(file_path):
    """
    Function to load a CSV file into a pandas DataFrame.
    Args:
        file_path (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None
# src/data_loader.py

import pandas as pd

def load_csv(file_path):
    """
    Function to load a CSV file into a pandas DataFrame.
    Args:
        file_path (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        # Load the data
        data = pd.read_csv(file_path)
        
        # Print the first few rows to confirm data is loaded
        print(f"Data loaded successfully from {file_path}")
        print(data.head())  # Print the first few rows of the data
        return data
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None

# Add a test call to load data directly in this script
if __name__ == "__main__":
    # Specify the path to your dataset
    file_path = r"C:\Users\alitr\OneDrive\Desktop\Ten Acadamey\Week Two\Data-20241218T114441Z-001\Data\Copy of Week2_challenge_data_source(CSV).csv"
    
    # Load the CSV file
    load_csv(file_path)
