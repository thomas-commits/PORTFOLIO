import logging

# Set up logging configuration
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(message)s')

def log_extracted_values(dimension, weight_limit, profit, weight):
    """
    Logs the extracted values to a debug file.

    :param dimension: Number of items.
    :param weight_limit: Maximum weight limit.
    :param profit: List of profits for each item.
    :param weight: List of weights for each item.
    """
    # Log the extracted values to the debug file
    print(f"Dimension: {dimension}")
    print(f"Weight Limit: {weight_limit}")
    print("Profit values: " + ', '.join(map(str, profit)))
    print("Weight values: " + ', '.join(map(str, weight)))

    return dimension, weight_limit, profit, weight

