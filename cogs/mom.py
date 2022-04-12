from discord.ext import commands
import discord




name = "alex"



class mom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def name(self, ctx, arg):
        """Says hello"""
        global name
        await ctx.channel.send(arg)
        print("Prev name is ", name)
        print("new name is ", arg)
        name = arg


def setup(bot):
    bot.add_cog(mom(bot))