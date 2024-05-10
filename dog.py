from discord.ext import commands, tasks
from itertools import cycle

import aiohttp
import discord
import random
import os
import asyncio
import json


class Dog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("dog.py is online!")

    @commands.command()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    "https://dog.ceo/api/breeds/image/random") as r:
                raw = await r.text()
                dogspic = json.loads(raw)

                embed = discord.Embed()
                embed.set_image(url=dogspic['message'])

                await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Dog(client))
