import discord 
from discord.ext import commands, tasks
from pictures import images
from random import randint
prefix = '$'
client = commands.Bot(command_prefix=prefix, help_command=None)
channel = 'The channel ID of the channel you want the bot to send the pictures to here'
token = 'bot token here'


@client.event
async def on_ready():
    print('bot is ready.')
    send_pictures.start()


@tasks.loop(hours=24)
async def send_pictures():
    channel = await client.fetch_channel(int(channel))
    num = randint(0, len(images)) - 1
    await channel.send(images[num])
    
    
client.run(token)
