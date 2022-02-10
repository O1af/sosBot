import discord
import os
import random
from discord.utils import get
from keep_alive import keep_alive


client = discord.Client()

@client.event
async def on_ready():
  print("Bot is ready!")
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  

  #lightmode
  if '⬜' in message.content:
    await message.reply("Light mode, doesn't count")
    await message.add_reaction('<:upvote:844410038256795678>')
  
  if '👩🏻‍🦳' in message.content:
    await message.reply("Light mode, doesn't count")
  
  if '👨🏻‍🦳' in message.content:
    await message.reply("Light mode, doesn't count")
  
  if '◽' in message.content:
    await message.reply("Light mode, doesn't count")
  
  if '❔' in message.content:
    await message.reply("Light mode, doesn't count")
  
  if '👩‍🦳' in message.content:
    await message.reply("Light mode, doesn't count")
  
  if '👨‍🦳' in message.content:
    await message.reply("Light mode, doesn't count")
  
  if '🏳️' in message.content:
    await message.reply("Light mode, doesn't count")
    await message.add_reaction('<:upvote:844410038256795678>')
  
  if '🔳' in message.content:
    await message.reply("Light mode, doesn't count")
    await message.add_reaction('<:upvote:844410038256795678>')
  
  if '◻️' in message.content:
    await message.reply("Light mode, doesn't count")
    await message.add_reaction('<:upvote:844410038256795678>')
  
  if '🤍' in message.content:
    await message.reply("Light mode, doesn't count")
    await message.add_reaction('<:upvote:844410038256795678>')

  if '▫️' in message.content:
    await message.reply("Light mode, doesn't count")
    await message.add_reaction('<:upvote:844410038256795678>')

  if '⚪' in message.content:
    await message.reply("Light mode, doesn't count")
    await message.add_reaction('<:upvote:844410038256795678>')
  
  if 'Light mode, doesn\'t count' in message.content:
    await message.add_reaction('<:upvote:844410038256795678>') 
  
  #commands
  if(message.content.startswith('--commands')):
    await message.channel.send('--unrated\n--repeat\n--uno\n--pfp\n--deepthroat\n--wtfolaf\n--epicrs\n--anishteddy\n--soochit\n--sochit\n--babyshek\n--sadnabi\n--gigashreyas\n--wtfshreyas\n--suchitbruh\n--venkydasimp\n--shreyascolor\n--shreyasmugshot\n--blackshreyas\n--sos\n--gigashreyascard\n--anishdoctor\n--wtfboots\n--prof(firstname)\nlovelyolaf')


  #repeat bot
  if message.content.startswith('--repeat'):
    m = message.content.split(" ", 1)
    newMessage = m[1]
    m = newMessage.split(" ",1)
    for i in range(int(m[0])):
      await message.channel.send(m[1])

  #soscommands
  if(message.content.startswith('--uno')):
    await message.channel.send('https://cdn.discordapp.com/attachments/817432681633153029/911777019321262080/no_u.png')
  if(message.content.startswith('--pfp')):
    await message.channel.send('https://cdn.discordapp.com/attachments/689191193267273838/924504774211162152/1640489479600.png')
  if(message.content.startswith('--deepthroat')):
    await message.channel.send('https://cdn.discordapp.com/attachments/689191193267273838/899480766239604836/unknown.png')
  if(message.content.startswith('--wtfolaf')):
    await message.channel.send('https://cdn.discordapp.com/attachments/843919055860924492/844405997338624010/wtf_olaf.png')
  if(message.content.startswith('--epicrs')):
    await message.channel.send('https://media.discordapp.net/attachments/925170620931661844/926539429491933184/rishith_epic.png')
  if(message.content.startswith('--anishteddy')):
    await message.channel.send('https://media.discordapp.net/attachments/925170620931661844/926539670043639938/AnishTeddy.png')
  if(message.content.startswith('--soochit')):
    await message.channel.send('https://media.discordapp.net/attachments/925170620931661844/926539759331975218/abhishek_feeds_suchit_too_much.png')
  if(message.content.startswith('--sochit')):
    await message.channel.send('https://media.discordapp.net/attachments/925170620931661844/926678525275168848/Sochit.jpg')
  if(message.content.startswith('--babyshek')):
    await message.channel.send('https://media.discordapp.net/attachments/925170620931661844/926678549824417852/abhishek.png')
  if(message.content.startswith('--sadnabi')):
    await message.channel.send('https://media.discordapp.net/attachments/925170620931661844/926678595080949760/IMG_4614.png')
  if(message.content.startswith('--gigashreyas')):
    await message.channel.send('https://media.discordapp.net/attachments/925170620931661844/926679175723614248/gigashreyas.png')
  if(message.content.startswith('--wtfshreyas')):
    await message.channel.send('https://media.discordapp.net/attachments/925170620931661844/926682368000012348/wtfshreyasresized.jpg')
  #if(message.content.startswith('--homecoming')):
   # await message.channel.send('https://media.discordapp.net/attachments/925170620931661844/926682001250062357/homecoming.jpg')
  if(message.content.startswith('--suchitbruh')):
    await message.channel.send('https://media.discordapp.net/attachments/925170620931661844/926682751753662534/812370477666009129.png')
  if(message.content.startswith('--venkydasimp')):
    await message.channel.send('https://media.discordapp.net/attachments/925170620931661844/930289251415916624/venkysimpcardv3.png?width=1089&height=701')
  if(message.content.startswith('--anishdoctor')):
    await message.channel.send('https://media.discordapp.net/attachments/925170620931661844/930291418281443338/wtf_anish.png?width=395&height=702')
  if(message.content.startswith('--gigashreyascard')):
    await message.channel.send('https://media.discordapp.net/attachments/925170620931661844/930289704199421952/gigashreyascard.jpg')
  if(message.content.startswith('--anishteddy')):
    await message.channel.send('https://media.discordapp.net/attachments/925170620931661844/930289885095526451/AnishTeddy.png')
  if(message.content.startswith('--blackshreyas')):
    await message.channel.send('https://media.discordapp.net/attachments/925170620931661844/930289985087750234/Shreyas_black_and_white.jpg?width=726&height=701')
  if(message.content.startswith('--sos')):
    await message.channel.send('https://cdn.discordapp.com/attachments/925170620931661844/930289984727048242/sosBot.png')
  if(message.content.startswith('--shreyascolor')):
    await message.channel.send('https://cdn.discordapp.com/attachments/925170620931661844/930290152813760572/Shreyas_color.png')
  if(message.content.startswith('--shreyasmugshot')):
    await message.channel.send('https://cdn.discordapp.com/attachments/925170620931661844/930290320292331640/IMG_3863.jpg')
  if(message.content.startswith('--wtfboots')):
    await message.channel.send('https://media.discordapp.net/attachments/817432681633153029/940310946453270568/unknown.png')
  if(message.content.startswith('--profolaf')):
    await message.channel.send('https://media.discordapp.net/attachments/817432681633153029/940307922624348200/Screenshot_20220207-130745_Adobe_Acrobat.jpg?width=321&height=431')
  if(message.content.startswith('--profanish')):
    await message.channel.send('https://media.discordapp.net/attachments/817432681633153029/940304338226663445/Screenshot_20220126-124836_Adobe_Acrobat.jpg?width=315&height=431')
  if(message.content.startswith('--profaneesh')):
    await message.channel.send('https://media.discordapp.net/attachments/817432681633153029/940308494312153108/Screenshot_20220207-131008_Adobe_Acrobat.jpg?width=251&height=432')
  if(message.content.startswith('--profvenkatesh')):
    await message.channel.send('https://media.discordapp.net/attachments/817432681633153029/940304336968376462/Screenshot_20220126-130232_Adobe_Acrobat.jpg?width=316&height=432')
  if(message.content.startswith('--profwilliam')):
    await message.channel.send('https://media.discordapp.net/attachments/817432681633153029/940307922884382720/Screenshot_20220207-130710_Adobe_Acrobat.jpg?width=325&height=432')
  if(message.content.startswith('--profabhishek')):
    await message.channel.send('https://media.discordapp.net/attachments/817432681633153029/940304338012733440/Screenshot_20220126-125304_Adobe_Acrobat.jpg?width=314&height=432')
  if(message.content.startswith('--profrishith')):
    await message.channel.send('https://media.discordapp.net/attachments/817432681633153029/940304337719156766/Screenshot_20220126-125347_Adobe_Acrobat.jpg?width=316&height=432')
  if(message.content.startswith('--profsuchit')):
    await message.channel.send('https://media.discordapp.net/attachments/817432681633153029/940304337467506688/Screenshot_20220126-125507_Adobe_Acrobat.jpg?width=315&height=432')
  if(message.content.startswith('--profnarayana')):
    await message.channel.send('https://media.discordapp.net/attachments/817432681633153029/940304337215823992/Screenshot_20220126-125527_Adobe_Acrobat.jpg?width=403&height=432')

  if(message.content.startswith('--lovelyolaf')):
    await message.channel.send(' https://media.discordapp.net/attachments/817432681633153029/940808945906364456/Snapchat-1781669876.png?width=364&height=700')
    
  #ratio time
  if 'ratio' in message.content:
    await message.add_reaction('<:upvote:844410038256795678>')
  if message.content.startswith('--unrated'):
    agents = ['Brimstone','Viper','Omen','Killjoy','Cypher','Sova','Sage','Phoenix','Jett','Reyna','Raze','Breach','Skye','Astra','KAY/O','Chamber']
    m = message.content.split()
    m.remove('--unrated')
    chosen = []
    i = 0
    while i < 5:
      randint = random.randint(0, len(agents)-1)
      if agents[randint] not in chosen:
        chosen.append(agents[randint])
        i+=1
    output = ''
    n = 5
    if len(m)<5:
      n = len(m)
    for i in range(n):
      output += m[i] + ': ' + chosen[i] + '\n'
    await message.channel.send(output)

    # m = newMessage.split()
    # for i in range(int(m[0])):
    #   await message.channel.send(m[1])

keep_alive()
client.run(os.getenv('TOKEN'))
