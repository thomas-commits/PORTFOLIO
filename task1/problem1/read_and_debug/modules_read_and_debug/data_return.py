def extract_values(raw_data):
    """
    Processes the raw data to extract meaningful values:
    DIMENSION, EDGE_WEIGHT_TYPE, and coordinates (latitude, longitude).
    Returns structured data (dimension, latitudes, longitudes, edge_weight_type).
    """
    coordinates = []
    latitudes = []
    longitudes = []
    dimension = 0
    edge_weight_type = None
    is_node_section = False

    for line in raw_data:
        line = line.strip()

        # Extract DIMENSION
        if line.startswith("DIMENSION"):
            dimension = int(line.split(":")[1].strip())

        # Extract EDGE_WEIGHT_TYPE
        elif line.startswith("EDGE_WEIGHT_TYPE"):
            edge_weight_type = line.split(":")[1].strip()

        # Identify the start of NODE_COORD_SECTION
        elif line.startswith("NODE_COORD_SECTION"):
            is_node_section = True
            continue

        # End of file, stop reading
        elif line.startswith("EOF"):
            break

        # Process coordinates
        if is_node_section:
            parts = line.split()
            if len(parts) == 3:  # Format: index, latitude, longitude
                latitude = float(parts[1])
                longitude = float(parts[2])
                latitudes.append(latitude)
                longitudes.append(longitude)
                coordinates.append((latitude, longitude))

    # Return structured data
    return dimension, latitudes, longitudes, edge_weight_type


