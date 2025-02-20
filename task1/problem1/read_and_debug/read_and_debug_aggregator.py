from read_and_debug.modules_read_and_debug.read import read_dataset
from read_and_debug.modules_read_and_debug.data_return import extract_values
from read_and_debug.modules_read_and_debug.debug import print_debug_info

FILE_PATH = r"C:\Users\thoma\Desktop\Root\Skole og jobb\vår25\ACIT4610\portfolio\task1\problem1\burma14.tsp"

def read_and_debug():
    """Reads the dataset, processes the values, and returns structured data."""
    raw_data = read_dataset(FILE_PATH)
    
    if raw_data:
        # Extract values from dataset
        dimension, latitudes, longitudes, edge_weight_type = extract_values(raw_data)
        
        # Convert latitudes & longitudes into a list of coordinate tuples
        coordinates = list(zip(latitudes, longitudes))  
        
        # Print debug info
        print_debug_info({
            "dimension": dimension,
            "coordinates": coordinates,
            "edge_weight_type": edge_weight_type
        })

        # Return a list of (lat, lon) tuples and metadata
        return dimension, coordinates, edge_weight_type  

    else:
        print("Failed to read the dataset.")
        return None
