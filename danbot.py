import discord
from discord import message,Member
from discord.ext import commands
from random import randint
import wikia
#link = "https://www.youtube.com/channel/UClvm_DttrJH83mKYV6T16Kw?sub_confirmation=1"
danbot_token = "Nzc3NzkzNjU3MzQwMjk3MjM2.X7Imyg.5O75n829r-yeuIEQDIWR0XLxgA4"
client = commands.Bot(command_prefix=">")
#####events
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,activity=discord.Game("krunker.io"))
    print(f"logged in as {client.user}")
###

#####commands
@client.command()
async def hello(ctx):
    await ctx.send(f"hello there {ctx.author}")

@client.command()
async def joined(ctx,member:discord.Member):
    await ctx.send(f"{member.name} joined on {member.joined_at}")

@client.command()
async def repeat(ctx,message):
    """Repeats a message multiple times."""
    await ctx.send(message)

@client.command()
async def roll(ctx):
    await ctx.send(randint(1,101))
###

######error_handling
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount=1):
    await ctx.channel.purge(limit=amount+1)
@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("arguments missing")
    elif isinstance(error,commands.MissingPermissions):
        await ctx.send("you're not allowed to do that")
    elif isinstance(error,commands.CommandNotFound):
        await ctx.send("command not found\ntype >help for more info")
###

client.run(danbot_token)
    