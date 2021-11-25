import os
import io
import aiohttp
import discord

client = discord.Client(activity=discord.Game(name="with your mom's tiddies"))

@client.event 
async def on_ready():
  print('yooo, im {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('#hey'):
    await message.channel.send('sup')
    await message.author.send('👀')
  if message.content.startswith('#bye') :
    await message.add_reaction('\U0001f44d')
  
  
client.run(os.getenv('token'))