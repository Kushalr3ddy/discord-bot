import discord
import os
from discord import message, member
from BOT_TOKEN import member_list,bot_token
from discord.ext import commands,tasks
from itertools import cycle
from HEADERS import headers


#client = commands.Bot(command_prefix ="!")#mcbot
client = commands.Bot(command_prefix =".")#codebot
status = cycle(["status 1","status 2"])



@client.event
async def on_ready():
    #change_status.start()
    await client.change_presence(status=discord.Status.online,activity=discord.Game(".help"))
    print(f"logged in as {client.user}")

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("arguments missing")
    elif isinstance(error,commands.MissingPermissions):
        await ctx.send("you're not allowed to do that")
    elif isinstance(error,commands.CommandNotFound):
        await ctx.send("command not found\ntype !help for more info")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx,member:discord.Member,*,reason =None):
    if str(member) in member_list :
        await ctx.send("not allowed to kick moderators")
    elif str(member) == client.user:
        await ctx.send("not allowed to kick me")
    else:
        await member.kick(reason =reason)
        await ctx.send(f"kicked {member.mention}")

'''
########not to be used untill required######

@client.command()
async def ban(ctx,member:discord.Member,*,reason =None):
    print(f"{member} has been banned")
    if str(member) in member_list:
        await ctx.send("youre not allowed to do that")#
    else:
        await member.ban(reason =reason)
        
'''

@client.command()
async def hello(ctx):
    await ctx.send(f"hello")

@client.command()
async def HELLO(ctx):
    
    await ctx.send(f"hello there ")


@client.command()
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, discriminator = member.split("#")
    for i in banned_users:
        user = i.user
        if (user.name,user.discriminator) == (member_name,discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"unbanned {user.mention}")
            return

@client.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined in {member.joined_at}'

"""
@commands.group(invoke_without_command=True)
async def your_command_name(self, ctx):
    do_your_functions()

@your_command_name.command()
async def sub_command_name(self, ctx):
    do_your_subcommand()
"""

'''
##########Cogs########

@client.command()
async def load(ctx,extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx,extension):
    client.unload_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


####task_loop#####
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@clear.error
async def clear_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("please specify an amount of messages to delete")

def checker_function(ctx):
    return ctx.author.id == "idfromdiscord"

@client.command()
@commmand.checks(check_function)
async def function_name():
    functions()
'''
"""@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount=1):
    await ctx.channel.purge(limit=amount+1)"""

    )
client.run(bot_token)