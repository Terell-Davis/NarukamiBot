import os
from discord.ext import commands
import subprocess
import time
from dotenv import load_dotenv

load_dotenv()
outputpath = os.getenv("OUTPUT")
terraria = os.getenv("Terraria")
owner = os.getenv("OWNER_ID")


class Terraria(commands.Cog):  # Note: This only works if the screen is named "terraria" and bot is executed but the same user who owns the screen

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tsay(self, ctx, *, message=None):
        print('"Say" Command Issued')
        message = message
        subprocess.call('screen -S terraria -p 0 -X stuff "say {}^M"'.format(message), shell=True)
        subprocess.call('screen -S terraria -X hardcopy {}'.format(outputpath), shell=True)

        fileHandle = open(outputpath, "r")
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
        subprocess.call('screen -S terraria -X hardcopy {}'.format(outputpath), shell=True)

        fileHandle = open(outputpath, "r")
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
        subprocess.call('screen -S terraria -X hardcopy {}'.format(outputpath), shell=True)

        fileHandle = open(outputpath, "r")
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
        subprocess.call('screen -S terraria -X hardcopy {}'.format(outputpath), shell=True)

        fileHandle = open(outputpath, "r")
        lineList = fileHandle.readlines()
        fileHandle.close()

        last = lineList[len(lineList) - 2]
        last = last.rstrip('\n')

        await ctx.send("__Terraria Console__")
        await ctx.send(last)

    @commands.command()
    async def tstart(self, ctx):
        print("Starting Terraria Server")
        subprocess.call('screen -dmS terraria', shell=True)
        subprocess.call('screen -S terraria -p 0 -X stuff ' +
                        fr'"TERM=xterm {terraria}/TerrariaServer.bin.x86_64 -config {terraria}/serverconfig.txt^M"',
                        shell=True)
        time.sleep(1)
        subprocess.call('screen -S terraria -p 0 -X stuff help^M', shell=True)
        await ctx.send("Terraria Server is starting.......")

    @commands.command()
    async def tstop(self, ctx):
        print("Stopping Terraria Server")
        subprocess.call('screen -S terraria -p 0 -X stuff save^M', shell=True)
        time.sleep(1)
        subprocess.call('screen -S terraria -p 0 -X stuff exit^M', shell=True)
        time.sleep(1)
        subprocess.call('screen -S terraria -p 0 -X stuff exit^M', shell=True)
        await ctx.send("Terraria Server has stopped")

    @commands.command()
    async def trestart(self, ctx):
        print("Restarting Terraria Server")
        subprocess.call('screen -S terraria -p 0 -X stuff save^M', shell=True)
        time.sleep(1)
        subprocess.call('screen -S terraria -p 0 -X stuff exit^M', shell=True)
        time.sleep(1)
        subprocess.call('screen -S terraria -p 0 -X stuff exit^M', shell=True)
        await ctx.send("Terraria Server has stopped")
        time.sleep(0.5)
        subprocess.call('screen -dmS terraria', shell=True)
        subprocess.call('screen -S terraria -p 0 -X stuff ' +
                        f'"TERM=xterm {terraria}/TerrariaServer.bin.x86_64 -config {terraria}/serverconfig.txt^M"',
                        shell=True)
        time.sleep(1)
        subprocess.call('screen -S terraria -p 0 -X stuff help^M', shell=True)

        await ctx.send("Terraria Server is starting.......")


def setup(bot):
    bot.add_cog(Terraria(bot))
