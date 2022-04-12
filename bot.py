from discord.ext import commands
from dotenv import load_dotenv
import os
import discord



name = "alex"

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print('Logged in.')

# Comment these out when you are testing. 



bot.load_extension("cogs.garlic")
bot.load_extension("cogs.cheese")
bot.load_extension("cogs.mom")


bot.run(TOKEN)