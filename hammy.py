import os
import asyncio
import os.path
from io import BytesIO
import random

import discord
from dotenv import load_dotenv

from discord.ext import commands, tasks
from discord import app_commands
from discord.utils import get

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents=discord.Intents.all()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

    member_ids = [member.id for member in guild.members]
    print(member_ids)

@bot.event
async def on_message(message):
    if message.author == bot.user:  # Ignore messages from the bot itself
        return
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send("Hi I'm Hammy, nice to meet you! *^_^*")

bot.run(TOKEN)
