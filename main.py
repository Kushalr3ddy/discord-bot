import discord
from discord.ext import commands
from BOT_TOKEN import *
import wikipedia

client = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
    print(f"logged in as {client.user}")
    print(f"on {str(len(client.servers))}")
@client.command()
async def hello(ctx):
    await ctx.send(f"hello there {str(ctx.author)}")

@client.command()
async def clear(ctx,no = 1):
    await ctx.channel.purge(limit=no+1)

@client.command()
async def wiki(ctx,search=None,lines=3):
    try:
        if search ==None:
            await ctx.send("usage:\n>wiki <search> <no-of-sentences-to-be-displayed>")
        else:
            await ctx.send(f"{wikipedia.summary(search,lines)}")
    except:
        await ctx.send("search not available")


client.run(bot_token)