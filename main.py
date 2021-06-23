import discord 
from discord.ext import commands, tasks
from pictures import images
from random import randint
from time import sleep
from secrets import token
prefix = '$'
client = commands.Bot(command_prefix=prefix, help_command=None)


@client.event
async def on_ready():
    print('bot is ready.')
    send_pictures.start()


@tasks.loop(hours=24)
async def send_pictures():
    channel = await client.fetch_channel(834843660214468669)
    num = randint(0, len(images)) - 1
    await channel.send(images[num])
    
    
client.run(token)
