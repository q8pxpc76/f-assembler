import os
import random
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
    rnd = random.randint(0, 1)
    if rnd == 0:
        output = "<a:spit:856805542647431179>"
    else:
        output = "<a:kidSpit:856821253389942785>"

    if message.author == client.user:
        return

    if 'assembl' in message.content.lower():
        await message.channel.send(output)

client.run(TOKEN)
