import discord
import os
import random
from discord.utils import get
from keep_alive import keep_alive
from discord.ext import commands


client = discord.Client()
bot = commands.Bot(command_prefix="")

@client.event
async def on_ready():
  print("Bot is ready!")


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  whitestoconvert = ['🤍', '⬜', '🔲', '⚪']
  convertedtoblacks = ['🖤', '⬛', '🔳', '⚫']

  #replacing darkmode
  newString = ""
  isLight = False
  for i in range(len(message.content)):
    print(message.content[i])
    if message.content[i] in whitestoconvert:
      isLight = True
  
  print(isLight)
  
  if isLight:
    for i in range(len(message.content)):
      if message.content[i] in whitestoconvert:
        index = whitestoconvert.index(message.content[i])
        newString += convertedtoblacks[index]
      else:
        newString += message.content[i]
    print(newString)
    webhook = await message.channel.create_webhook(name=message.author.name)
    await webhook.send(content=newString, avatar_url = message.author.avatar_url)
    await webhook.delete()
    await message.delete()


  #lightmode
  lightmode_emotes = ['👩🏻‍🦳','👨🏻‍🦳','❔','👩‍🦳','👨‍🦳','✅','❕','💮','☁️','⛅','🌨️','🌩️','⛈️','🌤️','🌥️','🌦️', '▫️', '◻️', '🏳️', '◽']

  for i in lightmode_emotes:
    if i in message.content:
      ctx =  await message.reply("Light mode, doesn't count")
      await ctx.add_reaction('<:upvote:844410038256795678>')
      break
     

  #repeat bot
  if message.content.startswith('++repeat'):
    m = message.content.split(" ", 1)
    newMessage = m[1]
    m = newMessage.split(" ",1)
    for i in range(int(m[0])):
      await message.channel.send(m[1])

  #pfp bot
  if message.content.startswith('++profile'):
    m = message.content.split(" ", 1)
    mention = m[1]
    mention = mention.replace('<','')
    mention = mention.replace('!','')
    mention = mention.replace('@','')
    mention = mention.replace('>','')
    user = await client.fetch_user(int(mention))
    pfp = user.avatar_url
    await message.channel.send(pfp)

  #soscommands

  commands = [
  '++uno',
  '++pfp',
  '++deepthroat',
  '++wtfolaf',
  '++epicrs',
  '++anishteddy',
  '++soochit',
  '++sochit', 
  '++babyshek', 
  '++sadnabi',
  '++gigashreyas',
  '++wtfshreyas',
  '++homecoming',
  '++suchitbruh',
  '++venkydasimp',
  '++anishdoctor',
  '++gigashreyascard',
  '++blackshreyas',
  '++sos',
  '++shreyascolor',
  '++shreyasmugshot',
  '++wtfboots',
  '++profolaf',
  '++profanish',
  '++profaneesh',
  '++profvenkatesh',
  '++profwilliam',
  '++profabhishek',
  '++profrishith',
  '++profsuchit',
  '++profnarayana',
  '++lovelyolaf',
  '++santanish',
  '++satanish',
  '++sahijwish',
  '++joshi',
  ]


  images = [
    'https://cdn.discordapp.com/attachments/817432681633153029/911777019321262080/no_u.png',
    'https://cdn.discordapp.com/attachments/689191193267273838/924504774211162152/1640489479600.png',
    'https://cdn.discordapp.com/attachments/689191193267273838/899480766239604836/unknown.png',
    'https://cdn.discordapp.com/attachments/843919055860924492/844405997338624010/wtf_olaf.png',
    'https://media.discordapp.net/attachments/925170620931661844/926539429491933184/rishith_epic.png',
    'https://media.discordapp.net/attachments/925170620931661844/926539670043639938/AnishTeddy.png',
    'https://media.discordapp.net/attachments/925170620931661844/926539759331975218/abhishek_feeds_suchit_too_much.png',
    'https://media.discordapp.net/attachments/925170620931661844/926678525275168848/Sochit.jpg',
    'https://media.discordapp.net/attachments/925170620931661844/926678549824417852/abhishek.png',
    'https://media.discordapp.net/attachments/925170620931661844/926678595080949760/IMG_4614.png',
    'https://media.discordapp.net/attachments/925170620931661844/926679175723614248/gigashreyas.png',
    'https://media.discordapp.net/attachments/925170620931661844/926682368000012348/wtfshreyasresized.jpg',
    'https://media.discordapp.net/attachments/925170620931661844/926682001250062357/homecoming.jpg',
    'https://media.discordapp.net/attachments/925170620931661844/926682751753662534/812370477666009129.png',
    'https://media.discordapp.net/attachments/925170620931661844/930289251415916624/venkysimpcardv3.png?width=1089&height=701',
    'https://media.discordapp.net/attachments/925170620931661844/930291418281443338/wtf_anish.png?width=395&height=702',
    'https://media.discordapp.net/attachments/925170620931661844/930289704199421952/gigashreyascard.jpg',
    'https://media.discordapp.net/attachments/925170620931661844/930289985087750234/Shreyas_black_and_white.jpg?width=726&height=701',
    'https://cdn.discordapp.com/attachments/925170620931661844/930289984727048242/sosBot.png',
    'https://cdn.discordapp.com/attachments/925170620931661844/930290152813760572/Shreyas_color.png',
    'https://cdn.discordapp.com/attachments/925170620931661844/930290320292331640/IMG_3863.jpg',
    'https://media.discordapp.net/attachments/817432681633153029/940310946453270568/unknown.png',
    'https://media.discordapp.net/attachments/817432681633153029/940307922624348200/Screenshot_20220207-130745_Adobe_Acrobat.jpg?width=321&height=431',
    'https://media.discordapp.net/attachments/817432681633153029/940304338226663445/Screenshot_20220126-124836_Adobe_Acrobat.jpg?width=315&height=431',
    'https://media.discordapp.net/attachments/817432681633153029/940308494312153108/Screenshot_20220207-131008_Adobe_Acrobat.jpg?width=251&height=432',
    'https://media.discordapp.net/attachments/817432681633153029/940304336968376462/Screenshot_20220126-130232_Adobe_Acrobat.jpg?width=316&height=432',
    'https://media.discordapp.net/attachments/817432681633153029/940307922884382720/Screenshot_20220207-130710_Adobe_Acrobat.jpg?width=325&height=432',
    'https://media.discordapp.net/attachments/817432681633153029/940304338012733440/Screenshot_20220126-125304_Adobe_Acrobat.jpg?width=314&height=432',
    'https://media.discordapp.net/attachments/817432681633153029/940304337719156766/Screenshot_20220126-125347_Adobe_Acrobat.jpg?width=316&height=432',
    'https://media.discordapp.net/attachments/817432681633153029/940304337467506688/Screenshot_20220126-125507_Adobe_Acrobat.jpg?width=315&height=432',
    'https://media.discordapp.net/attachments/817432681633153029/940304337215823992/Screenshot_20220126-125527_Adobe_Acrobat.jpg?width=403&height=432',
    'https://media.discordapp.net/attachments/817432681633153029/940808945906364456/Snapchat-1781669876.png?width=364&height=700',
    'https://images-ext-1.discordapp.net/external/_AhFATDwaRcscTwSgegkhNlPLtecBZTN6kNqQjhys6U/%3Fwidth%3D527%26height%3D701/https/media.discordapp.net/attachments/927053607700930580/935246245725896724/AA366A0C-80ED-4FAD-93A6-5577B98A3210.jpg',
    'https://media.discordapp.net/attachments/817432681633153029/941152742553043004/satanish.png?width=517&height=701',
    'https://media.discordapp.net/attachments/817432681633153029/941154680841576528/IMG_20220209_122937.png?width=526&height=701',
    'https://media.discordapp.net/attachments/817432681633153029/942509489721081896/image0.png?width=359&height=701',
  ]


  #say commands
  if message.content.startswith('++say'):
    if message.author.id == 635987876147888140 or 233753795220209665:
      await message.channel.send(message.content[6:])
      await message.delete()

  #commands
  if(message.content.startswith('++commands')):
    commandlist = "++unrated\n++repeat\n++profile\n"
    for i in commands:
      commandlist += i + "\n"
    await message.channel.send(commandlist)

  for i in range(0, len(commands)):
    if message.content.startswith(commands[i]):
      webhook = await message.channel.create_webhook(name=message.author.name)
      await webhook.send(content=images[i], avatar_url = message.author.avatar_url)
      await webhook.delete()
      await message.delete()
  
  #ratio time
  #message.author.id
  if 'ratio' in message.content.split():
    await message.add_reaction('<:upvote:844410038256795678>')

  #valorant unrated composition maker
  if message.content.startswith('++unrated'):
    agents = ['Brimstone','Viper','Omen','Killjoy','Cypher','Sova','Sage','Phoenix','Jett','Reyna','Raze','Breach','Skye','Astra','KAY/O','Chamber']
    m = message.content.split()
    m.remove('++unrated')
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
    output.replace('▫️','⬜')
    output.replace('◽','⬜')
    output.replace('◻️','⬜')
    output.replace('⬜','⬛')
    await message.channel.send(output)

    # m = newMessage.split()
    # for i in range(int(m[0])):
    #   await message.channel.send(m[1])

keep_alive()
client.run(os.getenv('TOKEN'))
