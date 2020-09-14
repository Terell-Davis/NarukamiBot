import subprocess
import time
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
owner = os.getenv("OWNER_ID")
minecraft = os.getenv("Minecraft")
terraria = os.getenv("Terraria")
moddedterraria = os.getenv("ModdedTerraria")
outputpath = os.getenv("OUTPUT")


class ServerManager(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('ServerManager is loaded and ready to go!')

    @commands.command(name="say", pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def say(self, ctx, arg1, *, message=""):
        message = message
        if arg1 == "Minecraft":
            subprocess.call('screen -S minecraft -p 0 -X stuff "say {}^M"'.format(message), shell=True)
            time.sleep(0.5)
            subprocess.call('screen -S minecraft -X hardcopy {}'.format(outputpath), shell=True)

            fileHandle = open(outputpath, "r")
            lineList = fileHandle.readlines()
            fileHandle.close()
            last = lineList[len(lineList) - 2]
            last = last.rstrip('\n')

            await ctx.send("__Minecraft Server__")
            await ctx.send(f'{last}')

        elif arg1 == "Terraria":
            subprocess.call('screen -S terraria -p 0 -X stuff "say {}^M"'.format(message), shell=True)
            subprocess.call('screen -S terraria -X hardcopy {}'.format(outputpath), shell=True)

            fileHandle = open(outputpath, "r")
            lineList = fileHandle.readlines()
            fileHandle.close()

            last = lineList[len(lineList) - 2]
            last = last.rstrip('\n').replace(':', '')

            await ctx.send("__Terraria Server__")
            await ctx.send(f'{last}')

        elif arg1 == "MTerraria":
            subprocess.call('screen -S moddedterraria -p 0 -X stuff "say {}^M"'.format(message), shell=True)
            subprocess.call('screen -S moddedterraria -X hardcopy {}'.format(outputpath), shell=True)

            fileHandle = open(outputpath, "r")
            lineList = fileHandle.readlines()
            fileHandle.close()

            last = lineList[len(lineList) - 2]
            last = last.rstrip('\n').replace(':', '')
            await ctx.send("__Modded Terraria Server__")
            await ctx.send(f'{last}')

        elif arg1 == "":
            await ctx.send("Please specify which server to send the command!")

        else: # arg1 != "Minecraft" or "Terraria" or "MTerraria":
            await ctx.send(f'{arg1} Server not found!')
        print(f'{arg1}: "Say" Command Issued')

    @commands.command(name="save", pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def save(self, ctx, arg1):
        if arg1 == "Minecraft":
            subprocess.call('screen -S minecraft -p 0 -X stuff "save-all^M"', shell=True)
            time.sleep(1.5)
            subprocess.call('screen -S minecraft -X hardcopy {}'.format(outputpath), shell=True)

            fileHandle = open(outputpath, "r")
            lineList = fileHandle.readlines()
            fileHandle.close()

            last = lineList[len(lineList) - 2]
            last = last.rstrip('\n')

            await ctx.send("__Minecraft Server__")
            await ctx.send(f'{last}')

        elif arg1 == "Terraria":
            subprocess.call('screen -S terraria -p 0 -X stuff "save^M"', shell=True)
            time.sleep(1.5)
            subprocess.call('screen -S terraria -X hardcopy {}'.format(outputpath), shell=True)

            fileHandle = open(outputpath, "r")
            lineList = fileHandle.readlines()
            fileHandle.close()

            last = lineList[len(lineList) - 2]
            last = last.rstrip('\n').replace(':', '')

            await ctx.send("__Terraria Server__")
            await ctx.send(f'{last}')

        elif arg1 == "MTerraria":
            subprocess.call('screen -S moddedterraria -p 0 -X stuff "save^M"', shell=True)
            time.sleep(1.5)
            subprocess.call('screen -S moddedterraria -X hardcopy {}'.format(outputpath), shell=True)

            fileHandle = open(outputpath, "r")
            lineList = fileHandle.readlines()
            fileHandle.close()

            last = lineList[len(lineList) - 2]
            last = last.rstrip('\n').replace(':', '')

            await ctx.send("__Modded Terraria Server__")
            await ctx.send(f'{last}')
        elif arg1 == "":
            await ctx.send("Please specify which server to send the command!")

        else:  # arg1 != "Minecraft" or "Terraria" or "MTerraria":
            await ctx.send(f'{arg1} Server not found!')
        print(f'{arg1}: "Save" Command Issued')

    @commands.command(name="playing", pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def playing(self, ctx, arg1):
        if arg1 == "Minecraft":
            subprocess.call('screen -S minecraft -p 0 -X stuff "list^M"', shell=True)
            time.sleep(0.5)
            subprocess.call('screen -S minecraft -X hardcopy {}'.format(outputpath), shell=True)

            fileHandle = open(outputpath, "r")
            lineList = fileHandle.readlines()
            fileHandle.close()

            last = lineList[len(lineList) - 1]
            last = last.rstrip('\n')

            if last == "":
                last = lineList[len(lineList) - 1]
                last = last.rstrip('\n')

                await ctx.send("__Minecraft Server__")
                await ctx.send(f'{last}')
            else:
                await ctx.send("__Minecraft Server__")
                await ctx.send(f'{last}')

        elif arg1 == "Terraria":
            subprocess.call('screen -S terraria -p 0 -X stuff "playing^M"', shell=True)
            subprocess.call('screen -S terraria -X hardcopy {}'.format(outputpath), shell=True)

            fileHandle = open(outputpath, "r")
            lineList = fileHandle.readlines()
            fileHandle.close()

            last = lineList[len(lineList) - 2]
            last = last.rstrip('\n').replace(':', '')

            await ctx.send("__Terraria Server__")
            await ctx.send(f'{last}')

        elif arg1 == "MTerraria":
            subprocess.call('screen -S moddedterraria -p 0 -X stuff "playing^M"', shell=True)
            subprocess.call('screen -S moddedterraria -X hardcopy {}'.format(outputpath), shell=True)

            fileHandle = open(outputpath, "r")
            lineList = fileHandle.readlines()
            fileHandle.close()

            last = lineList[len(lineList) - 2]
            last = last.rstrip('\n').replace(':', '')
            await ctx.send("__Modded Terraria Server__")
            await ctx.send(f'{last}')

        elif arg1 == "":
            await ctx.send("Please specify which server to send the command!")

        else:  # arg1 != "Minecraft" or "Terraria" or "MTerraria":
            await ctx.send(f'{arg1} Server not found!')
        print(f'{arg1}: "Playing" Command Issued')

    @commands.command(name="seed", pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def seed(self, ctx, arg1):
        if arg1 == "Minecraft":
            subprocess.call('screen -S minecraft -p 0 -X stuff "seed^M"', shell=True)
            time.sleep(0.5)
            subprocess.call('screen -S minecraft -X hardcopy {}'.format(outputpath), shell=True)

            fileHandle = open(outputpath, "r")
            lineList = fileHandle.readlines()
            fileHandle.close()

            last = lineList[len(lineList) - 1]
            last = last.rstrip('\n')

            if last == "":
                last = lineList[len(lineList) - 1]
                last = last.rstrip('\n')

                await ctx.send("__Minecraft Server__")
                await ctx.send(f'{last}')
            else:
                await ctx.send("__Minecraft Server__")
                await ctx.send(f'{last}')

        elif arg1 == "Terraria":
            subprocess.call('screen -S terraria -p 0 -X stuff "seed^M"', shell=True)
            subprocess.call('screen -S terraria -X hardcopy {}'.format(outputpath), shell=True)

            fileHandle = open(outputpath, "r")
            lineList = fileHandle.readlines()
            fileHandle.close()

            last = lineList[len(lineList) - 2]
            last = last.rstrip('\n').replace(':', '')

            await ctx.send("__Terraria Server__")
            await ctx.send(f'{last}')

        elif arg1 == "MTerraria":
            subprocess.call('screen -S moddedterraria -p 0 -X stuff "seed^M"', shell=True)
            subprocess.call('screen -S moddedterraria -X hardcopy {}'.format(outputpath), shell=True)

            fileHandle = open(outputpath, "r")
            lineList = fileHandle.readlines()
            fileHandle.close()

            last = lineList[len(lineList) - 2]
            last = last.rstrip('\n').replace(':', '')
            await ctx.send("__Modded Terraria Server__")
            await ctx.send(f'{last}')

        elif arg1 == "":
            await ctx.send("Please specify which server to send the command!")

        else:  # arg1 != "Minecraft" or "Terraria" or "MTerraria":
            await ctx.send(f'{arg1} Server not found!')
        print(f'{arg1}: "Seed" Command Issued')


def setup(bot):
    bot.add_cog(ServerManager(bot))
