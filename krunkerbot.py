import discord
from discord.ext import commands
from BOT_TOKEN import *
from krunker import *
import requests

def get_prefix(client,message):
    with open("prefixes.json","r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix = '>')#commands.when_mentioned_or("."))

@client.event
async def on_ready():
    print(f"logged in as {client.user}")

@client.event
async def on_command_error(ctx,error):
    await ctx.send(error)

@client.command()
async def clear(ctx,amount=1):
    await ctx.channel.purge(limit=amount+1)

@client.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx.author}")

@client.command()
async def menu(ctx):
    j = []
    for i in menu_items:
        await ctx.send(f"{i.text}")
#    for _ in j:
#        await ctx.send(_)



@client.command()
async def classes(ctx):
    for i in class_img:
        await ctx.send(i.get("src"))
    await ctx.send(18*"_")



client.run(krunkbot_token)
