from discord.ext import commands, tasks

import discord
import random
import os
import asyncio
from itertools import cycle


class MagicBall(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('8ball.py is ready!')

  @commands.command(aliases=['8ball'])
  async def magic_ball(self, ctx, *, question):
    with open("8ball-responses.txt", "r") as f:
      random_responses = f.readlines()
      response = random.choice(random_responses)

    await ctx.send(response)


async def setup(client):
  await client.add_cog(MagicBall(client))
