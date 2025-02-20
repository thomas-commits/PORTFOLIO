def read_dataset(file_path):
    """Reads the dataset from the given file path."""
    try:
        with open(file_path, "r") as file:
            data = file.readlines()
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
