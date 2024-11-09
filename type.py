import requests, json

with open('all_types.json') as file:
    all_types = json.load(file)
    
# Function to get types from PokéAPI
def get_pokemon_types_from_api(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
    if response.status_code != 200:
        print("Error: Could not retrieve Pokémon data.")
        return None
    data = response.json()
    return [t['type']['name'] for t in data['types']]


def get_multipliers(types):
    multipliers = {
        'defense': {},
        'attack': {}
    }
    
    for type_ in types:
        damage_relations = all_types[type_]
        no_damage_to = damage_relations['attack']['zero']
        no_damage_from = damage_relations['defense']['zero']
        half_damage_to = damage_relations['attack']['half']
        half_damage_from = damage_relations['defense']['half']
        double_damage_to = damage_relations['attack']['double']
        double_damage_from = damage_relations['defense']['double']
        
        for t in no_damage_to:
            if t in multipliers['attack']:
                multipliers['attack'][t] *= 0
            else:
                multipliers['attack'][t] = 0
                
        for t in no_damage_from:
            if t in multipliers['defense']:
                multipliers['defense'][t] *= 0
            else:
                multipliers['defense'][t] = 0
                
        for t in half_damage_to:
            if t in multipliers['attack']:
                multipliers['attack'][t] *= 0.5
            else:
                multipliers['attack'][t] = 0.5
                
        for t in half_damage_from:
            if t in multipliers['defense']:
                multipliers['defense'][t] *= 0.5
            else:
                multipliers['defense'][t] = 0.5
                
        for t in double_damage_to:
            if t in multipliers['attack']:
                multipliers['attack'][t] *= 2
            else:
                multipliers['attack'][t] = 2
                
        for t in double_damage_from:
            if t in multipliers['defense']:
                multipliers['defense'][t] *= 2
            else:
                multipliers['defense'][t] = 2
                
    return multipliers


# Function to format the type info
def format_type_info(pokemon_name):
    types = get_pokemon_types_from_api(pokemon_name)
    if not types:
        return f"Could not retrieve types for {pokemon_name}."

    multipliers = get_multipliers(types)
    
    weaknesses = {}
    resistances = {}
    immunities = []

    for type_name, multiplier in multipliers['defense'].items():
        print(type_name, multiplier)
        if multiplier > 1:
            weaknesses.setdefault(multiplier, []).append(type_name)
        elif multiplier < 1 and multiplier > 0:
            resistances.setdefault(multiplier, []).append(type_name)
        elif multiplier == 0:
            immunities.append(type_name)
    
    formatted_info = f"**{pokemon_name.capitalize()} type info**\n"
    formatted_info += f"**type**: {', '.join(types)}\n"
    
    # Weaknesses
    for mult, types in weaknesses.items():
        formatted_info += f"**weakness {mult}x**: {', '.join(types)}\n"
    
    # Resistances
    for mult, types in resistances.items():
        formatted_info += f"**resistance 1/{1/mult:.0f}**: {', '.join(types)}\n"
    
    # Immunities
    if immunities:
        formatted_info += f"**immunity**: {', '.join(immunities)}\n"
    
    formatted_info += "\n||by zzyxin||"
    
    return formatted_info

while True:
    print(format_type_info(input(">>> ")))
