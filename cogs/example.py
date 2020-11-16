import discord 
from discord.ext import commands

class Example(commands.Cog):
    def __init__(self,client):
        self.client = client
    #events
    @commands.Cog.listener()
    async def on_ready(self):
        print("bot is online")
        
    #commands
    @commands.command()
    async def ping(self,ctx):
        await ctx.send("pong")

    @commands.group(invoke_without_command=True)
    async def query(self, ctx):
        await ctx.send("choose")

    @query.command()
    async def ask(self, ctx):
        await ctx.send("y/n")


def setup(client):
    client.add_cog(Example(client))
    
