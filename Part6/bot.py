


import os
import asyncio
import discord

from discord.ext import commands
from secrets import credential

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='-',intents=intents)





@client.command()
async def load(ctx,extension): #loading the cogs
    await client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx,extension): #unloading the cogs
    await client.unload_extension(f'cogs.{extension}')




#we want whenever bot is online we need access to all cogs so we loads all files from cogs folder
async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}') # we used slicing as we do  not need .py from filename






async def main():
    async with client:
        await load_extensions()
        await client.start(credential['token'])

asyncio.run(main())


