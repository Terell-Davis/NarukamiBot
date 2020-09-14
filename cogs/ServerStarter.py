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


class ServerStarter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('ServerStarter is loaded and ready to go!')

    @commands.command(name="start", pass_context=True)
    @commands.has_permissions(administrator=True)
    async def start(self, ctx, arg1):
        if arg1 == "Minecraft":
            subprocess.call('screen -dmS minecraft', shell=True)
            subprocess.call(f'screen -S minecraft -p 0 -X stuff "cd {minecraft}^M"', shell=True)
            time.sleep(0.5)
            subprocess.call(f'screen -S minecraft -p 0 -X stuff ' +
                            f'"java -Xms{os.getenv("MinecraftMin")} -Xmx{os.getenv("MinecraftMax")} ' +
                            f'-jar {os.getenv("ServerJarName")} nogui^M"', shell=True)
            time.sleep(8)
            subprocess.call('screen -S minecraft -p 0 -X stuff help^M', shell=True) # This is to fill the screen so that hardcopy works properly
            await ctx.send("**Minecraft Server Started!**")

        elif arg1 == "Terraria":
            subprocess.call('screen -dmS terraria', shell=True)
            subprocess.call('screen -S terraria -p 0 -X stuff ' +
                            f'"TERM=xterm {terraria}/TerrariaServer.bin.x86_64 -config {terraria}/serverconfig.txt^M"',
                            shell=True)
            time.sleep(1)
            subprocess.call('screen -S terraria -p 0 -X stuff help^M', shell=True)
            await ctx.send("**Terraria Server Started!**")

        elif arg1 == "MTerraria":
            subprocess.call('screen -dmS moddedterraria', shell=True)
            subprocess.call('screen -S moddedterraria -p 0 -X stuff ' +
                            f'"TERM=xterm {moddedterraria}/tModLoaderServer.bin.x86_64^M"', shell=True)
            time.sleep(10)
            subprocess.call('screen -S moddedterraria -p 0 -X stuff 1^M', shell=True)
            subprocess.call('screen -S moddedterraria -p 0 -X stuff 8^M', shell=True)
            subprocess.call('screen -S moddedterraria -p 0 -X stuff 7777^M', shell=True)
            subprocess.call('screen -S moddedterraria -p 0 -X stuff ^M', shell=True)
            time.sleep(10)
            subprocess.call('screen -S moddedterraria -p 0 -X stuff help^M', shell=True)
            await ctx.send("**Modded Terraria Server Started**")

        elif arg1 == "":
            await ctx.send("Please specify which server to send the command!")

        else:  # arg1 != "Minecraft" or "Terraria" or "MTerraria":
            await ctx.send(f' Server not found!')
        print(f'{arg1}: "Start" Command Issued')

    @commands.command(name="stop", pass_context=True)
    @commands.has_permissions(administrator=True)
    async def stop(self, ctx, arg1):
        if arg1 == "Minecraft":
            subprocess.call('screen -S minecraft -p 0 -X stuff save-all^M', shell=True)
            time.sleep(3)
            subprocess.call('screen -S minecraft -p 0 -X stuff stop^M', shell=True)
            time.sleep(3)
            subprocess.call('screen -S minecraft -p 0 -X stuff exit^M', shell=True)
            await ctx.send("Minecraft Server has stopped")

        elif arg1 == "Terraria":
            subprocess.call('screen -S terraria -p 0 -X stuff save^M', shell=True)
            time.sleep(1)
            subprocess.call('screen -S terraria -p 0 -X stuff exit^M', shell=True)
            time.sleep(1)
            subprocess.call('screen -S terraria -p 0 -X stuff exit^M', shell=True)
            await ctx.send("Terraria Server has stopped")

        elif arg1 == "MTerraria":
            subprocess.call('screen -S moddedterraria -p 0 -X stuff save^M', shell=True)
            time.sleep(1)
            subprocess.call('screen -S moddedterraria -p 0 -X stuff exit^M', shell=True)
            time.sleep(1)
            subprocess.call('screen -S moddedterraria -p 0 -X stuff exit^M', shell=True)
            await ctx.send("Modded Terraria Server has stopped")

        elif arg1 == "":
            await ctx.send("Please specify which server to send the command!")

        else:  # arg1 != "Minecraft" or "Terraria" or "MTerraria":
            await ctx.send(f' Server not found!')
        print(f'{arg1}: "Stop" Command Issued')

    @commands.command(name="restart", pass_context=True)
    @commands.has_permissions(administrator=True)
    async def restart(self, ctx, arg1):
        if arg1 == "Minecraft":
            subprocess.call('screen -S minecraft -p 0 -X stuff save-all^M', shell=True)
            time.sleep(3)
            subprocess.call('screen -S minecraft -p 0 -X stuff stop^M', shell=True)
            time.sleep(3)
            subprocess.call('screen -S minecraft -p 0 -X stuff exit^M', shell=True)

            await ctx.send("Minecraft Server is restarting.....")

            subprocess.call('screen -dmS minecraft', shell=True)
            subprocess.call(f'screen -S minecraft -p 0 -X stuff "cd {minecraft}^M"', shell=True)
            time.sleep(0.5)
            subprocess.call(f'screen -S minecraft -p 0 -X stuff ' +
                            f'"java -Xms{os.getenv("MinecraftMin")} -Xmx{os.getenv("MinecraftMax")} ' +
                            f'-jar {os.getenv("ServerJarName")} nogui^M"', shell=True)
            time.sleep(8)
            subprocess.call('screen -S minecraft -p 0 -X stuff help^M',
                            shell=True)  # This is to fill the screen so that hardcopy works properly
            await ctx.send("**Minecraft Server Started!**")

        elif arg1 == "Terraria":
            subprocess.call('screen -S terraria -p 0 -X stuff save^M', shell=True)
            time.sleep(1)
            subprocess.call('screen -S terraria -p 0 -X stuff exit^M', shell=True)
            time.sleep(1)
            subprocess.call('screen -S terraria -p 0 -X stuff exit^M', shell=True)

            await ctx.send("Terraria Server is restarting.....")

            subprocess.call('screen -dmS terraria', shell=True)
            subprocess.call('screen -S terraria -p 0 -X stuff ' +
                            f'"TERM=xterm {terraria}/TerrariaServer.bin.x86_64 -config {terraria}/serverconfig.txt^M"',
                            shell=True)
            time.sleep(1)
            subprocess.call('screen -S terraria -p 0 -X stuff help^M', shell=True)

            await ctx.send("**Terraria Server Started!**")

        elif arg1 == "MTerraria":
            subprocess.call('screen -S moddedterraria -p 0 -X stuff save^M', shell=True)
            time.sleep(1)
            subprocess.call('screen -S moddedterraria -p 0 -X stuff exit^M', shell=True)
            time.sleep(1)
            subprocess.call('screen -S moddedterraria -p 0 -X stuff exit^M', shell=True)

            await ctx.send("Modded Terraria Server is restarting")

            subprocess.call('screen -dmS moddedterraria', shell=True)
            subprocess.call('screen -S moddedterraria -p 0 -X stuff ' +
                            f'"TERM=xterm {moddedterraria}/tModLoaderServer.bin.x86_64^M"', shell=True)
            time.sleep(10)
            subprocess.call('screen -S moddedterraria -p 0 -X stuff 1^M', shell=True)
            subprocess.call('screen -S moddedterraria -p 0 -X stuff 8^M', shell=True)
            subprocess.call('screen -S moddedterraria -p 0 -X stuff 7777^M', shell=True)
            subprocess.call('screen -S moddedterraria -p 0 -X stuff ^M', shell=True)
            time.sleep(10)
            subprocess.call('screen -S moddedterraria -p 0 -X stuff help^M', shell=True)
            await ctx.send("**Modded Terraria Server Started**")

        elif arg1 == "":
            await ctx.send("Please specify which server to send the command!")

        else:  # arg1 != "Minecraft" or "Terraria" or "MTerraria":
            await ctx.send(f' Server not found!')
        print(f'{arg1}: "Restart" Command Issued')


def setup(bot):
    bot.add_cog(ServerStarter(bot))
