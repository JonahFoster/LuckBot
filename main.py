import discord
import os
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

@client.event 
async def on_ready():
    print('We have logged in as Luckbot'.format(client))

client.run(os.getenv("DISCORD_TOKEN"))