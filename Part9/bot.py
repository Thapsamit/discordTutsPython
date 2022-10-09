


import os
import asyncio
from pydoc import cli
import discord
from itertools import cycle
from discord.ext import commands,tasks
from secrets import credential

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='-',intents=intents)
status = cycle(['with you','my magic','with technology'])



@client.event
async def on_ready():
    change_status.start() #invoking background task
    await client.change_presence(status=discord.Status.online,activity=discord.Game('with you'))
    print("Bot is Online!!")


# handling errors for example if someone has typed the command but doesn't give any arguments which is necessary so we need to handle those errors




@client.command()
async def load(ctx,extension): #loading the cogs
    await client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx,extension): #unloading the cogs
 
    await client.unload_extension(f'cogs.{extension}')

@tasks.loop(seconds=5)
async def change_status(): # changes the activity of bot after every 5 seconds automatically
    await client.change_presence(activity=discord.Game(next(status)))



#we want whenever bot is online we need access to all cogs so we loads all files from cogs folder
async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}') # we used slicing as we do  not need .py from filename



# handle all commands that has missing arguments error
@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send(f"Hey!! {ctx.author} please send required arguments!!")
    if isinstance(error,commands.CommandNotFound):
        await ctx.send(f'Hey Its Wrong command!!')


async def is_owner(ctx):
    return ctx.author.id == 879248153033977857
@client.command()
@commands.check(is_owner)
async def clear(ctx,amt:int): #int represents the type of argument required
    await ctx.channel.purge(limit=amt)

# specifying error only if clear command has an error


@clear.error
async def clear_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send(f"Hey!! {ctx.author} please send required arguments for clear command !! \n for example :-    -clear 5 ")

async def main():
    async with client:
        await load_extensions()
        await client.start(credential['token'])

asyncio.run(main())


