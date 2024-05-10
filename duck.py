from discord.ext import commands, tasks
from itertools import cycle

import aiohttp
import discord
import random
import os
import asyncio
import json


class Duck(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("duck.py is online!")

    @commands.command()
    async def duck(self, ctx):
        with open("duck-links.txt", "r") as f:
            random_responses = f.readlines()
            response = random.choice(random_responses)

        embed = discord.Embed()
        embed.set_image(url=response.strip())

        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Duck(client))
