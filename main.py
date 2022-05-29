import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

description = '''The Jonah Foster Test Bot'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='.', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as LuckBot')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

client.run(os.getenv("DISCORD_TOKEN"))