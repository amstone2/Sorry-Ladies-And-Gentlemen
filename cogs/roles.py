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

class roles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
		name='totalRoles',
		description='Gets the total roles for the server',
		usage='getRoles'
	)
    async def getRoles(self, ctx):
        if ctx.author.bot:
            return
        await ctx.channel.send(f"{ctx.author.mention} There are a total of {len(ctx.guild.roles)} roles.")


    @commands.command(
		name='myTotalRoles',
		description='Gets the authors users roles for the server',
		usage='myTotalRoles'
	)
    async def getRoles(self, ctx):
        if ctx.author.bot:
            return
        await ctx.channel.send(f"{ctx.author.mention} has a total of {len(ctx.author.roles)} roles.")


    @commands.command(
		name='usersTotalRoles',
		description='Gets the mentioned users roles for the server',
		usage='usersTotalRoles'
	)
    async def getRoles(self, ctx, arg):
        if ctx.author.bot:
            return
        userID = arg.replace('<', '').replace('@', '').replace('>', '')
        user = ctx.guild.get_member(int(userID))
        await ctx.channel.send(f"{user.name} has a total of {len(user.roles)} roles.")

def setup(bot):
    bot.add_cog(roles(bot))