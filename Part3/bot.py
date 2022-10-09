from ast import alias
import imp
from urllib import response
import discord
import random
from discord.ext import commands
from secrets import credential

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='-',intents=intents)


@client.event
async def on_ready():
    print("Bot is Online")

@client.event 
async def on_member_join(member):
    print(f"{member} has joined the server..")

@client.event
async def on_member_left(member):
    print(f"{member} has left the server..")


# command has parenthesis as it can accepts some pararmeters. Refer docs of discord!!
# the function name will become a command
@client.command()
async def hello(ctx): #ctx is context
    await ctx.send(f'Hi {ctx.author} from Anonymous Bot!! {round(client.latency*1000)}ms')


# underscore allows to start a function name with a number
# aliases allows all those commands to run the below function
@client.command(aliases=['8ball','eightball','8alls','eightballs'])
async def _8ball(ctx,*,que): # asterisk in between allows 'que' to take all the arguments after the command
    responses = ['You are awesome','definitely','Maybe','Better luck next time!!']
    await ctx.send(f'Question - {que}\n Answer - {random.choice(responses)}')

client.run(credential['token'])
