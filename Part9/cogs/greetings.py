
import discord
from discord.ext import commands


class Greetings(commands.Cog):
    def __init__(self,client):
        self.client = client


        
    @commands.command()
    async def hello(self,ctx):
        await ctx.send(f'Hello {ctx.author} from Anonymous Bot!!')

async def setup(client):
    await client.add_cog(Greetings(client))