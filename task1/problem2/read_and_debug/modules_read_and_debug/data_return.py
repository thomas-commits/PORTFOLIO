def extract_values(raw_data):
    """Extract meaningful values like dimension, weight limit, profit, and weight from the raw data."""
    # Read first two values
    dimension = int(raw_data[0].strip())  # Number of items
    weight_limit = int(raw_data[1].strip())  # Maximum allowed weight

    profit = []
    weight = []

    # Read the remaining values and extract profit and weight
    for line in raw_data[2:]:  # Skip first two lines
        values = line.split()
        if len(values) == 2:
            profit.append(int(values[0]))  # Left value is profit
            weight.append(int(values[1]))  # Right value is weight

    return dimension, weight_limit, profit, weight
