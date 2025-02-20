import math

def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculate the great-circle distance between two points using the Haversine formula."""
    R = 6371  # Earth's radius in kilometers
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])  # Convert degrees to radians

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c  # Returns distance in kilometers

def compute_distance_matrix(coordinates):
    """Compute a distance matrix for a given list of (lat, lon) coordinates."""
    num_cities = len(coordinates)
    distance_matrix = [[0] * num_cities for _ in range(num_cities)]  # Initialize matrix

    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                lat1, lon1 = coordinates[i]
                lat2, lon2 = coordinates[j]
                distance_matrix[i][j] = haversine_distance(lat1, lon1, lat2, lon2)
            else:
                distance_matrix[i][j] = 0  # Distance to itself is always 0

    return distance_matrix

def evaluate_population(population, distance_matrix):
    """
    Evaluate a population by computing the total travel distance for each chromosome.
    
    :param population: List of chromosomes (each chromosome is a list of city indices).
    :param distance_matrix: Precomputed matrix with distances between all cities.
    :return: List of tuples (chromosome, total_distance) sorted by best fitness (lowest distance).
    """
    evaluated_population = []
    
    for chromosome in population:
        total_distance = sum(
            distance_matrix[chromosome[i]][chromosome[i + 1]]
            for i in range(len(chromosome) - 1)
        )
        # Add distance from last to first city to complete the tour
        total_distance += distance_matrix[chromosome[-1]][chromosome[0]]

        evaluated_population.append((chromosome, total_distance))

    # Sort the population by fitness (shorter distance is better)
    evaluated_population.sort(key=lambda x: x[1])
    
    return evaluated_population
