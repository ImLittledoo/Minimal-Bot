from discord.app_commands.transformers import NoneType
from discord.ext import commands, tasks
import discord
import random
import os
import asyncio
from itertools import cycle

client = commands.Bot(command_prefix='.',
                      intents=discord.Intents.all(),
                      help_command=None)

bot_status_game = cycle([".help", "Dank Memer", "Minimal Dank"])


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status_game)))


@client.event
async def on_ready():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')
    print("Minimal Dank is ready")
    await change_status.start()


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')


client.run(
    "MTE1MTkyNTkzMTM3NjY0MDA4MQ.GOoEm8.QmPJMlN88MTe3MwtwufOuH00vhAucdC2Iz9Fcs")
