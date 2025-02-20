def print_debug_info(tsp_data):
    """Prints debug information to verify that the dataset is correct and accessible."""
    if tsp_data:
        print("=== DEBUG INFORMATION ===")
        print(f"Number of Cities: {tsp_data['dimension']}")
        print(f"Edge Weight Type: {tsp_data['edge_weight_type']}")
        
        