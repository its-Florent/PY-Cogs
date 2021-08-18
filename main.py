import discord
from discord.ext \
    import commands
import asyncio
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='.') #intents=discord.Intents.all()) # Optional due to the Discord intents 


extensions = ['test']# Your extensions (Path + filename!)


if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)# Load all extensions from the list.
        except Exception as error:
            print('{} could not be loaded. [{}]'.format(extension, error))


@bot.event
async def on_ready():
    print("Bot online with:")
    print("Username: ", bot.user.name)
    print("User ID: ", bot.user.id)


bot.run("TOKEN") # Your Token from discord.com/developers
