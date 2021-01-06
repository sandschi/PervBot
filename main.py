import discord
import os 
from keep_alive import keep_alive 

import requests 
client = discord.Client()



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name='with himself'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "ß" in message.content:
        await message.channel.send('Das fälschung Niederlander geht: ßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßß')

#@client.event
#async def on_message(message):
#   if message.author == client.user:
#       return
#
#    if "dad" in message.content:
#     dadjoke = request.get('')
#     await message.channel.send(dadjoke)

@client.event
async def on_message_delete(message):    
   await message.channel.send('I saw that! :eyes:')   

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "insult me" in message.content:
      insult = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=text')
      await message.channel.send(insult.text)


keep_alive()
client.run(os.getenv('TOKEN'))