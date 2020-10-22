import commands
import os
import discord
import sys
from discord.ext.commands import Bot
mb = Bot(command_prefix='!') # Creates the main bot object - asynchronous

scheduled = False

@mb.event
async def on_message(message):
    if(scheduled):
        return
    response_content = await commands.find(message.content.lower()[1:])
    if(response_content is not None):
        if(isinstance(response_content, discord.Embed)):
            await message.channel.send(embed=response_content)
        else:
            await message.channel.send(response_content)

@mb.event
async def on_ready():
    #if a CLI arg is passed, run that scheduled task and quit
    if(len(sys.argv) == 2 and sys.argv[1] in commands.scheduled):
        scheduled = True
        await getattr(commands, sys.argv[1])(mb)
        os._exit(0)

mb.run(open("TOKEN.txt", "r").readline())
