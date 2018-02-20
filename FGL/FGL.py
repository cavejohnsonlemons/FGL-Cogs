# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands
from cogs.utils import checks
from random import randint
from random import choice

__author__ = "kirdneh"


class FGL:
    """Commands developed by the Future Gadget Laboratory"""

    def __init__(self, bot):
        self.bot = bot
        

    @commands.command()
    async def catchphrase(self):
        """I say my catchphrase!"""
        await self.bot.say("Tuturu~ ♫")

def setup(bot):
    n = FGL(bot)
    bot.add_cog(n)
