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

        if (message.guild.name == 'Ligma Pi Fraternity'):
            return

        messages = await message.channel.history(limit=5).flatten()


        # Gets the roles we need
        cheeseTouch = discord.utils.get(message.guild.roles, name="Cheese Touch")

        # Gests who sent the message
        user = message.author.id
        member = message.author

        await message.channel.send(f"https://static.wikia.nocookie.net/doawk/images/0/0b/Greg_technically_has_the_Cheese_Touch_as_the_boys_scream_and_ran_away.jpg/revision/latest/scale-to-width-down/755?cb=20190320011029")


        # If they have the cheese touch. 
        if cheeseTouch in message.author.roles:
            # Random Chance to remove cheese touch 
            randomFloat = round(random.uniform(0.00, 99.99), 2)
            print("Random float: ", randomFloat)
            if randomFloat < 2.00:
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
                    await message.channel.send(f"<@{author.id}> Now has the cheese touch!")
                    await message.channel.send(f"https://static.wikia.nocookie.net/doawk/images/0/0b/Greg_technically_has_the_Cheese_Touch_as_the_boys_scream_and_ran_away.jpg/revision/latest/scale-to-width-down/755?cb=20190320011029")



        #     if randomInt < 2:
        #         await message.channel.send(f"<@{user}> No longer has the cheese touch!")
        #         await member.remove_roles(cheeseTouch)
        #         await member.add_roles(clean)
            
        #         # Get users with this role. 
        #         usersWithNoCheese = []
        #         for guild in self.bot.guilds:
        #             for member in guild.members:
        #                 if clean in member.roles:
        #                     usersWithNoCheese.append(member)
        #         for user in usersWithNoCheese:
        #             print("Members with no cheese: ", user) 

        #         # Pick one at random and give them the cheese touch. 
        #         randomInt2 = random.randint(0, len(usersWithNoCheese) - 1)
        #         print("rand int2 ", randomInt2, " with length of role", len(usersWithNoCheese))
        #         await usersWithNoCheese[randomInt2].remove_roles(clean)
        #         await usersWithNoCheese[randomInt2].add_roles(cheeseTouch)
        #         await message.channel.send(f"<@{usersWithNoCheese[randomInt2].id}> Now has the cheese touch!!!!!!")



def setup(bot):
    bot.add_cog(cheese(bot))