
from tkn import token
import discord
from discord import message,Member
from discord.ext import commands
from discord.ext.commands import Greedy
from random import randint,choice
from tester import check
import keep_alive
import wikipedia
from datetime.datetime import now
mods = []
cmd =""
client = commands.Bot(command_prefix= ";")
#####events
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,activity=discord.Game("under testing do not ping"))
    print(f"logged in as {client.user}")

@client.event
async def on_message(ctx):
    if str(ctx.author) == str(client.user):
        return
    if str(ctx.author) in mods:
        return

    #print(f"{now.strftime("%d/%m/%Y %H:%M:%S")}|{ctx.author}:{ctx.author.id}:{ctx.content}")
    file1 = open("myfile.txt", "a")  # append mode 
    file1.write(f"{ctx.author}:{ctx.content}\n") 
    result = check(str(ctx.content))
    if result == True:
        #await ctx.channel.send(f"Thats some strong language {ctx.author.mention}")
        #me = await client.get_user_info(ctx.author)
        #await ctx.author.send(content='seems like you used some strong language in the server{}\n{}'.format(ctx.author.mention,ctx.content))
        #await ctx.send_message(ctx.author, "#The message")
        pass
    await client.process_commands(ctx)

###

#####commands
@client.command()
async def hello(ctx):
    """returns hello"""
    await ctx.send(f"hello there {ctx.author}")

@client.command()
async def joined(ctx,member:discord.Member):
    """Shows when a user joined the server"""
    await ctx.send(f"{member.name} joined on {member.joined_at}")

@client.command()
async def repeat(ctx,message):
    """Repeats a message
    usage:\n;repeat <your-message>"""
    await ctx.send(message)

@client.command()
async def roll(ctx):
    """random number between 1 to 100"""
    await ctx.send(f"{ctx.author} rolled a {randint(1,101)}")

@client.command()
async def flip(ctx):
    """flips a coin\nreturns heads or tails"""
    coin = ["heads","tails"]
    await ctx.send(f"{ctx.author} flipped {choice(coin)}")
@client.command()
async def source(ctx):
    await ctx.send("https://repl.it/@KushalReddy1/SmugFearfulGlitch")


###


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount=1):
    """clears specified no of messages (default is 1)\n
    usage: ;clear <no-of-messages>"""
    await ctx.channel.purge(limit=amount+1)


@client.command()
async def  wiki(ctx,query,lines=2):
    """does wikipedia search"""
    try:
        if len(query) == 0:
            await ctx.send("usage ;wiki [search]")
        else:
            await ctx.send(wikipedia.summary(query,lines))
    except:
        return
        #await ctx.send("search not found or some error has occured")
######error_handling
@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("arguments missing")
    elif isinstance(error,commands.MissingPermissions):
        await ctx.send("you're not allowed to do that")
    elif isinstance(error,commands.CommandNotFound):
        await ctx.send("command not found\ntype ;help for more info")




keep_alive.keep_alive()
client.run(token)
    