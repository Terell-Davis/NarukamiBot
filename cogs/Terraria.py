import os
from discord.ext import commands
import subprocess
import time
from dotenv import load_dotenv

load_dotenv()
path = os.getenv("OUTPUT")


class Terraria(commands.Cog): # Note: This only works if the screen is named "terraria" and bot is excuted but the same user who owns the screen

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tsay(self, ctx, *, message=None):
        print('"Say" Command Issued')
        message = message
        subprocess.call('screen -S terraria -p 0 -X stuff "say {}^M"'.format(message), shell=True)
        subprocess.call('screen -S terraria -X hardcopy {}'.format(path), shell=True)

        fileHandle = open(path, "r")
        lineList = fileHandle.readlines()
        fileHandle.close()

        last = lineList[len(lineList) - 2]
        last = last.rstrip('\n')

        await ctx.send("__Terraria Console__")
        await ctx.send(last)

    @commands.command()
    async def tsave(self, ctx):
        print('"Save" Command Issued')
        subprocess.call('screen -S terraria -p 0 -X stuff "save^M"', shell=True)
        time.sleep(1.5)
        subprocess.call('screen -S terraria -X hardcopy {}'.format(path), shell=True)

        fileHandle = open(path, "r")
        lineList = fileHandle.readlines()
        fileHandle.close()

        last = lineList[len(lineList) - 2]
        last = last.rstrip('\n')

        await ctx.send("__Terraria Console__")
        await ctx.send(last)

    @commands.command()
    async def tplaying(self, ctx):
        print('"Playing" Command Issued')
        subprocess.call('screen -S terraria -p 0 -X stuff "playing^M"', shell=True)
        subprocess.call('screen -S terraria -X hardcopy {}'.format(path), shell=True)

        fileHandle = open(path, "r")
        lineList = fileHandle.readlines()
        fileHandle.close()

        last = lineList[len(lineList) - 2]
        last = last.rstrip('\n')

        await ctx.send("__Terraria Console__")
        await ctx.send(last)

    @commands.command()
    async def tseed(self, ctx):
        print('"seed" Command Issued')
        subprocess.call('screen -S terraria -p 0 -X stuff "seed^M"', shell=True)
        subprocess.call('screen -S terraria -X hardcopy {}'.format(path), shell=True)

        fileHandle = open(path, "r")
        lineList = fileHandle.readlines()
        fileHandle.close()

        last = lineList[len(lineList) - 2]
        last = last.rstrip('\n')

        await ctx.send("__Terraria Console__")
        await ctx.send(last)


def setup(bot):
    bot.add_cog(Terraria(bot))