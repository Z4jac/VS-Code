import random
import discord
from discord.ext import commands

TOKEN = ('NTcwMjI5OTU3MzUyMjI2ODM2.XZhXaA.5Y43DhWyr2ZM9dMT_u90BsvG--M')
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot online")

@client.command
async def funcname(parameter_list):
    pass



client.run(TOKEN)


