import discord
from discord.ext import commands, tasks
from itertools import cycle

status = cycle(["teemo", 'garen', 'yasuo', 'monkey', 'dog'])

class bgtask(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()
        print('Bot is online')

    @tasks.loop(seconds=5)
    async def change_status(self):
        await self.client.change_presence(activity=discord.Game(next(status)))


def setup(client):
    client.add_cog(bgtask(client))
