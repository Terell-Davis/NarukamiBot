import discord
from discord.ext import commands
import logging
from pathlib import Path
import json

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

secret_file = json.load(open(cwd + '/bot_config/hidden.json'))
bot = commands.Bot(command_prefix='n!', case_insensitive=True)
bot.config_token = secret_file['token']
logging.basicConfig(level=logging.INFO)


@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is: n!\n-----")
    # Another way to use variables in strings
    # print("-----\nLogged in as: {} : {}\n-----\nMy current prefix is: n!\n-----".format(bot.user.name, bot.user.id))
    await bot.change_presence(activity=discord.Game(name=f"Persona 5 Royal n!"))


@bot.command(name='hi', aliases=['hello'])
async def _hi(ctx):
    """
    A simple command which says hi to the author.
    """
    await ctx.send(f"Hi {ctx.author.mention}!")
    # Another way to do this code is (user object).mention
    # await ctx.send(f"Hi <@{ctx.author.id}>!")


@bot.command()
async def echo(ctx, *, message=None):
    """
    A simple command that repeats the users input back to them.
    """
    message = message or "Please provide the message to be repeated."
    await ctx.message.delete()
    await ctx.send(message)


bot.run(bot.config_token)  # Turns the bot on
