iv_requirements = {
    "Arceus": "16+ hp , 17+ def , 20+ sp.atk , 31 speed",
    "Mega Mewtwo X": "22+ hp , 21+ def , 22+ sp.def , 31 speed",
    "Mega Mewtwo Y": "31 speed , 25+ hp , 26+ def , 10+ sp.atk",
    "Yveltal": "23+ hp, 20+ atk, 22+ def, 20+ spd",
    "Mega Rayquaza": "14+ Hp, 14+ Def, 31 Speed, recommend 25+ Hp and 25+ Def",
    "Primal Groudon": "22+ Hp, 8+ Atk, 11+ Def, 0+ Sp. Atk, 23+ Sp. Def, 31 Speed",
    "Primal Kyogre": "31 Speed, 24+ Hp, 24+ Def, 10+ Sp. Atk, 8+ Sp. Def",
    "Dialga": "18+ Hp, 0+ Def, 20+ Sp. Atk, 19+ Sp. Def 31 Speed",
    "Xerneas": "15+ hp, 25+ atk, 10+ def, 15+ spdef, 31+ speed",
    "Eternatus": "25+ hp, 20+ spatk, 31 spd, 26+ def/spdef",
    "Palkia": "12+ hp, 23+ spatk, 11+ def/spdef, 31 spd",
    
}


battle_instructions = {
    "Mega Mewtwo Y": {
        "wins": {
            "Mega Mewtwo X": "Wins via Future Sight spam",
            "Primal Kyogre": "Wins via Future Sight spam",
            "Zekrom": "Wins via Future Sight spam",
            "Marshadow": "Wins via Future Sight spam",
            "Ho-oh": "Wins via Future Sight spam",
            "Landorus": "Wins via Future Sight spam",
            "Diancie": "Wins via Future Sight spam",
            "Dialga": "Wins via Aura Sphere spam",
        },
        "loses": {
            "Mega Rayquaza": "Loses via 2KO",
            "Magearna": "Loses via 2KO",
            "Solgaleo": "Loses via 2KO",
            "Lunala": "Loses via 2KO",
            "Lugia": "Loses via 2KO",
            "Zygarde": "Loses via 2KO",
            "Yveltal": "Loses via Ohko",
            "Regigigas": "Loses via Ohko",
            "Giratina": "Loses via Ohko",
            "Primal Groudon": "Loses without 25+ HP and 26+ Defense",
            "Xerneas": "Loses to Adamant no matter what"
        },
        "conditional": {
            "Kyurem": "Loses if Glaciate then Outrage. Wins via Future Sight 2KO if not",
            "Arceus": "Depends on Arceus' Atk and SpAtk. Mewtwo should win via Future Sight 2KO. Arceus is weak to fighting so use aura sphere if you want to use type advantage.",
            "Mega Mewtwo Y": "50/50 chance, depends on who sends the challenge first"
        }
    },
    "Arceus": {
        "wins": {
            "Mega Rayquaza": "Wins via Hyper Beam Spam",
            "Primal Groudon": "Wins via Hyper Beam Spam",
            "Xerneas": "Wins via Hyper Beam Spam",
            "Yveltal": "Wins via Hyper Beam Spam",
            "Regigigas": "Wins via Hyper Beam Spam",
            "Zekrom": "Wins via Hyper Beam Spam",
            "Lugia": "Wins via Hyper Beam Spam",
            "Kyurem": "Wins via Hyper Beam Spam",
            "Zygarde": "Wins via Hyper Beam Spam",
            "Dialga": "Wins via Earth Power Spam",
            "Magearna": "Wins via Earth Power Spam",
            "Solgaleo": "Wins via Earth Power Spam",
            "Diancie": "Wins via Earth Power Spam",
            "Landorus": "Wins via Hyper Beam then Extreme Speed"
        },
        "loses": {
            "Primal Kyogre": "Loses via 2KO+",
            "Lunala": "Loses via 2KO+",
            "Zacian": "Might lose to fast Zacian but use Hyper Beam spam then Extreme speed when you are on very low HP",
            "Ho-oh": "Loses via 2KO+",
            "Marshadow": "Loses via 2KO+",
            "Mega Mewtwo Y": "Most likely you will lose this fight but do Hyper Beam then Extreme Speed",
            "Mega Mewtwo X": "The higher your SpAtk, the higher Mewtwo's bulk has to be to beat you. Use Hyper Beam then Extreme Speed"
        },
        "conditional": {
            "Mega Mewtwo Y": "Most likely you will lose this fight but do Hyper Beam then Extreme Speed",
            "Mega Mewtwo X": "The higher your SpAtk, the higher Mewtwo's bulk has to be to beat you. Use Hyper Beam then Extreme Speed"
        }
    },
    "Mega Rayquaza": {
        "wins": {
            "Eternatus": "Wins via Outrage Ohko or 2KO (considering decent stats on rayquaza, dragon is super effective to dragon)",
            "Zekrom": "Wins via Outrage Ohko",
            "Kyurem": "Wins via Outrage Ohko but don't switch to Rayquaza if opponent is using kyogre (rayquaza is 4x weak to ice beam)",
            "Giratina": "Wins via Outrage 2KO",
            "Lunala": "Wins if jolly via Crunch Ohko",
            "Yveltal": "Wins via Dragon Ascent + Extreme Speed",
            "Ho-oh": "Wins via Outrage 2KO",
            "Lugia": "Wins via Outrage 2KO",
            "Landorus": "Wins via Outrage 2KO",
            "Marshadow": "Wins via Fly Ohko",
            "Zacian": "Wins via dragon ascent then extreme speed",
            "Mega Mewtwo Y": "Wins via Outrage then Extreme Speed",
            "Mega Mewtwo X": "Wins via Fly then Extreme Speed",
            "Primal Groudon": "Wins via Double Outrage then Extreme Speed",
            "Lunala": "Wins via Crunch Ohko",
            "Zygarde": "Wins via Outrage 2KO if Ray has 10+ Hp and 11+ Def vs Jolly Zygarde",
            "Shadow Rider Calyrex": "Wins via Crunch"
        },
        "loses": {
            "Magearna": "Loses via Ohko",
            "Regigigas": "Loses via Ohko",
            "Dialga": "Loses via Ohko",
            "Primal Kyogre": "Loses via Ohko",
            "Diancie": "Loses via Ohko",
            "Arceus": "Loses via 2KO",
            "Xerneas": "Loses via Moonblast 2KO but use extreme speed"
        },
        "conditional": {
            "Mega Rayquaza": "Whoever sends the battle will win via Outrage Ohko, assuming you have max speed and Jolly mint"
        }
    },

    "Adamant Yveltal": {
        "wins": {
            "Mewtwo Y": "Wins via Sucker Punch spam",
            "Lugia": "Wins via Sucker Punch spam",
            "Giratina": "Wins via Sucker Punch spam",
            "Solgaleo": "Wins via Sucker Punch spam",
            "Lunala": "Wins via Sucker Punch spam",
            "Mewtwo X": "Wins via Sky Attack spam",
            "Ho-Oh": "Wins via Sky Attack spam",
            "Zacian": "Wins via Sky Attack spam",
            "Zygarde": "Wins via Sky Attack spam",
            "Landorus": "Wins via Sky Attack spam",
            "Marshadow": "Wins via Sky Attack spam",
            "Primal Kyogre": "Wins via Sky Attack + Sucker Punch"
        },
        "loses": {
            "Xerneas": "Adamant: Always loses, \nJolly: Depends on who sends; wins via Sky Attack 2KO if it does",
            "Primal Groudon": "Loses via 2KO+",
            "Dialga": "Loses via 2KO+",
            "Regigigas": "Loses via 2KO+",
            "Arceus": "Loses via 2KO+",
            "Zeroara": "Loses via 2KO+",
            "Kyurem": "Loses via 2KO+",
            "Zekrom": "Loses via Ohko",
            "Diancie": "Loses via Ohko",
            "Magearna": "Use Snarl first to prevent you from the Ohko"
        },
        "conditional": {
            "Xerneas": "Adamant: Always loses, \nJolly: Depends on who sends; wins via Sky Attack 2KO if it does",
            "Mega Rayquaza": "ADAMANT YVELTAL Beats Jolly Rayquaza via Sky Attack + Sucker Punch (Loses to Adamant Rayquaza) (Can tank max atk outrage + extreme speed)"
        }
    },
}


battle_instructions["Primal Groudon"] = {
    "wins": {
        "Zacian": "Wins Via Precipice Blades Ohko",
        "Yveltal": "Wins via Eruption Spam",
        "Magearna": "Wins via Eruption Spam",
        "Solgaleo": "Wins via Eruption Spam",
        "Dialga": "Wins via Precipice Blades Spam",
        "Xerneas": "Wins via Precipice Blades Spam",
        "Marshadow": "Wins via Precipice Blades Spam",
        "Zekrom": "Wins via Precipice Blades Spam",
        "Diancie": "Wins via Precipice Blades Spam",
        "Regigigas": "Wins via Hammer Arm Spam",
        "Arceus": "Wins via Hammer Arm Spam",
        "Kyurem": "Wins via Hammer Arm Spam",
        "Crowned Zacian": "Wins via Eruption Ohko",
        "Mega Mewtwo X": "Wins via Hammer Arm then Precipice Blades",
        "Mega Mewtwo Y": "Wins via Hammer Arm then Precipice Blades"
    },
    "loses": {
        "Mega Rayquaza": "Loses via 2KO+",
        "Lunala": "Loses via 2KO+",
        "Ho-oh": "Loses via 2KO+",
        "Zygarde": "Loses via 2KO+",
        "Lugia": "Loses via Ohko"
    },
    "conditional": {
        "Primal Kyogre": "May lose via Ohko, but use Precipice Blades",
        "Giratina": "Depends on who sends first, use Precipice Blades"
    }
}

battle_instructions["Primal Kyogre"] = {
    "wins": {
        "Mega Mewtwo X": "Wins via Water Spout Spam",
        "Primal Groudon": "Wins via Water Spout Spam",
        "Magearna": "Wins via Water Spout Spam",
        "Marshadow": "Wins via Water Spout Spam",
        "Lunala": "Wins if timid via Water Spout 2KO+",
        "Solgaleo": "Wins via Water Spout Spam",
        "Lunala": "Wins via Water Spout Spam if timid",
        "Ho-oh": "Wins via Water Spout Spam",
        "Landorus": "Wins via Water Spout Spam",
        "Diancie": "Wins via Water Spout Spam",
        "Mega Rayquaza": "Wins via Ice Beam Spam",
        "Zygarde": "Wins via Ice Beam Spam",
        "Zacian": "Should Win via Water Spout",
        
    },
    "loses": {
        "Mega Mewtwo Y": "Loses via 2KO+",
        "Dialga": "Loses via 2KO+",
        "Yveltal": "Loses via 2KO+",
        "Regigigas": "Loses via 2KO+",
        "Lugia": "Loses via 2KO+",
        "Kyurem": "Loses via 2KO+",
        "Zekrom": "Loses via Ohko"
    },
    "conditional": {
        "Xerneas": "Loses to Naive Xerneas via 2KO, Wins vs Adamant Xerneas via Water Spout 2KO",
        "Giratina": "Depends on Send, use Ice Beam",
        "Primal Kyogre": "Depends on Send, use 2 Water Spouts then Double-Edge",
        "Arceus": "Wins if Naive arceus, Loses to Rash Arceus if less than 23 HP and 23 SpDef"
    }
}

battle_instructions["Mega Mewtwo X"] = {
    "wins": {
        "Primal Groudon": "Wins via Future Sight Spam",
        "Xerneas": "Wins via Future Sight Spam",
        "Zekrom": "Wins via Future Sight Spam",
        "Marshadow": "Wins via Future Sight Spam",
        "Landorus": "Wins via Future Sight Spam",
        "Zygarde": "Wins via Future Sight Spam",
        "Dialga": "Wins via Aura Sphere Spam",
        "Regigigas": "Wins via Aura Sphere Spam",
        "Solgaleo": "Wins via Aura Sphere Spam",
        "Kyurem": "Wins via Aura Sphere Spam"
    },
    "loses": {
        "Mega Mewtwo Y": "Loses via 2KO+",
        "Primal Kyogre": "Loses via 2KO+",
        "Giratina": "Loses via 2KO+",
        "Lunala": "Loses via 2KO+",
        "Lugia": "Loses via 2KO+",
        "Mega Rayquaza": "Loses via Ohko",
        "Yveltal": "Loses via Ohko",
        "Magearna": "Loses via Ohko",
        "Ho-oh": "Loses via Ohko",
        "Diancie": "Loses via Ohko"
    },
    "conditional": {
        "Mega Mewtwo X": "Whoever has Send wins via Future Sight 2KO",
        "Arceus": "The higher the bulk, the higher Arceus' Sp. Atk has to be. Min bulk to survive Max Arceus (NOT INCLUDED: 24+ HP, 25+ Def, 25+ Sp. Def)"
    }
}

battle_instructions["Dialga"] = {
    "wins": {
        "Mega Rayquaza": "Wins via Roar of Time Spam",
        "Primal Kyogre": "Wins via Roar of Time Spam",
        "Yveltal": "Wins via Roar of Time Spam",
        "Regigigas": "Wins via Roar of Time Spam",
        "Giratina": "Wins via Roar of Time Spam",
        "Zekrom": "Wins via Roar of Time Spam",
        "Lugia": "Wins via Roar of Time Spam",
        "Kyurem": "Wins via Roar of Time Spam",
        "Ho-oh": "Wins via Roar of Time Spam",
        "Landorus": "Wins via Roar of Time Spam",
        "Diancie": "Wins via Flash Cannon Spam",
        "Magearna": "Wins via Earth Power Spam",
        "Solgaleo": "Wins via Earth Power Spam"
    },
    "loses": {
        "Primal Groudon": "Loses via Ohko",
        "Mewtwo X": "Loses via 2KO+",
        "Mewtwo Y": "Loses via 2KO+",
        "Xerneas": "Loses via 2KO+",
        "Marshadow": "Loses via 2KO+",
        "Lunala": "Loses via 2KO+",
        "Zygarde": "Loses via 2KO+"
    },
    "conditional": {
        "Arceus": "May lose via 2KO+, but use Roar of Time.",
    }
}


battle_instructions["Giratina"] = {
    "wins": {
        "Mega Mewtwo Y": "Wins via Shadow Force 1HKO",
        "Marshadow": "Wins via Shadow Force 1HKO",
        "Metagross": "Wins via Shadow Force 2HKO",
        "Arceus": "Wins via Aura Sphere Spam"
    },
    "loses": {
        "Yveltal": "Loses via 2HKO+",
        "Rayquaza": "Loses via 2HKO+",
        "Magearna": "Loses via 2HKO+",
        "Diancie": "Loses via 2HKO+",
        "Xerneas": "Loses via 2HKO+",
        "Regigigas": "Loses via 2HKO+",
        "Groudon": "Loses via 2HKO+",
        "Zygarde": "Loses via 2HKO+",
        "Zekrom": "Loses via 2HKO+",
        "Dialga": "Loses via Roar of Time 1HKO",
        "Kyogre": "Loses to Modest Kyogre via Ice Beam 2HKO"
    },
    "conditional": {
        "Kyogre": "Needs 30+ HP & 26+ Sp. Def to beat Timid Kyogre via 2x Shadow Force + Sneak",
        "Giratina": "Depends on send or who is faster, wins via Shadow Force 2HKO"
    }
}

battle_instructions["Marshadow"] = {
    "wins": {
        "Arceus": "Wins via Close Combat Spam",
        "Regigigas": "Wins via Close Combat Spam",
        "Zekrom": "Wins via Close Combat Spam",
        "Kyurem": "Wins via Close Combat then Sucker Punch",
        "Landorus": "Wins via Ice Punch Spam",
        "Dialga": "Wins vs Timid via Close Combat Spam"
    },
    "loses": {
        "Zygarde": "Loses via 2KO+",
        "Rayquaza": "Loses via OHKO",
        "Kyogre": "Loses via OHKO",
        "Groudon": "Loses via OHKO",
        "Yveltal": "Loses via OHKO",
        "Mewtwo X": "Loses via OHKO",
        "Mewtwo Y": "Loses via OHKO",
        "Xerneas": "Loses via OHKO",
        "Giratina": "Loses via OHKO",
        "Magearna": "Loses via OHKO",
        "Ho-oh": "Loses via OHKO",
        "Lugia": "Loses via OHKO",
        "Diancie": "Loses via OHKO"
    },
    "conditional": {
        "Marshadow": "Chances, use spectral thief or use sucker punch if low HP.",
        "Solgaleo": "Wins with 29+ HP and 30+ Def via Spectral Thief 2KO, otherwise OHKO (Not included in stats)",
        "Dialga": "Loses to Modest"
    }
}
battle_instructions["Zacian"] = {
    "wins": {
        "Ice Rider": "Wins via Iron Head Spam",
        "Black and White Kyurem": "Wins via Iron Head Spam",
        "Marshadow": "Wins via Iron Head Spam",
        "Xerneas": "Wins via Iron Head Spam",
        "Diancie": "Wins via Iron Head Spam",
        "Dusk Necrozma": "Wins via Close Combat then Crunch",
        "Mewtwo X": "Wins via Giga Impact Spam",
        "Rayquaza": "Wins via Giga Impact Spam",
        "Yveltal": "Wins via Giga Impact Spam",
        "Shadow Rider": "Wins via Crunch Spam",
        "Ultra Necrozma": "Wins via Crunch Spam",
        "Dawn Necrozma": "Wins via Crunch Spam",
        "Mewtwo Y": "Wins via Crunch Spam",
        "Solgaleo": "Wins via Crunch Spam",
        "Zamazenta": "Wins via Close Combat Spam",
        "Regigigas": "Wins via Close Combat Spam",
        "Arceus": "Wins via Close Combat Spam",
        "Dialga": "Wins via Close Combat Spam",
        "Magearna": "Wins via Close Combat Spam"
    },
    "loses": {
        "Rayquaza": "Loses via dragon ascent then extreme speed",
        "Zygarde": "Loses via 2KO",
        "Groudon": "Loses via OHKO",
        "Victini": "Loses via OHKO",
        "Zacian": "Whoever has send or is faster wins via Close Combat 2KO",
        "Eternatus": "Beats with max Atk if it has less than 28 HP & 28 Def (for 25 Atk Eternatus needs less than 26 HP and 26 Def)",
        "Origin Giratina": "Loses to Adamant Giratina via 2KO, beats Jolly Giratina via Crunch 3KO"
    },
    "conditional": {
        "Kyogre": "Wins vs Timid Kyogre via Giga Impact 2KO or loses to Modest Kyogre if it has less than 20 HP and 21 Sp. Def"
    }
}



battle_instructions["Dragapult"] = {
    "wins": {
        "Metagross": "Wins via Phantom Force then Sucker Punch",
        "Toxapex": "Wins via Dragon Darts spam",
        "Gyarados": "Wins via Dragon Darts spam",
        "Swampert": "Wins via Dragon Darts spam",
        "Staraptor": "Wins via Dragon Darts spam",
        "Haxorus": "Wins via Dragon Darts spam",
        "Braviary": "Wins via Dragon Darts spam",
        "Pyroar": "Wins via Dragon Darts spam",
        "Feraligatr": "Wins via Dragon Darts spam",
        "Mamoswine": "Wins via Dragon Darts spam",
        "Porygon": "Wins via Dragon Darts spam",
        "Conkeldurr": "Wins via Dragon Darts spam",
        "Noivern": "Wins via Dragon Darts spam",
        "Starmie": "Wins via Phantom Force spam",
        "Arcanine": "Wins via Phantom Force spam",
        "Infernape": "Wins via Phantom Force spam",
        "Archeops": "Wins via Phantom Force spam",
        "Delphox": "Wins via Phantom Force spam",
        "Hawlucha": "Wins via Phantom Force spam",
        "Copperajah": "Wins via Phantom Force spam",
        "Toxtricity": "Wins via Phantom Force spam",
        "Dragonite": "Wins via Dragon Darts OHKO vs Dragonite"
    },
    "loses": {
        "Slaking": "Loses via 2KO+",
        "Golisopod": "Loses via 2KO+",
        "Skuntank": "Loses via 2KO+",
        "Garchomp": "Loses via OHKO",
        "Primarina": "Loses via OHKO",
        "Rhyperior": "Loses via OHKO",
        "Krookodile": "Loses via OHKO",
        "Dragapult": "Loses if Impish Dnite with 27+ HP and 28+ Def"
    },
    "conditional": {
        "Dragapult": "Whoever is faster or has send wins via Phantom Force"
    }
}


battle_instructions["Eternatus"] = {
    "wins": {
        "Rayquaza": "Wins via Hyper Beam Spam",
        "Kyogre": "Wins via Dynamax Cannon or Eternabeam Spam", 
        "Regigigas": "Wins via Dynamax Cannon or Eternabeam Spam",
        "Arceus": "Wins via Dynamax Cannon or Eternabeam Spam",
        "Yveltal": "Wins via Dynamax Cannon or Eternabeam Spam",
        "Giratina": "Wins via Dynamax Cannon or Eternabeam Spam",
        "Zekrom": "Wins via Dynamax Cannon or Eternabeam Spam",
        "Marshadow": "Wins via Dynamax Cannon or Eternabeam Spam",
        "Lugia": "Wins via Dynamax Cannon or Eternabeam Spam",
        "Ho-oh": "Wins via Dynamax Cannon or Eternabeam Spam",
        "Kyurem": "Wins via Dynamax Cannon or Eternabeam Spam",
        "Landorus": "Wins via Dynamax Cannon or Eternabeam Spam",
        "Victini": "Wins via Dynamax Cannon or Eternabeam Spam",
        "Zamazenta": "Wins via Flamethrower Spam",
        "Magearna": "Wins via Flamethrower Spam",
        "Solgaleo": "Wins via Flamethrower Spam",
        "Melmetal": "Wins via Flamethrower Spam",
        "Xerneas": "Wins via Venoshock Spam",
        "Diancie": "Wins via Venoshock Spam"
    },
    "loses": {
        "Zacian": "Loses via 2KO+, but using Venoshock should work well.",
        "Lunala": "Loses via 2KO+, but use Dynamax Cannon (can also use Flamethrower).",
        "Groudon": "Loses via 2KO+, but use Dynamax Cannon. Do NOT use Flamethrower as Groudon is resistant to fire.",
        "Ice Rider Calyrex": "Loses via Ohko, but use Flamethrower.",
        "Shadow Rider Calyrex": "Loses via Ohko, but use Dynamax Cannon (can also use Flamethrower).",
        "Dialga": "Loses via Ohko, but use Dynamax Cannon (can also use Flamethrower).",
        "Mewtwo X": "Loses via Ohko, but use Dynamax Cannon (or Flamethrower).",
        "Mewtwo Y": "Loses via Ohko, but use Dynamax Cannon (or Flamethrower)."
    },
    "conditional": {
        "Zygarde": "May lose via 2KO+, but use Eternabeam or Dynamax Cannon. 28+ Sp. Atk versus perfect Bulk Zygarde, but about 20+ Sp. Atk to win generally."
    }
}

