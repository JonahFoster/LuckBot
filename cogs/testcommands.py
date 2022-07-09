import discord
from discord.ext import commands
import random

class testCommands(commands.Cog): # Create the class for the cog

    def __init__(self, bot):
        self.bot = bot
    
    # Sample Text Command
    @discord.slash_command(name = "test", description = "A test command.")
    async def test(self, ctx):
        await ctx.respond("Test passed.")

    # Sample Random Choice Command
    @discord.slash_command(name = "testrandomchoices", description = "A test command.")
    async def testrandomchoices(self, ctx):
        await ctx.respond(random.choice(testing))

    # Sample Image Command
    @discord.slash_command(name = "testimage", description = "A test command.")
    async def testimage(self, ctx):
        await ctx.respond(file=discord.File('C:/Users/jonah/Desktop/LuckBot/photos/cryingmj.jpeg'))

def setup(bot):
    bot.add_cog(testCommands(bot)) # Add the cog to the bot










testing = ["Test1", "Test2", "Test3", "Test4"]