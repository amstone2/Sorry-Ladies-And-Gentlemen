from ast import Return
from discord.ext import commands
import random
import discord
from discord.utils import get
import time


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

class cheese(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        # if (message.guild.name == 'Ligma Pi Fraternity'):
        #     return

        messages = await message.channel.history(limit=10).flatten()


        # Gets the role we need
        cheeseTouch = discord.utils.get(message.guild.roles, name="Cheese Touch")

        # Gests who sent the message
        user = message.author.id
        member = message.author


        # If they have the cheese touch. 
        if cheeseTouch in message.author.roles:
            # Random Chance to remove cheese touch 
            randomFloat = round(random.uniform(0.00, 99.99), 2)
            print("Random float: ", randomFloat)
            if randomFloat < 3:
                prevMessagesAuthors = []
                for msg in messages:
                    if (msg.author.bot == False) & (msg.author != message.author):
                        prevMessagesAuthors.append(msg.author)
                    for author in prevMessagesAuthors:
                        print(author, "\n")
                if(len(prevMessagesAuthors) > 0):
                    await message.channel.send(f"<@{user}> No longer has the cheese touch!")
                    await member.remove_roles(cheeseTouch)

                    time.sleep(1)
                    await message.channel.send("Finding next host...")
                    time.sleep(1)
                    await message.channel.send("Finding next host...")
                    time.sleep(1)
                    await message.channel.send("Finding next host...")

                    author = random.choice(prevMessagesAuthors)
                    await author.add_roles(cheeseTouch)
                    await message.channel.send(f"<@{author.id}> Now has the cheese touch! Typing close to other users will have a chance to give it to them.")
                    await message.channel.send(f"https://tenor.com/view/cheese-touch-diary-of-a-wimpy-kid-greg-no-gif-25045298")
                    

def setup(bot):
    bot.add_cog(cheese(bot))