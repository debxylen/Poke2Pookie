import battle_instruct as batinst
import requests
import re
from utils import *
from battle_instruct import *

def extract_embed_fields(embed):
    # Add all fields, if any
    fields = []
    for field in embed.fields:
        fields.append({field.name:field.value})
    return fields


def get_pokemon_type(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
    if response.status_code == 200:
        pokemon_data = response.json()
        # Extract types
        types = [t['type']['name'] for t in pokemon_data['types']]
        return types
    return None

def info_title(text):
    pattern = r'^Level\s(\d+)\s+([A-Z][a-z]*(?:\s[A-Z][a-z]*)*)(?:\s+"([^"]+)"|\s*)?'
    match = re.match(pattern, text)
    if match:
        level = match.group(1)
        name = match.group(2)
        nickname = match.group(3) if match.group(3) else None
        return level, name, nickname
    return None


# Function to check type advantage
def type_advantage(pokemon_name, opponent_name):
    """
    Check if the Pokémon has a type advantage over the opponent using the PokéAPI.
    """
    def get_type_data(type_name):
        response = requests.get(f"https://pokeapi.co/api/v2/type/{type_name}")
        if response.status_code == 200:
            return response.json()
        return None

    # Get types for both Pokémon
    pokemon_types = get_pokemon_type(pokemon_name)
    opponent_types = get_pokemon_type(opponent_name)

    if pokemon_types is None or opponent_types is None:
        print("Error retrieving Pokémon type data.")
        return False

    # Check for type advantages
    for pokemon_type in pokemon_types:
        type_data = get_type_data(pokemon_type)
        if type_data is None:
            print(f"Error retrieving type data for {pokemon_type}.")
            continue
        
        # Check if the Pokémon type has double damage to any of the opponent types
        double_damage_to = [t['name'] for t in type_data['damage_relations']['double_damage_to']]
        if any(opponent_type in double_damage_to for opponent_type in opponent_types):
            return [True, pokemon_types, opponent_types]
    
    return [False, pokemon_types, opponent_types]

# Extract stats from the PokéTwo embed's plain text
def extract_stats_from_plaintext(embed):
    stats = {}
    
    # Use regex to extract different stats
    hp_match = re.search(r'\*\*HP:\*\*\s+(\d+)\s+–\s+IV:\s+(\d+)/31', embed)
    attack_match = re.search(r'\*\*Attack:\*\*\s+(\d+)\s+–\s+IV:\s+(\d+)/31', embed)
    defense_match = re.search(r'\*\*Defense:\*\*\s+(\d+)\s+–\s+IV:\s+(\d+)/31', embed)
    sp_atk_match = re.search(r'\*\*Sp\.\sAtk:\*\*\s+(\d+)\s+–\s+IV:\s+(\d+)/31', embed)
    sp_def_match = re.search(r'\*\*Sp\.\sDef:\*\*\s+(\d+)\s+–\s+IV:\s+(\d+)/31', embed)
    speed_match = re.search(r'\*\*Speed:\*\*\s+(\d+)\s+–\s+IV:\s+(\d+)/31', embed)
    iv_match = re.search(r'\*\*Total IV:\*\*\s+(\d+\.\d+)%', embed)

    # If the matches are found, store them in the stats dictionary
    if hp_match:
        stats["hp"] = int(hp_match.group(1))
        stats["hp_iv"] = int(hp_match.group(2))
    if attack_match:
        stats["attack"] = int(attack_match.group(1))
        stats["attack_iv"] = int(attack_match.group(2))
    if defense_match:
        stats["defense"] = int(defense_match.group(1))
        stats["defense_iv"] = int(defense_match.group(2))
    if sp_atk_match:
        stats["sp_atk"] = int(sp_atk_match.group(1))
        stats["sp_atk_iv"] = int(sp_atk_match.group(2))
    if sp_def_match:
        stats["sp_def"] = int(sp_def_match.group(1))
        stats["sp_def_iv"] = int(sp_def_match.group(2))
    if speed_match:
        stats["speed"] = int(speed_match.group(1))
        stats["speed_iv"] = int(speed_match.group(2))
    if iv_match:
        stats["total_iv"] = float(iv_match.group(1))
    
    return stats

def extract_nature(text):
    match = re.search(r'\*\*Nature:\*\* ([^\n]+)', text)
    return match.group(1) if match else None

def get_instructions(your_pokemon, opponent):
    your_pokemon = your_pokemon.title()
    opponent = opponent.title()
    if your_pokemon in batinst.battle_instructions:
        instructions = batinst.battle_instructions[your_pokemon]
        wins = instructions.get("wins", {}).get(opponent, "0")
        loses = instructions.get("loses", {}).get(opponent, "0")
        conditional = instructions.get("conditional", {}).get(opponent, "0")
        
        return {
            "wins": wins,
            "loses": loses,
            "conditional": conditional
        }
    else:
        return "0"

def extract_pokemon_index(text):
    pattern = r'pokémon (\d+)'
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    return None 



def recommend_best_team(user_id, opponent_team):
    data = load_pokemon_data_from_file()
    user_id = str(user_id)
    if user_id not in data:
        print("User not found in data.")
        return []

    user_pokemons = data[user_id]
    points = {}
    
    for pokemon_index, your_pokemon in user_pokemons.items():
        total_points = 0
        for opponent in opponent_team:
            instructions = get_instructions(your_pokemon['name'], opponent)
            if instructions == "0":
                continue
            # Count wins and conditionals as points
            if not instructions["wins"]=="0":
                total_points += 1
            if not instructions["conditional"]=="0":
                total_points += 0.5

        # Store the total points for this Pokémon
        points[your_pokemon['name']] = total_points

    # Sort Pokémon by total points and recommend the top 3
    sorted_pokemons = sorted(points.items(), key=lambda x: x[1], reverse=True)
    recommended_pokemon = [pokemon[0] for pokemon in sorted_pokemons[:3]]  # Get names of the top 3
    return [recommended_pokemon, points]


def move_against_team(recommended_team, opponent_team):
    # This will store the moves/instructions for each Pokémon against the opponent's team
    all_moves = {}

    # Iterate through each recommended Pokémon
    for your_pokemon in recommended_team:
        pokemon_moves = {}  # To store the moves against each opponent

        # Loop through the opponent team and get instructions for each opponent
        for opponent in opponent_team:
            instructions = get_instructions(your_pokemon, opponent)

            # Check if the result is a win or conditional (not a loss)
            if (not instructions["wins"] == "0") or (not instructions["conditional"] == "0"):
                # Store the move only if it's a win or conditional
                instructionss = {}
                for i in instructions:
                    if not instructions[i]=="0":
                        instructionss[i]=instructions[i]
                pokemon_moves[opponent] = instructionss

        # Only store this Pokémon's moves if it has valid moves (non-losing)
        if pokemon_moves:
            all_moves[your_pokemon] = pokemon_moves

    return all_moves





def add_recommendations_to_embed(embed, user_id, opponent_team):
    recommended_team = recommend_best_team(str(user_id),opponent_team)[0]
##    pointss = recommend_best_team(str(user_id),opponent_team)[-1]
##    points = {}
##    for k,v in pointss.items():
##        if not str(v)=="0":
##            points[k]=v
    recommendations_dict = move_against_team(recommended_team, opponent_team)
    for opponent in opponent_team:
        # Start building the field value
        field_value = ""
        
        # Loop through each opponent and their respective instructions (wins/conditional)
        for pokemon, details in recommendations_dict.items():
            # Get win/conditional information
            if not opponent in details:
                continue
            if 'wins' in details[opponent]:
                move_info = details[opponent]['wins']
                field_value += f"**{pokemon}**: {move_info}\n"  # Bold the opponent name
            elif 'conditional' in details[opponent]:
                move_info = details[opponent]['conditional']
                field_value += f"**{pokemon}** (Conditional): {move_info}\n"
        
        # Add the Pokémon and its moves against opponents as a new field in the embed
        if field_value:  # Only add if there's something to show
            embed.add_field(name=f"# Against Opponent's *{opponent}*", value=field_value, inline=False)
            embed.add_field(name="",value="\n\n", inline = False)
    embed.description = ", ".join(recommended_team)
    return embed



def add_all_recommendations_to_embed(embed, user_id, opponent_team):
    pointss = recommend_best_team(str(user_id),opponent_team)[-1]
    points = {}
    for k,v in pointss.items():
        if not str(v)=="0":
            points[k]=v
    recommended_team = points.keys()
    recommendations_dict = move_against_team(recommended_team, opponent_team)
    for opponent in opponent_team:
        # Start building the field value
        field_value = ""
        
        # Loop through each opponent and their respective instructions (wins/conditional)
        for pokemon, details in recommendations_dict.items():
            # Get win/conditional information
            if not opponent in details:
                continue
            if 'wins' in details[opponent]:
                move_info = details[opponent]['wins']
                field_value += f"**{pokemon}**: {move_info}\n"  # Bold the opponent name
            elif 'conditional' in details[opponent]:
                move_info = details[opponent]['conditional']
                field_value += f"**{pokemon}** (Conditional): {move_info}\n"
        
        # Add the Pokémon and its moves against opponents as a new field in the embed
        if field_value:  # Only add if there's something to show
            embed.add_field(name=f"# Against Opponent's *{opponent}*", value=field_value, inline=False)
            embed.add_field(name="",value="\n\n", inline = False)
    embed.description = ", ".join(points.keys())
    return embed
    


# Function to recommend IVs for a given Pokémon based on its current IVs
def recommend_stats(pokemon_name):
    pokemon_name = pokemon_name.title()  # Ensure capitalization matches dictionary keys
    if pokemon_name not in iv_requirements:
        return f"Sorry, IV recommendations for {pokemon_name} are not available."
    
    requirements = iv_requirements[pokemon_name]
    return requirements


