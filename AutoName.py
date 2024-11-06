import discord
from discord.ext import commands
import requests
import random
import os
from io import BytesIO
from PIL import Image
from loadai import match_pokemon, load_data_from_file

class PokeNamer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ai = load_data_from_file("pokemon.ai")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 716390085896962058:  
            if message.embeds:
                if message.embeds[0].image:
                    image_url = message.embeds[0].image.url

                    response = requests.get(image_url)
                    image = Image.open(BytesIO(response.content))
                    temp_image_path = "temp/%s.jpg"%random.randint(1,10_000_000)
                    image.save(temp_image_path)

                    result, score = match_pokemon(temp_image_path, self.ai, 400)
                    await message.channel.send(f"Best Match: {result}\nScore: {score}\nPings: <@925982382778109982>")
                    os.remove(temp_image_path)


                    

