#masterspin
#11/23/2021
#valTeamComp

import discord
import os
import random

client = discord.Client()

@client.event
async def on_ready():
  print("Bot is ready!")
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('--unrated'):
    agents = ['Brimstone','Viper','Omen','Killjoy','Cypher','Sova','Sage','Phoenix','Jett','Reyna','Raze','Breach','Skye','Yoru','Astra','KAY/O','Chamber']
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

client.run(os.getenv('TOKEN'))
