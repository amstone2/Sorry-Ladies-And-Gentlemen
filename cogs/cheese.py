# Imports
from ast import Return
from discord.ext import commands
import random
import discord
from discord.utils import get
import time
import datetime
from discord.ext import tasks
from os.path import exists
import json

class cheese(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.activate_touch_global = True
        self.infection_rate_global = 5.00
        self.users_with_cheese = None
        timeout_duration_days = 2
        self.timeout_duration_in_seconds = 86400 * timeout_duration_days

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
            self.users_with_cheese = data
            print(data)

            print("Creating ct_users.json")
            self.write_to_file()
        else:
            with open('ct_users.json') as json_file:
                self.users_with_cheese = json.load(json_file)

    @tasks.loop(minutes=30) 
    async def change_presence(self):
        if self.users_with_cheese:
            for server in self.users_with_cheese:
                if server != 'SL&G':
                    continue
                if self.has_cheese_timed_out(server):
                    most_recent_channel = await self.get_most_recent_channel(server)
                    last_person_member = self.get_last_person_with_cheese(server, most_recent_channel.members)

                    await most_recent_channel.send("The cheese touch has expired!")
                    eligible_members = await self.get_eligible_members(server, most_recent_channel, last_person_member)
                    await self.assign_cheese(most_recent_channel, eligible_members, last_person_member)
                else:
                    print('Cheese still valid for', server)

        return

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if (self.activate_touch_global == False):
            return
        if(message.guild.name == 'Ligma Pi Fraternity'):
            return 

        ten_most_recent_authors = []
        async for msg in message.channel.history(limit=10):
            if msg.author not in ten_most_recent_authors and not msg.author.bot:
                ten_most_recent_authors.append(msg.author)

        person_with_cheese = self.get_last_person_with_cheese(message.guild.name, message.channel.members)

        if person_with_cheese in ten_most_recent_authors:
            # Remove person with the cheese so they don't get it again
            ten_most_recent_authors.remove(person_with_cheese)

            random_float = round(random.uniform(0.00, 100.00), 2)
            print("Random float: ", random_float)
            print("Percent chance: ", self.infection_rate_global)
            print("\n")
            # Only reassign if chance 
            if random_float < float(self.infection_rate_global):
                await self.assign_cheese(message.channel, ten_most_recent_authors, person_with_cheese)
    
    @commands.command(
		name='changeInfectionRate',
		description='Changes the percent change for someone to pass along the cheese touch.',
		usage='changeInfectionRate'
	)
    async def change_infection_rate(self, ctx, arg):
        if(ctx.author.id == 163862875738341376 or ctx.author.id == 184116812328337408):
            print("Alex sent this command")
            old_infection_rate = self.infection_rate_global
            self.infection_rate_global = arg
            await ctx.channel.send(f"<@{ctx.author.id}> Changed infection rate from {old_infection_rate} to {self.infection_rate_global} percent.")

    @commands.command(
		name='changeActivationStatus',
		description='Gets whos infected by the cheese touch.',
		usage='whoIsInfected'
	)
    async def change_activation_status(self, ctx, arg):
        if(ctx.author.id == 163862875738341376 or ctx.author.id == 184116812328337408):
            old_touch = self.activate_touch_global
            self.activate_touch_global = arg
            await ctx.channel.send(f"{ctx.author.mention} Changed activation rate from {old_touch} to {arg}.")

    @commands.command(
		name='whoIsInfected',
		description='Gets whos infected by the cheese touch.',
		usage='whoIsInfected'
	)
    async def who_is_infected(self, ctx):
        if ctx.author.bot:
            return
        cheese_touch = discord.utils.get(ctx.guild.roles, name="Cheese Touch")
        for user in ctx.guild.members:
            if cheese_touch in user.roles:
                await ctx.channel.send(f"{user.mention} Is infected with the cheese touch.")

        await ctx.channel.send('https://tenor.com/view/thats-gross-ewww-disgusting-gif-14383467')

    async def get_most_recent_channel(self, server_name):
        most_recent_channel = None
        most_recent_timestamp = 0

        # Find server in list of servers the bot is attached to
        for server in self.bot.guilds:
            if server.name == server_name:
                # Loop through all channels and find the most recently active channel
                for channel in server.text_channels:
                    channel_permissions = channel.overwrites_for(server.default_role)
                    if channel_permissions.view_channel or channel_permissions.view_channel is None:
                        last_msg = await channel.history().get()
                        if last_msg and last_msg.created_at.timestamp() > most_recent_timestamp:
                            most_recent_channel = channel
                            most_recent_timestamp = last_msg.created_at.timestamp()
        
        print("most recent channel " + most_recent_channel.name + " at " + str(datetime.datetime.fromtimestamp(most_recent_timestamp)))

        return most_recent_channel

    def has_cheese_timed_out(self, server_name):
        user_with_cheese = self.users_with_cheese[server_name]
        return time.time() > user_with_cheese['timestamp'] + self.timeout_duration_in_seconds

    async def get_eligible_members(self, server_name, channel, last_person_with_cheese=None):
        # Get 10 most recent authors in channel
        ten_most_recent_authors = []
        async for message in channel.history(limit=10):
            if message.author not in ten_most_recent_authors and not message.author.bot:
                ten_most_recent_authors.append(message.author)

        for author in ten_most_recent_authors:
            print('\t', author.name)

        # Make sure that the last person with the cheese is populated
        if last_person_with_cheese:
            # Remove last person with the cheese from possible candidates so they aren't assigned it again
            if last_person_with_cheese in ten_most_recent_authors:
                ten_most_recent_authors.remove(last_person_with_cheese)

        return ten_most_recent_authors

    async def assign_cheese(self, channel, eligible_members, last_person_with_cheese):
        cheese_touch_role = discord.utils.get(channel.guild.roles, name="Cheese Touch")
        if(len(eligible_members) > 0):
            # Remove cheese touch from the user
            await channel.send(f"{last_person_with_cheese.mention} No longer has the cheese touch!")
            await last_person_with_cheese.remove_roles(cheese_touch_role)
            
            for i in range(3):
                time.sleep(1)
                await channel.send("Finding next host...")

            # Randomly assign to new user from the most recent messages
            author = random.choice(eligible_members)
            await author.add_roles(cheese_touch_role)
            await channel.send(f"<@{author.id}> Now has the cheese touch! Typing close to other users will have a chance to give it to them.")
            await channel.send(f"https://tenor.com/view/cheese-touch-diary-of-a-wimpy-kid-greg-no-gif-25045298")

            # Update JSON data and write to file
            self.users_with_cheese[channel.guild.name] = {'name': author.name, 'id': author.id, 'timestamp': time.time()}
            self.write_to_file()
        else:
            print('No eligible members to assign cheese touch to!')

    def write_to_file(self):
        jsonString = json.dumps(self.users_with_cheese)
        jsonFile = open("ct_users.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()

    def get_last_person_with_cheese(self, server, members):
        last_person_member = None

        for member in members:
            if member.id == self.users_with_cheese[server]['id']:
                last_person_member = member
                break
        
        return last_person_member

def setup(bot):
    bot.add_cog(cheese(bot))