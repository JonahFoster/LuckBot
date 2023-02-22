import discord
import os
from dotenv import load_dotenv
import sys



load_dotenv()
bot = discord.Bot(debug_guilds=[933551727557373993])

description = '''The Jonah Foster Test Bot'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

def check_version() -> None:
    import pkg_resources


    # Read the requirements.txt file and add each line to a list
    with open('requirements.txt') as f:
        required = f.read().splitlines()

    # For each library listed in requirements.txt, check if the corresponding version is installed
    for package in required:
        # Use the pkg_resources library to get information about the installed version of the library
        package_name, package_verion = package.split('==')
        installed = pkg_resources.get_distribution(package_name)
        # Extract the library name and version number
        name, version = installed.project_name, installed.version
        # Compare the version number to see if it matches the one in requirements.txt
        if package != f'{name}=={version}':
            print(f'{name} version {version} is installed but does not match the requirements')
            sys.exit();

if __name__ == '__main__': 
    check_version()

@bot.event
async def on_ready():
    print('Luckbot is online')

bot.load_extension('cogs.testcommands')
bot.load_extension('cogs.openaicog')

bot.run(os.getenv("DISCORD_TOKEN"))