# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

#@client.event
#async def on_ready():
#    print(f'{client.user} has connected to Discord!')
#
#client.run(TOKEN)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'assembler' in message.content.lower() or 'assembly' in message.content.lower():
        await message.channel.send("<a:spit:856805542647431179>")
        #await message.channel.send("🖕 assembler")

client.run(TOKEN)
