import discord
import os 
from keep_alive import keep_alive 
#import logging 
import requests 
client = discord.Client()
import time

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
    #for emoji in client.emojis:
        #print("Name:", emoji.name + ",", "ID:", emoji.id)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.author.id == 664508672713424926:
        print('Ignored Pokemeow')
        return 
    elif message.author.id == 490707751832649738:
        print('Ignored Taco')
        return 
    if message.channel.id == 831789312378667028:
        print('Ignored Tacochannel')
        return
    if message.channel.id == 832178751709118524:
      print('Ignored Customerchannel')
      return
    if message.channel.id == 832220565414477884:
      print('Ignored Franchisechannel')
      return    
    if "ß" in message.content:
        await message.channel.send('Das fälschung Niederlander geht: ßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßß')
    
    elif "!buy" in message.content.lower():
      return

    if "!lisa" in message.content:
      async with message.channel.typing():
        await message.channel.send('Lisa goes: ßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßß')

    if "insult me" in message.content.lower():
       async with message.channel.typing():
        insult = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=text')
        await message.channel.send(insult.text)

    if "die" in message.content.lower():
      async with message.channel.typing():
       await message.channel.send(file=discord.File('passaway.gif'))
    
    if "i hate you" in message.content.lower():
      async with message.channel.typing():
       await message.channel.send(file=discord.File('ihateyou.gif'))

    if "poop" in message.content.lower():
        await message.add_reaction('💩')
      
    if "hot" in message.content.lower():
        await message.add_reaction('🔥')
        await message.add_reaction('🚒')
        await message.add_reaction('🇭')
        await message.add_reaction('🇴')
        await message.add_reaction('🇹')
        
    if "tomika" in message.content.lower():
        await message.add_reaction('🤮')
        await message.add_reaction('🤢')

    if "snow" in message.content.lower():
            await message.add_reaction('❄️')

    if "glasses" in message.content.lower():
            await message.add_reaction('👓')        
            await message.add_reaction('🕶️')  
            await message.add_reaction('🥽')  
    
    if "mask" in message.content.lower():
            await message.add_reaction('😷')
        
    if "potentie" in message.content.lower():
      await message.channel.send(file=discord.File('potentie.gif'))

   # if "@" in message.content:
   #   await message.channel.send(file=discord.File('ping.gif'))  

    if "please wait" in message.content.lower():
      await message.channel.send(file=discord.File('wait.gif'))  
    
    if "!help" in message.content.lower(): 
       embed=discord.Embed(title="made by sandschi", url="https://twitch.tv/sandschi", description="Bot Features", color=0x0fe628)
       embed.set_author(name="Bot Help")
       embed.add_field(name="!help", value="brings up help file", inline=True)
       embed.add_field(name="!b ", value="Lisa goes: ßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßß", inline=True)
       embed.add_field(name="insult me ", value="you will be insulted", inline=True)
       embed.add_field(name=" die", value="posts a gif ", inline=True)
       embed.add_field(name=" i hate you ", value="posts another gif", inline=True)
       embed.add_field(name="poop", value="💩", inline=True)
       embed.add_field(name=" ß", value="blame yowey for that one, try  and find out ", inline=True)
       embed.add_field(name="potentie ", value="¯\_༼ ಥ ‿ ಥ ༽_/¯", inline=True)
       embed.add_field(name="hot", value="🔥🚒 🇭 🇴  🇹", inline=True)
       embed.add_field(name="snow", value="❄️", inline=True)
       embed.add_field(name="glasses ", value="get glasses", inline=True)
       embed.add_field(name="mask", value="😷", inline=True)
       embed.set_footer(text="BOT VER 0.0.06 Absolutely not Beta ")
       await message.channel.send(embed=embed)


#dadjoke
#    if "dad" in message.content:
#     dadjoke = request.get('https://icanhazdadjoke.com/')
#     await message.channel.send(dadjoke.text)

@client.event
async def on_message_delete(message):    
   await message.channel.send('I saw that! :eyes:')   


keep_alive()
client.run(os.getenv('TOKEN'))