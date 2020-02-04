import discord
import json
from discord.ext import commands

class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.bot.loop.create_task(self.save_users())

        with open(r"C:\Users\Max\PycharmProjects\midyeardiscordbot\users.json", 'r') as f:
            self.users = json.load(f)
    async def seve_users(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            with open(r"C:\Users\Max\PycharmProjects\midyeardiscordbot\users.json", 'w') as f:
                json.dump(self.users, f, indent=4)

    def lvl_up(self, author_id):
        cur_xp = self.users[author_id]['exp']
        cur_lvl = self.users[author_id]['level']

        if cur_xp >= round((4 * (cur_lvl ** 3)) / 5):
            self.users[author_id]['level'] += 1
            return True
        else:
            return False

    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        author_id = str(message.author.id)

        if author_id in self.users:
            self.users[author_id] = {}
            self.users[author_id]['level'] = 1
            self.users[author_id]['exp'] = 0
        self.users[author_id]['exp'] += 1
        if self.lvl_up(author_id):
            await ctx.send(f"{message.author.mention} is not level {self.users[author_id]['level']}")

def setup(bot):
    bot.add_cog(Levels(bot))



    # try:
    #     with open("users.json") as fp:
    #         users = json.load(fp)
    # except Exception:
    #     users = {}
    #
    # def save_users(self):
    #     with open("users.json", "w+") as fp:
    #         json.dump(self.users, fp, sort_keys=True, indent=4)
    #
    # def add_points(self, user: discord.User, points: int):
    #     id = user.id
    #     if id not in self.users:
    #         self.users[id] = {}
    #     self.users[id]["points"] = self.users[id].get("points", 0) + points
    #     print("{} now has {} points".format(user.name, self.users[id]["points"]))
    #     self.save_users()
    #
    # def get_points(self, user: discord.User):
    #     id = user.id
    #     if id in self.users:
    #         return self.users[id].get("points", 0)
    #     return 0
    #
    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     if message.author == self.client.user:
    #         return
    #     print("{} sent a message".format(message.author.name))
    #     if message.content.lower().startswith("!points"):
    #         msg = "You have {} points!".format(self.get_points(message.author))
    #         await message.channel.send(msg)
    #     self.add_points(message.author, 1)
#     try:
#         with open("users.json") as fp:
#             users = json.load(fp)
#     except Exception:
#         users = {}
#
#     def save_users(self):
#         with open("users.json", "w+") as fp:
#             json.dump(self.users, fp, sort_keys=True, indent=4)
#
#     def add_points(self, user: discord.User, points : int):
#         id = user.id
#
#         if id not in self.users:
#             self.users[id] = {}
#             self.users[id]["level"] = self.users[id].get("level", 0) + points
#     #  print("{} now has {} level".format(user.name, users[id]["level"]))
#             self.save_users()
#
#     def get_points(self, user: discord.User):
#         id = user.id
#
#         if id in self.users:
#             return self.users[id].get("level", 0)
#         return 0
#
#     @commands.Cog.listener()
#     async def on_message(self,message):
#         if message.author == self.client.user:
#             return
#
#     # print("{} sent a message".format(message.author.name))
#     # if message.content.lower().startswith("!points"):
#     #     msg = "You have {} points!".format(get_points(message.author))
#     #     await client.send_message(message.channel, msg)
#         self.add_points(message.author, 1)
#
#         if message.content == '!Lvl':
#             msg = "Your Lvl {}!".format(self.get_points(message.author))
#             await message.channel.send(msg)
#
#
# def setup(client):
#     client.add_cog(Example(client))