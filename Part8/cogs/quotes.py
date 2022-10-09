
from random import random
import random
import discord
from discord.ext import commands


class Quotes(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def quote(self,ctx):
        responses = ['You are genius','Great!!','Good Luck']
        await ctx.send(f'{random.choice(responses)} {ctx.author}')

async def setup(client):
    await client.add_cog(Quotes(client))