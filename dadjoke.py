from discord.ext import commands, tasks
from itertools import cycle

import aiohttp
import discord
import random
import os
import asyncio


class DadJokes(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("dadjokes.py is online!")

    @commands.command()
    async def dadjoke(self, ctx):
        async with aiohttp.ClientSession() as session, \
                   session.get('https://icanhazdadjoke.com/',
                               headers={'Accept': 'application/json'}) as response:
            if response.status == 200:
                data = await response.json()
                joke = data['joke']
                await ctx.send(joke)
            else:
                await ctx.send(
                    "Oops! Couldn't fetch a dad joke right now. Try again later."
                )


async def setup(client):
    await client.add_cog(DadJokes(client))
