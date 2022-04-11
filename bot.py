from discord.ext import commands
from dotenv import load_dotenv
import os
import discord


load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('SERVER')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print('logged in')

bot.load_extension("cogs.garlic")
bot.load_extension("cogs.cheese")

bot.run(TOKEN)