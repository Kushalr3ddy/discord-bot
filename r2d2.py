import discord
from discord import message,Member
from discord.ext import commands
from random import randint,choice
import keep_alive
import wikia

danbot_token = "Nzc3NzkzNjU3MzQwMjk3MjM2.X7Imyg.6NidwiHIDFMdMnP2tRTICC0UGJo"
client = commands.Bot(command_prefix=">")
#####events
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,activity=discord.Game("krunker.io| >help"))
    print(f"logged in as {client.user}")

@client.event
async def on_message(ctx):
    if ctx.author == client.user:
        return
    print(f"{ctx.author}:{ctx.content}")
    file1 = open("myfile.txt", "a")  # append mode 
    file1.write(f"{ctx.author}:{ctx.content}") 
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
    usage: >repeat <your-message>"""
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
async def yt(ctx):
    """Zoom link for classes"""
    await ctx.send("https://zoom.us/j/95398188063?pwd=T3pOeWFlS1JxaG03WkNibHJVT3Fldz09")###

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount=1):
    """clears specified no of messages (default is 1)\n
    usage: >clear <no-of-messages>"""
    await ctx.channel.purge(limit=amount+1)

@client.command()
async def nudge(ctx, users: discord.ext.commands.Greedy[discord.User]):
    #user = await bot.get_user_info(user_id)
    #link = await ctx.channel.create_invite(max_age = 300)
    for user in users:
        await user.send(f"{ctx.author} nudged you")
        #await user.send(link)

######error_handling
@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("arguments missing")
    elif isinstance(error,commands.MissingPermissions):
        await ctx.send("you're not allowed to do that")
    elif isinstance(error,commands.CommandNotFound):
        await ctx.send("command not found\ntype >help for more info")




keep_alive.keep_alive()
client.run(bot_token)
    