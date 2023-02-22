import discord
from discord.ext import commands
import responses


config = responses.get_config()

isPrivate = False

class openaicog(commands.Cog): # Create the class for the cog

    def __init__(self, bot):
        self.bot = bot

    async def send_message(message, user_message):
        await message.response.defer(ephemeral=isPrivate)
        try:
            response = '> **' + user_message + '** - <@' + \
                str(message.user.id) + '>\n\n'
            response = f"{response}{user_message}{await responses.handle_response(user_message)}"
            if len(response) > 1900:
                # Split the response into smaller chunks of no more than 1900 characters each(Discord limit is 2000 per chunk)
                if "```" in response:
                    # Split the response if the code block exists
                    parts = response.split("```")
                    # Send the first message
                    await message.followup.send(parts[0])
                    # Send the code block in a seperate message
                    code_block = parts[1].split("\n")
                    formatted_code_block = ""
                    for line in code_block:
                        while len(line) > 1900:
                            # Split the line at the 50th character
                            formatted_code_block += line[:1900] + "\n"
                            line = line[1900:]
                        formatted_code_block += line + "\n"  # Add the line and seperate with new line

                    # Send the code block in a separate message
                    if (len(formatted_code_block) > 2000):
                        code_block_chunks = [formatted_code_block[i:i+1900]
                                            for i in range(0, len(formatted_code_block), 1900)]
                        for chunk in code_block_chunks:
                            await message.followup.send("```" + chunk + "```")
                    else:
                        await message.followup.send("```" + formatted_code_block + "```")

                    # Send the remaining of the response in another message

                    if len(parts) >= 3:
                        await message.followup.send(parts[2])
                else:
                    response_chunks = [response[i:i+1900]
                                    for i in range(0, len(response), 1900)]
                    for chunk in response_chunks:
                        await message.followup.send(chunk)
            else:
                await message.followup.send(response)
        except Exception as e:
            await message.followup.send("> **Error: Something went wrong, please try again later!**")

    @discord.slash_command(name="chat", description="Have a chat with ChatGPT")
    async def chat(ctx, *, message: str):
        if ctx.user == discord.user:
            return
        username = str(ctx.user)
        user_message = message
        channel = str(ctx.channel)
        await ctx.respond(ctx, user_message)

   # @discord.slash_command(name="private", description="Toggle private access")
   # async def private(self, ctx):
        #global isPrivate
        #await ctx.response.defer(ephemeral=False)
        #if not isPrivate:
          #  isPrivate = not isPrivate
         #   await ctx.followup.send("> **Info: Next, the response will be sent via private message. If you want to switch back to public mode, use `/public`**")
        #else:
       #     await ctx.followup.send("> **Warn: You already on private mode. If you want to switch to public mode, use `/public`**")

#    @discord.slash_command(name="public", description="Toggle public access")
#    async def public(self, ctx):
 #       global isPrivate
  #      await ctx.response.defer(ephemeral=False)
   #     if isPrivate:
    #        isPrivate = not isPrivate
     #       await ctx.followup.send("> **Info: Next, the response will be sent to the channel directly. If you want to switch back to private mode, use `/private`**")
      #  else:
       #     await ctx.followup.send("> **Warn: You already on public mode. If you want to switch to private mode, use `/private`**")

def setup(bot):
    bot.add_cog(openaicog(bot)) # Add the cog to the bot