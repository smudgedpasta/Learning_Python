# This file serves as a template for the discord.py rewrite module
# Name the class the file name if you want it to be the category name ⚠️

import discord
from discord.ext import commands

class cogs(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def example(self, ctx):
        await ctx.send("```Dev test.```")

def setup (dottie):
    client.add_cog(cogs(client))
