from discord.ext import commands
import random
import discord
from discord.utils import get


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

class cheese(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_message(self, message):

        # Gets the roles we need
        cheeseTouch = discord.utils.get(message.guild.roles, name="Cheese Touch")
        noCheeseTouch = discord.utils.get(message.guild.roles, name="No Cheese")

        # Gests who sent the message
        user = message.author.id
        member = message.author

        # If they have the cheese touch. 
        if cheeseTouch in message.author.roles:
            # Random Chance to remove cheese touch 
            randomInt = random.randint(0, 100)
            print("Random int: ", randomInt)
            if randomInt < 15:
                await message.channel.send(f"<@{user}> No longer has the cheese touch!")
                await member.remove_roles(cheeseTouch)
                await member.add_roles(noCheeseTouch)
            
                # Get users with this role. 
                usersWithNoCheese = []
                for guild in self.bot.guilds:
                    for member in guild.members:
                        if noCheeseTouch in member.roles:
                            usersWithNoCheese.append(member)
                for user in usersWithNoCheese:
                    print("Members with no cheese: ", user) 

                # Pick one at random and give them the cheese touch. 
                randomInt2 = random.randint(0, len(usersWithNoCheese) - 1)
                print("rand int2 ", randomInt2, " with length of role", len(usersWithNoCheese))
                await usersWithNoCheese[randomInt2].remove_roles(noCheeseTouch)
                await usersWithNoCheese[randomInt2].add_roles(cheeseTouch)
                await message.channel.send(f"<@{usersWithNoCheese[randomInt2].id}> Now has the cheese touch!!!!!!")



def setup(bot):
    bot.add_cog(cheese(bot))