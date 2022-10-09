import imp
import discord
from discord.ext import commands
from secrets import credential
intents = discord.Intents.default()
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

client.run(credential['token'])
