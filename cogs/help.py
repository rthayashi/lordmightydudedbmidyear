import discord
from discord.ext import commands
class help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(add_reactions=True,embed_links=True)
    async def help(self,ctx):
        author = ctx.message.author

        embed = discord.Embed(
            color = ctx.author.color, timestamp=ctx.message.created_at
        )

        embed.set_author(name= 'Help', icon_url=ctx.author.avatar_url)

        embed.add_field(name="level", value = "Displays user level current xp and required xp for next level", inline = False)
        embed.add_field(name="clear (#)", value = "Will delete # amount of messages not including itself", inline = False)
        embed.add_field(name="userinfo (member)", value = "Displays user info", inline = False)
        embed.add_field(name="help", value = "It is literally the command you are using", inline = False)
        embed.add_field(name="load (cog name)", value = "Loads the cog that is specified", inline = False)
        embed.add_field(name="unload (cog name)", value = "Unloads the cog that is specified", inline = False)
        embed.add_field(name="kick (user)", value = "Kicks user", inline = False)
        embed.add_field(name="ban (user)", value = "Bans user", inline = False)
        embed.add_field(name="unban (user)", value = "Unbans user", inline = False)


        await ctx.send(embed=embed)
        await ctx.message.add_reaction(emoji='✉')

def setup(client):
    client.remove_command("help")
    client.add_cog(help(client))