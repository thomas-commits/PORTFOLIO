# parameters.py
from parameter_arrays.modules_parameter_arrays.population_size import get_population_sizes  # Import population size
from parameter_arrays.modules_parameter_arrays.generations import get_generation_values  # Import generation values

def get_parameters():
    """Fetches necessary parameters for the algorithm."""
    population_sizes = get_population_sizes()  # Fetch the population sizes
    generation_values = get_generation_values()  # Fetch the generation values

    return {
        "population_sizes": population_sizes,
        "generation_values": generation_values
    }
