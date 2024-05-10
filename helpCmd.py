from discord.ext import commands, tasks

import discord
import random
import os
import asyncio
from itertools import cycle


class HelpCmd(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("help.py is ready!")

    @commands.command()
    async def help(self, ctx):

        help_embed = discord.Embed(title="Help Command",
                                   color=discord.Color.green(),
                                   description="These are the bot's commands:")
        help_embed.set_author(name="Minimal")
        help_embed.set_footer(text=f"Requested by {ctx.author.name}",
                              icon_url=ctx.author.avatar)
        help_embed.add_field(name="8ball",
                             value="Let the magic ball predict your fate!",
                             inline=False)
        help_embed.add_field(name="dadjoke",
                             value="Get a completely random dad joke.",
                             inline=False)
        help_embed.add_field(
            name="ping",
            value="This command returns the latency of the bot.",
            inline=False)
        help_embed.add_field(name="echo",
                             value="This command returns a message.",
                             inline=False)

        await ctx.send(embed=help_embed)


async def setup(client):
    client.add_cog(HelpCmd(client))
