import os
from discord.ext import commands
import subprocess
import time
from dotenv import load_dotenv

load_dotenv()
outputpath = os.getenv("OUTPUT")
minecraft = os.getenv("Minecraft")
owner = os.getenv("OWNER_ID")


class Minecraft(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def msay(self, ctx, *, message=None):
        print('"Say" Command Issued')
        message = message
        subprocess.call('screen -S minecraft -p 0 -X stuff "say {}^M"'.format(message), shell=True)
        time.sleep(0.5)
        subprocess.call('screen -S minecraft -X hardcopy {}'.format(outputpath), shell=True)

        fileHandle = open(outputpath, "r")
        lineList = fileHandle.readlines()
        fileHandle.close()

        last = lineList[len(lineList) - 2]
        last = last.rstrip('\n')

        await ctx.send("__Minecraft Console__")
        await ctx.send(last)

    @commands.command()
    async def msave(self, ctx):
        print('"Save" Command Issued')
        subprocess.call('screen -S minecraft -p 0 -X stuff "save-all^M"', shell=True)
        time.sleep(1.5)
        subprocess.call('screen -S minecraft -X hardcopy {}'.format(outputpath), shell=True)

        fileHandle = open(outputpath, "r")
        lineList = fileHandle.readlines()
        fileHandle.close()

        last = lineList[len(lineList) - 2]
        last = last.rstrip('\n')

        await ctx.send("__Minecraft Console__")
        await ctx.send(last)

    @commands.command()
    async def mplaying(self, ctx):
        print('"Playing" Command Issued')
        subprocess.call('screen -S minecraft -p 0 -X stuff "list^M"', shell=True)
        time.sleep(0.5)
        subprocess.call('screen -S minecraft -X hardcopy {}'.format(outputpath), shell=True)

        fileHandle = open(outputpath, "r")
        lineList = fileHandle.readlines()
        fileHandle.close()

        last = lineList[len(lineList) - 1]
        last = last.rstrip('\n')

        if last == "":
            last = lineList[len(lineList) -1]
            last = last.rstrip('\n')

            await ctx.send("__Minecraft Server__")
            await ctx.send(last)
        else:
            await ctx.send("__Minecraft Server__")
            await ctx.send(last)

    @commands.command()
    async def mseed(self, ctx):
        print('"seed" Command Issued')
        subprocess.call('screen -S minecraft -p 0 -X stuff "seed^M"', shell=True)
        time.sleep(0.5)
        subprocess.call('screen -S minecraft -X hardcopy {}'.format(outputpath), shell=True)

        fileHandle = open(outputpath, "r")
        lineList = fileHandle.readlines()
        fileHandle.close()

        last = lineList[len(lineList) - 2]
        last = last.rstrip('\n')

        await ctx.send("__Minecraft Console__")
        await ctx.send(last)

    @commands.command()
    async def mstart(self, ctx):
        print("Starting Minecraft Server")
        subprocess.call('screen -dmS minecraft', shell=True)
        subprocess.call(f'screen -S minecraft -p 0 -X stuff "cd {minecraft}^M"', shell=True)
        time.sleep(0.5)
        subprocess.call('screen -S minecraft -p 0 -X stuff ' +
                        f'"java -Xms2048M -Xmx4096M -jar server.jar nogui^M"',
                        shell=True)
        time.sleep(5)
        subprocess.call('screen -S minecraft -p 0 -X stuff help^M', shell=True) # This is cheating to fill up console
        await ctx.send("Minecraft Server is starting.......")

    @commands.command()
    async def mstop(self, ctx):
        print("Stopping Minecraft Server")
        subprocess.call('screen -S minecraft -p 0 -X stuff save-all^M', shell=True)
        time.sleep(3)
        subprocess.call('screen -S minecraft -p 0 -X stuff stop^M', shell=True)
        time.sleep(3)
        subprocess.call('screen -S minecraft -p 0 -X stuff exit^M', shell=True)
        await ctx.send("Minecraft Server has stopped")

    @commands.command()
    async def mrestart(self, ctx):
        print("Restarting Minecraft Server")
        subprocess.call('screen -S minecraft -p 0 -X stuff save-all^M', shell=True)
        time.sleep(5)
        subprocess.call('screen -S minecraft -p 0 -X stuff stop^M', shell=True)
        time.sleep(5)
        subprocess.call('screen -S minecraft -p 0 -X stuff exit^M', shell=True)
        await ctx.send("Minecraft Server has stopped")
        time.sleep(0.5)
        subprocess.call('screen -dmS minecraft', shell=True)
        subprocess.call(f'screen -S minecraft -p 0 -X stuff "cd {minecraft}^M"', shell=True)
        subprocess.call('screen -S minecraft -p 0 -X stuff ' +
                        f'"java -Xms2048M -Xmx4096M -jar server.jar nogui^M"',
                        shell=True)
        time.sleep(1)
        subprocess.call('screen -S minecraft -p 0 -X stuff help^M', shell=True)

        await ctx.send("Minecraft Server is starting.......")


def setup(bot):
    bot.add_cog(Minecraft(bot))