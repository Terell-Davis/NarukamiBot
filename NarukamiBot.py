import discord
from discord.ext import commands
import logging
from pathlib import Path
import os
from dotenv import load_dotenv
cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

load_dotenv()
owner = os.getenv("OWNER_ID")
prefix = os.getenv("PREFIX")
bot = commands.Bot(command_prefix=prefix, case_insensitive=True)
logging.basicConfig(level=logging.INFO)



@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is: {prefix}\n-----")
    await bot.change_presence(activity=discord.Game(name=f"Persona 5 Royal n!help")) # Sets Presence


@bot.command()
async def load(ctx, extension):
    if extension == '':
        await ctx.send("Please enter the Category to load")
    else:
        bot.load_extension(f'cogs.{extension}')


@bot.command()
async def reload(ctx, extension):
    if extension == '':
        await ctx.send("Please enter the Category to reload")
    else:
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    if extension == '':
        await ctx.send("Please enter the Category to load")
    else:
        bot.unload_extension(f'cogs.{extension}')


def is_owner(ctx):
    return ctx.author.id == owner


@bot.command()
async def shutdown(ctx):
    message = f'{ctx.author} is not authorized to shutdown this bot!'
    if ctx.author.id == owner:
        message = f'{ctx.author} is authorized, Shutting Down Bot......'
        await ctx.send(message)
        await bot.close()
    else:
        await ctx.send(message)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.getenv("TOKEN"))  # Turns the bot on
