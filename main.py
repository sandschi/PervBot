import discord
import os 
from keep_alive import keep_alive 
#import logging 
import requests 
client = discord.Client()

#logging
#logger = logging.getLogger('discord')
#logger.setLevel(logging.DEBUG)
#handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
#handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
#logger.addHandler(handler)


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

    if "!b" in message.content:
        await message.channel.send('Lisa goes: ßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßß')

    if "insult me" in message.content:
      insult = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=text')
      await message.channel.send(insult.text)

    if "die" in message.content:
      await message.channel.send(file=discord.File('passaway.gif'))
    
    if "i hate you" in message.content:
      await message.channel.send(file=discord.File('ihateyou.gif'))
 
#dadjoke
#    if "dad" in message.content:
#     dadjoke = request.get('https://icanhazdadjoke.com/')
#     await message.channel.send(dadjoke.text)

@client.event
async def on_message_delete(message):    
   await message.channel.send('I saw that! :eyes:')   


keep_alive()
client.run(os.getenv('TOKEN'))