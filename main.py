import re
import discord
import asyncio

from discord.ext import commands
from discord.ext.commands import errors

TKN = ""

with open("token.md", 'r') as file:
    content = file.read()
    match = re.search(r'token\s*=\s*(\S+)', content)

    if match:
        TKN = match.group(1)
        print(TKN)
    else:
        print("ERROR - NO TKN FOUND")

bot = commands.Bot(command_prefix='-', intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command
async def test():
    pass

if TKN:
    try:
        bot.run(TKN)
    except errors.LoginFailure:
        print("!! ABORTING !!")

    else:
        print("!! ABORTING !!")

