import discord
from discord.ext import commands

class testCommands(commands.Cog): # Create the class for the cog

    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(name = "test", description = "A test command.")
    async def test(ctx):
        await ctx.respond("Test passed.")

def setup(bot):
    bot.add_cog(testCommands(bot)) # Add the cog to the bot