from ast import Return
from discord.ext import commands
import random
import discord
from discord.utils import get
import time


activateTouchGlobal = True


infectionRateGlobal = 5.00





class cheese(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    global infectionRateGlobal
    @commands.Cog.listener()
    async def on_message(self, message):
        # print(message.content, "\n")

        if message.author.bot:
            return

        if (activateTouchGlobal == False):
            return
        
        # if(message.guild.name == 'Ligma Pi Fraternity'):
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
            randomFloat = round(random.uniform(0.00, 100.00), 2)
            print("Random float: ", randomFloat)
            if randomFloat < infectionRateGlobal:
                prevMessagesAuthors = []
                for msg in messages:
                    if (msg.author.bot == False) & (msg.author != message.author):
                        prevMessagesAuthors.append(msg.author)
                    for author in prevMessagesAuthors:
                        print(author, "\n")
                if(len(prevMessagesAuthors) > 0):
                    await message.channel.send(f"{user.mention} No longer has the cheese touch!")
                    await member.remove_roles(cheeseTouch)
                    

                    for i in range(3):
                        time.sleep(1)
                        await message.channel.send("Finding next host...")


                    author = random.choice(prevMessagesAuthors)
                    await author.add_roles(cheeseTouch)
                    await message.channel.send(f"<@{author.id}> Now has the cheese touch! Typing close to other users will have a chance to give it to them.")
                    await message.channel.send(f"https://tenor.com/view/cheese-touch-diary-of-a-wimpy-kid-greg-no-gif-25045298")
    
    @commands.command(
		name='changeInfectionRate',
		description='Changes the percent change for someone to pass along the cheese touch.',
		usage='changeInfectionRate'
	)
    async def changeInfectionRate(self, ctx, arg):
        global infectionRateGlobal
        authorID = str(ctx.author.id)
        if(authorID == "163862875738341376"):
            print("Alex sent this command")
            oldInfectionRate = infectionRateGlobal
            infectionRateGlobal = arg
            await ctx.channel.send(f"<@{ctx.author.id}> Changed infection rate from {oldInfectionRate} to {infectionRateGlobal} percent.")
        

    @commands.command(
		name='changeActivationStatus',
		description='Gets whos infected by the cheese touch.',
		usage='whoIsInfected'
	)
    async def changeActivationStatus(self, ctx, arg):
        global activateTouchGlobal
        authorID = str(ctx.author.id)
        if(authorID == "163862875738341376"):
            oldTouch = activateTouchGlobal
            activateTouchGlobal = arg
            await ctx.channel.send(f"{ctx.author.mention} Changed activation rate from {oldTouch} to {arg}.")



    @commands.command(
		name='whoIsInfected',
		description='Gets whos infected by the cheese touch.',
		usage='whoIsInfected'
	)
    async def whoIsInfected(self, ctx):
        if ctx.author.bot:
            return
        print("hello")
        cheeseTouch = discord.utils.get(ctx.guild.roles, name="Cheese Touch")
        print(cheeseTouch)
        for user in ctx.guild.members:
            if cheeseTouch in user.roles:
                await ctx.channel.send(f"{user.mention} Is infected with the cheese touch.")

            await ctx.channel.send('https://tenor.com/view/thats-gross-ewww-disgusting-gif-14383467')
        

def setup(bot):
    bot.add_cog(cheese(bot))