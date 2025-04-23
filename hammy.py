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

import discord, requests as r, pickle, os.path as p
from dotenv import dotenv_values


import discord
from discord.ext import commands
import subprocess

from csv_parse import read_csv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

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

    await tree.sync(guild=guild)
    print(f"Synced commands with {guild.name} ({guild.id})")

@bot.event
async def on_message(message):
    if message.author == bot.user:  # Ignore messages from the bot itself
        return
    await bot.process_commands(message)

@tree.command( name="hello", description="Checks if the bot is online." )
async def hello(inter: discord.Interaction):
    await inter.response.send_message("Hi I'm Hammy, nice to meet you! *^_^*")
    print("[CMD] hello command executed.")

@tree.command( name="sync", description="Sync the bot's command tree")
async def sync(inter: discord.Interaction):
    try:
        await tree.sync()
        await inter.response.send_message("Command tree synced successfully.")
        print("[CMD] Command tree synced.")
    except Exception as e:
        await inter.response.send_message(f"Command tree could not be synced. Error: {e}")
        print("[CMD] Command tree sync failed.")

bot.run(TOKEN)
