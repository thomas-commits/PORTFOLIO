from read_and_debug.modules_read_and_debug.read import read_dataset
from read_and_debug.modules_read_and_debug.data_return import extract_values
from read_and_debug.modules_read_and_debug.debug import log_extracted_values

FILE_PATH = r"C:\Users\thoma\Desktop\Root\Skole og jobb\vår25\ACIT4610\portfolio\task1\problem2\s006.kp"

def read_and_debug():
    # Read raw data from the file
    raw_data = read_dataset(FILE_PATH)
    
    if raw_data:  # Check if data is successfully read
        # Debug output to see the raw data content
        print("Raw data read from file:")
        print(raw_data)
        
        # Strip leading/trailing whitespace and remove empty lines
        raw_data = [line.strip() for line in raw_data if line.strip()]

        # Debug output after cleaning the data
        print("Cleaned raw data (after removing empty lines):")
        print(raw_data)

        # Extract the values using extract_values function
        dimension, weight_limit, profit, weight = extract_values(raw_data)

        # Debug output to verify that profit and weight are correctly populated
        print(f"Extracted profit: {profit[:5]}")  # Show first 5 values
        print(f"Extracted weight: {weight[:5]}")  # Show first 5 values
        print(f"Total dimension: {dimension}")
        print(f"Weight limit: {weight_limit}")

        # Return the extracted values to be used in the genetic algorithm
        return dimension, weight_limit, profit, weight
    else:
        print("Error: No data read.")
        return None
