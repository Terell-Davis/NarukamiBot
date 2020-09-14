from discord.ext import commands


class Template(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener() # Anytime you want an event in a cog need this line
    async def on_ready(self):
        print('')

    @commands.command() # For any commands
    async def ping(self, ctx):
        await ctx.send('Pong!')


def setup(bot):
    bot.add_cog(Template(bot))
