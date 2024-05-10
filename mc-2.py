from discord.ext import commands, tasks

import discord
import random
import os
import asyncio
from itertools import cycle


class MC2(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('mc-2.py is ready!')

    @commands.command()
    async def membercount(self, ctx):
        total_members = ctx.guild.member_count
        real_members = len(
            [member for member in ctx.guild.members if not member.bot])
        bot_count = total_members - real_members

        embed = discord.Embed(title='Member Count')
        embed.add_field(name='Total Members', value=total_members)
        embed.add_field(name='Members', value=real_members)
        embed.add_field(name='Bots', value=bot_count)

        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(MC2(client))
