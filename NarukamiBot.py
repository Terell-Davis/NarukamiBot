import discord
from discord.ext import commands
import logging
from pathlib import Path
import os

from discord.ext.commands import CommandNotFound, MissingPermissions, MissingRequiredArgument
from dotenv import load_dotenv
cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"\nWorking dir:{cwd}")

load_dotenv()
owner = int(os.getenv("OWNER_ID"))
prefix = os.getenv("PREFIX")
bot = commands.Bot(command_prefix=prefix, case_insensitive=True)
logging.basicConfig(level=logging.INFO)


@bot.event
async def on_ready():
    print(f'{bot.user.name} with id:{bot.user.id} is now ready!\nCurrent bot prefix is: {prefix}') # Just for the terminal
    print(f'The current owner id is: {owner}')
    await bot.change_presence(activity=discord.Game(name=f"Persona 5 Royal {prefix}help")) # Sets Status
    #  await bot.change_presence(activity=discord.Game(name=f"Phoenix Wright: Ace Attorney")) # Used for upcoming AdachiBot


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingRequiredArgument):
        await ctx.send(f'{ctx.author}, you are missing 1 or more arguments for this command!')
        return
    elif isinstance(error, MissingPermissions):
        await ctx.send(f'{ctx.author} does not have permission for this command!')
        return
    elif isinstance(error, CommandNotFound):
        await ctx.send(f'Command not found, Use {prefix}help to see a list of avaiable commands.')
        return
    raise error


@bot.command(pass_context=True)
async def load(ctx, extension=''):
    if ctx.message.author.id == owner:
        if extension == '':
            await ctx.send("Please enter the Category to load")
        else:
            bot.load_extension(f'cogs.{extension}')
    else:
        await ctx.send("You do not have permission for this command")


@bot.command(pass_context=True)
async def reload(ctx, extension=''):
    if ctx.message.author.id == owner:
        if extension == '':
            await ctx.send("Please enter the Category to reload")
        else:
            bot.unload_extension(f'cogs.{extension}')
            bot.load_extension(f'cogs.{extension}')
            await ctx.send(f'Reloading {extension}')
    else:
        await ctx.send("You do not have permission for this command")


@bot.command()
async def unload(ctx, extension=''):
    if ctx.message.author.id == owner:
        if extension == '':
            await ctx.send("Please enter the Category to load")
        else:
            bot.unload_extension(f'cogs.{extension}')
    else:
        await ctx.send("You do not have permission for this command")


@bot.command()
async def shutdown(ctx):
    if ctx.author.id == owner:
        message = f'{ctx.author} is authorized, Shutting Down Bot......'
        await ctx.send(message)
        await bot.logout()
        await bot.close()
    else:
        await ctx.send(f'{ctx.author} is not authorized to shut down this bot')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.getenv("TOKEN"))  # Turns the bot on
