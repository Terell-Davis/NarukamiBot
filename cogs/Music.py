from discord import utils
from discord import embeds
from discord.ext import commands


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Music(bot))
