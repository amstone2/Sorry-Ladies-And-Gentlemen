# Imports
from ast import Return
from discord.ext import commands
import random
import discord
from discord.utils import get
import time
from discord.ext import tasks
from os.path import exists
import json

class cheese(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.activateTouchGlobal = True
        self.infectionRateGlobal = 5.00

    @commands.Cog.listener()
    async def on_ready(self):
        self.change_presence.start()
                
        if exists('ct_users.json') == False:
            print('ct_users.json not found')

            t = time.time()

            data = {}
            for server in self.bot.guilds:
                cheese_role = discord.utils.get(server.roles, name="Cheese Touch")
                if not cheese_role:
                    # self.assign_cheese()
                    print('need to assign person with cheese touch')
                    continue
                person_with_cheese = cheese_role.members[0]
                data[server.name] = {'name': person_with_cheese.name, 'id': person_with_cheese.id, 'timestamp': t}
            print(data)

            print("Creating ct_users.json")
            jsonString = json.dumps(data)
            jsonFile = open("ct_users.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()
        else:
            with open('ct_users.json') as json_file:
                self.users_with_cheese = json.load(json_file)

    @tasks.loop(minutes=1) 
    async def change_presence(self):
        return

    @commands.Cog.listener()
    async def on_message(self, message):
        # print(message.content, "\n")

        if message.author.bot:
            return

        if (self.activateTouchGlobal == False):
            return
        
        # if(message.guild.name == 'Ligma Pi Fraternity'):
        #     return 
        
        cheeseTouch = discord.utils.get(message.guild.roles, name="Cheese Touch")

        tenMostRecentAuthors = []
        tenMessages = await message.channel.history(limit=10).flatten()
        for msg in tenMessages:
            # No duplicates
            if msg.author not in tenMostRecentAuthors:
                if msg.author.bot == False:
                    tenMostRecentAuthors.append(msg.author)
        
        print("10 most recent authors")
        for author in tenMostRecentAuthors:
            print(author)

        personWithCheeseTouch = None
        for user in message.guild.members:
            if cheeseTouch in user.roles:
                personWithCheeseTouch = user

        if personWithCheeseTouch in tenMostRecentAuthors:
            print("Cheese touch user within most recent authors \n")
            tenMostRecentAuthors.remove(personWithCheeseTouch)

            print("Ten most recent authors no cheese touch")
            for author in tenMostRecentAuthors:
                print(author.name)
            print("\n")

            randomFloat = round(random.uniform(0.00, 100.00), 2)
            print("Random float: ", randomFloat)
            print("Percent chance: ", self.infectionRateGlobal)
            print("\n")
            if randomFloat < float(self.infectionRateGlobal):
                if(len(tenMostRecentAuthors) > 0):
                    await message.channel.send(f"{personWithCheeseTouch.mention} No longer has the cheese touch!")
                    await personWithCheeseTouch.remove_roles(cheeseTouch)
                    
                    for i in range(3):
                        time.sleep(1)
                        await message.channel.send("Finding next host...")

                    author = random.choice(tenMostRecentAuthors)
                    await author.add_roles(cheeseTouch)
                    await message.channel.send(f"<@{author.id}> Now has the cheese touch! Typing close to other users will have a chance to give it to them.")
                    await message.channel.send(f"https://tenor.com/view/cheese-touch-diary-of-a-wimpy-kid-greg-no-gif-25045298")
    
    @commands.command(
		name='changeInfectionRate',
		description='Changes the percent change for someone to pass along the cheese touch.',
		usage='changeInfectionRate'
	)
    async def changeInfectionRate(self, ctx, arg):
        authorID = str(ctx.author.id)
        if(authorID == "163862875738341376"):
            print("Alex sent this command")
            oldInfectionRate = self.infectionRateGlobal
            self.infectionRateGlobal = arg
            await ctx.channel.send(f"<@{ctx.author.id}> Changed infection rate from {oldInfectionRate} to {self.infectionRateGlobal} percent.")

    @commands.command(
		name='changeActivationStatus',
		description='Gets whos infected by the cheese touch.',
		usage='whoIsInfected'
	)
    async def changeActivationStatus(self, ctx, arg):
        authorID = str(ctx.author.id)
        if(authorID == "163862875738341376"):
            oldTouch = self.activateTouchGlobal
            self.activateTouchGlobal = arg
            await ctx.channel.send(f"{ctx.author.mention} Changed activation rate from {oldTouch} to {arg}.")

    @commands.command(
		name='whoIsInfected',
		description='Gets whos infected by the cheese touch.',
		usage='whoIsInfected'
	)
    async def whoIsInfected(self, ctx):
        if ctx.author.bot:
            return
        cheeseTouch = discord.utils.get(ctx.guild.roles, name="Cheese Touch")
        for user in ctx.guild.members:
            if cheeseTouch in user.roles:
                await ctx.channel.send(f"{user.mention} Is infected with the cheese touch.")

        await ctx.channel.send('https://tenor.com/view/thats-gross-ewww-disgusting-gif-14383467')

def setup(bot):
    bot.add_cog(cheese(bot))