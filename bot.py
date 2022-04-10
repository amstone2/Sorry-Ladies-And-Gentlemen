# bot.py
import os

import discord
from dotenv import load_dotenv
import garlic

load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('SERVER')

client = discord.Client()



@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    messageFromUser = message.content
    messageFromUserLowerCase = messageFromUser.lower()

    if "garlic" in messageFromUserLowerCase:
        response = garlic.getRandomGarlicMeme()
        await message.channel.send(response)




client.run(TOKEN)