import discord
import os
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot(debug_guilds=[933551727557373993])

description = '''The Jonah Foster Test Bot'''

intents = discord.Intents.default()
intents.members = True

@bot.event
async def on_ready():
    print('Luckbot is online')

bot.load_extension('cogs.testcommands')
bot.load_extension('cogs.twitter')

bot.run(os.getenv("DISCORD_TOKEN"))