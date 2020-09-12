import os
from discord.ext import commands
import subprocess
import time
from dotenv import load_dotenv

load_dotenv()
outputpath = os.getenv("OUTPUT")
moddedterraria = os.getenv("ModdedTerraria")
owner = os.getenv("OWNER_ID")


class ModdedTerraria(commands.Cog): # Note: This only works if the screen is named "moddedterraria" and bot is excuted but the same user who owns the screen

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mtsay(self, ctx, *, message=None):
        print('"Say" Command Issued')
        message = message
        subprocess.call('screen -S moddedterraria -p 0 -X stuff "say {}^M"'.format(message), shell=True)
        subprocess.call('screen -S moddedterraria -X hardcopy {}'.format(outputpath), shell=True)

        fileHandle = open(outputpath, "r")
        lineList = fileHandle.readlines()
        fileHandle.close()

        last = lineList[len(lineList) - 2]
        last = last.rstrip('\n')

        await ctx.send("__Modded Terraria Console__")
        await ctx.send(last)

    @commands.command()
    async def mtsave(self, ctx):
        print('"Save" Command Issued')
        subprocess.call('screen -S moddedterraria -p 0 -X stuff "save^M"', shell=True)
        time.sleep(1.5)
        subprocess.call('screen -S moddedterraria -X hardcopy {}'.format(outputpath), shell=True)

        fileHandle = open(outputpath, "r")
        lineList = fileHandle.readlines()
        fileHandle.close()

        last = lineList[len(lineList) - 2]
        last = last.rstrip('\n')

        await ctx.send("__Modded Terraria Console__")
        await ctx.send(last)

    @commands.command()
    async def mtplaying(self, ctx):
        print('"Playing" Command Issued')
        subprocess.call('screen -S moddedterraria -p 0 -X stuff "playing^M"', shell=True)
        subprocess.call('screen -S moddedterraria -X hardcopy {}'.format(outputpath), shell=True)

        fileHandle = open(outputpath, "r")
        lineList = fileHandle.readlines()
        fileHandle.close()

        last = lineList[len(lineList) - 2]
        last = last.rstrip('\n')

        await ctx.send("__Modded Terraria Console__")
        await ctx.send(last)

    @commands.command()
    async def mtseed(self, ctx):
        print('"seed" Command Issued')
        subprocess.call('screen -S moddedterraria -p 0 -X stuff "seed^M"', shell=True)
        subprocess.call('screen -S moddedterraria -X hardcopy {}'.format(outputpath), shell=True)

        fileHandle = open(outputpath, "r")
        lineList = fileHandle.readlines()
        fileHandle.close()

        last = lineList[len(lineList) - 2]
        last = last.rstrip('\n')

        await ctx.send("__Modded Terraria Console__")
        await ctx.send(last)

    @commands.command()
    async def mtstart(self, ctx):
        print("Starting Modded Terraria Server")
        subprocess.call('screen -dmS moddedterraria', shell=True)
        subprocess.call('screen -S moddedterraria -p 0 -X stuff ' +
                        f'"TERM=xterm {moddedterraria}/tModLoaderServer.bin.x86_64 -config {moddedterraria}/serverconfig.txt^M"',
                        shell=True)
        time.sleep(1)
        subprocess.call('screen -S moddedterraria -p 0 -X stuff help^M', shell=True)
        await ctx.send("Modded Terraria Server is starting.......")

    @commands.command()
    async def mtstop(self, ctx):
        print("Stopping Modded Terraria Server")
        subprocess.call('screen -S moddedterraria -p 0 -X stuff save^M', shell=True)
        time.sleep(1)
        subprocess.call('screen -S moddedterraria -p 0 -X stuff exit^M', shell=True)
        time.sleep(1)
        subprocess.call('screen -S moddedterraria -p 0 -X stuff exit^M', shell=True)
        await ctx.send("Modded Terraria Server has stopped")

    @commands.command()
    async def mtrestart(self, ctx):
        print("Restarting Modded Terraria Server")
        subprocess.call('screen -S moddedterraria -p 0 -X stuff save^M', shell=True)
        time.sleep(1)
        subprocess.call('screen -S moddedterraria -p 0 -X stuff exit^M', shell=True)
        time.sleep(1)
        subprocess.call('screen -S moddedterraria -p 0 -X stuff exit^M', shell=True)
        await ctx.send("Modded Terraria Server has stopped")
        time.sleep(0.5)
        subprocess.call('screen -dmS moddedterraria', shell=True)
        subprocess.call('screen -S moddedterraria -p 0 -X stuff ' +
                        f'"TERM=xterm {moddedterraria}/tModLoaderServer.bin.x86_64 -config {moddedterraria}/serverconfig.txt^M"',
                        shell=True)
        time.sleep(1)
        subprocess.call('screen -S moddedterraria -p 0 -X stuff help^M', shell=True)

        await ctx.send("Modded Terraria Server is starting.......")


def setup(bot):
    bot.add_cog(ModdedTerraria(bot))