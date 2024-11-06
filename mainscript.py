import discord
import re
import requests
from discord.ext import commands
import extract_info as extinfo
import battle_helper as batinst
from battle_helper import get_instructions
from utils import *
from prices import *
import os
from AutoName import PokeNamer

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.messages = True
intents = discord.Intents().all()
client = commands.Bot(command_prefix="?", intents=intents)
pokemon_data = load_pokemon_data_from_file()
# Dictionary to store logged Pokémon stats
pokemon_data = {}


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    client.add_cog(PokeNamer(client))

@client.command()
async def ping(ctx):
    await ctx.send('Pong! {0}ms'.format(round(client.latency*1000, 1)))

@client.command()
async def israre(ctx, name):
    res = extinfo.israre(name.title())
    if res[-1] == True:
        await ctx.send("%s is %s." % (name.title(), res[0]))
    elif res[-1] == False:
        await ctx.send("%s is not rare (or it is not known as rare by the bot.)" % name)
    else:
        await ctx.send("Some error occurred.")

@client.command()
async def battle(ctx, your, opponent):
    result = get_instructions(your.lower(), opponent.lower())
    em = discord.Embed(title="Instructions")
    if result == "0":
        em.description = "Your Pokémon is not in the instructions list."
        await ctx.send(embed=em)
        return
    if not result["wins"]=="0":
        em.add_field(name="Wins",value=result["wins"],inline = False)
    if not result["loses"]=="0":
        em.add_field(name="Loses",value=result["loses"],inline = False)
    if not result["conditional"]=="0":
        em.add_field(name="Conditional",value=result["conditional"],inline = False)
    await ctx.send(embed=em)

@client.command()
async def team(ctx, *args):
    opponent_team = []
    for arg in args:
        opponent_team.append(arg)
    embed = discord.Embed(title="Recommended Team and Moves")
    embed = batinst.add_recommendations_to_embed(embed, str(ctx.author.id), opponent_team)
    await ctx.send(embed=embed)

@client.command()
async def team_all(ctx, *args):
    opponent_team = []
    for arg in args:
        opponent_team.append(arg)
    embed = discord.Embed(title="Recommended Team and Moves")
    embed = batinst.add_all_recommendations_to_embed(embed, str(ctx.author.id), opponent_team)
    await ctx.send(embed=embed)

@client.command()
async def type_advantage(ctx, your, opp):
    res = batinst.type_advantage(your, opp)
    em = discord.Embed(title=f"Type advantage: {res[0]}")
    em.add_field(name="Your Pokemon Types", value = res[1])
    em.add_field(name="Opponent Pokemon Types", value = res[2])
    await ctx.send(embed=em)

@client.command()
async def iv(ctx, name):
    await ctx.send("[Atk/Spatk and Def/Spdef can vary depending on whether you are focusing on physical or special. Stats shown are the most typical/recommended ones.]\n"+batinst.recommend_stats(name))


@client.command()
async def shiny_prices(ctx):
    await ctx.send(format_price_guide())


# Event listener to capture Pokémon stats via embeds
@client.event
async def on_message(message):
    if message.author.bot:  # Ignore messages from bots
        return

    if message.content.lower() == "?info-log":
        if message.reference and message.channel.permissions_for(message.author).read_messages:
            original_message = await message.channel.fetch_message(message.reference.message_id)
            
            if original_message.embeds:
                for embed in original_message.embeds:
                    if "Level" in embed.title: 
                        pokemon_stats = batinst.extract_stats_from_plaintext(batinst.extract_embed_fields(embed)[-1]['Stats'])
                        nature = batinst.extract_nature(batinst.extract_embed_fields(embed)[0]['Details'])
                        pokemon_stats['nature'] = nature
                        user_id = message.author.id
                        p_index = batinst.extract_pokemon_index(embed.footer.text)
                        pokemon_name = batinst.info_title(embed.title)[1]
                        pokemon_stats['name'] = pokemon_name

                        if user_id not in pokemon_data:
                            pokemon_data[user_id] = {}
                        pokemon_data[user_id][p_index] = pokemon_stats
                        save_pokemon_data_to_file(pokemon_data)
                        
                        await message.channel.send(f"{pokemon_name} has been logged successfully.")
                        break 
            else:
                await message.channel.send("No Pokémon embed found in the original message.")
    else:
        await client.process_commands(message)


client.run(TOKEN)
