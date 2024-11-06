price_guide = {
    "Common Shiny Pokémon with No Collector Interest": {
        "Value": "~40k",
        "Examples": ["L8 Kabuto 40K ID: 1278055", "L8 Pidove 41K ID: 1278064"]
     },
    "Common Mint Shiny": {
        "Value": "120k - 140k",
        "Examples": ["L1 Scatterbug 121K ID: 1276710","L1 Gigalith 125K ID: 1275993"]
    },
    "Common, But Collector Interest Shiny Pokémon": {
        "Value": "Fluctuates.",
        "Examples": ["L7 Eevee 1.99M ID: 1276166", "L40 Ralts 200K ID: 1275594","L26 Alcremie 515K ID: 1278043"]
    },
    "Rare Shinies": {
        "Value": "Varies, can usually go for much more than 1M.",
        "Examples": ["L29 Arceus 3.55M ID: 1180602", "L13 Mew 9.45M ID: 1277044", "L18 Pride Mew 96M ID: 1259645", "L20 Mega Rayquaza 6.5M ID: 1274367", "L28 Koraidon 5.4M ID: 1275491"]
    },
    "Special Forms Shinies": {
        "Value": "Differs.",
        "Examples": ["L17 Partner Pikachu 5.56M ID: 1273924", ]
    },
    "Event Shinies": {
        "Value": "Usually not too much, but varies.",
        "Examples": ["L25 Relay Race Raboot 315K ID: 1278100", "L13 Autumn Chikorita 400K ID: 1276893", "L25 Bird Nest Nuzleaf 280K ID: 1256105"]
    },
    "Multiple Features": {
        "Value": "Can get insane.",
        "Examples": ["L29 Shiny Ice Yveltal 132M ID: 817455", "L68 Primal Glastrier 18M ID: 528646", "L100 Shadow Mewtwo 14M ID: 212309"]
    },
}

def format_price_guide():
    global price_guide
    """Formats the price guide into a Discord message."""
    response = "### Price Guide for Shiny Pokémon\n\n"
    
    for category, details in price_guide.items():
        response += f"**{category}**\n"
        
        if isinstance(details, dict):
            # Check if it's a value with examples
            if "Value" in details and "Examples" in details:
                response += f" - **Value**: {details['Value']}\n"
                response += " - **Examples**:\n"
                for example in details["Examples"]:
                    response += f"   - {example}\n"
            else:
                # If it's just a value with examples
                response += f" - **Value**: {details['Value']}\n"
                response += " - **Examples**:\n"
                for example in details["Examples"]:
                    response += f"   - {example}\n"

        response += "\n"  # Add a line break between categories
    
    return response