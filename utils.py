import json

# Function to save Pokémon data to a file
def save_pokemon_data_to_file(data, filename='info_logs.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Function to load Pokémon data from a file
def load_pokemon_data_from_file(filename='info_logs.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file doesn't exist







