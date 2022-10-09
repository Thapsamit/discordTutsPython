import imp
import discord
from discord.ext import commands
from secrets import credential
intents = discord.Intents.default()
client = commands.Bot(command_prefix='-',intents=intents)


@client.event
async def on_ready():
    print("Bot is Online")

client.run(credential['token'])
