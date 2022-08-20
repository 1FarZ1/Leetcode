import random

import discord
from discord.ext import commands

def QuizzBrain(diffuculty):
    pass
# bot = commands.Bot(command_prefix='!')
intents=discord.Intents.default()
intents.message_content=True
client=discord.Client(intents=intents)
TOKEN = 'MTAxMDYwMjY3MzMyMzYzODg0NA.Go6l2f.W8f2QdTVR_vC1LoDl74nW2VWKIYQqtl_D2f_iM'
messages=[
  "faregamer"
  "bimber",
  "mdolna jokes",
  "zedx yjwz bem",
  "zaki mywj3ouch raso",
]
hikm=[
  "khtik mn lig",
  "roh llgym",
  "zaki hyati rust",
  "zedx yjwz bem",
  "FaresYotuber",
]
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):   
    
    if message.author ==client.user:
      print("here")
      return
    elif "1" or "2" or "3" in message.content:
        if message.author==Targeted_user:
            QuizzBrain(message.content)
    elif "!joke" in message.content:
      random_int=random.randint(0,2)
      await message.channel.send(messages[random_int])
    elif "!hikma" in message.content:
      random_int=random.randint(0,3)
      await message.channel.send(hikm[random_int])
    elif "!addJoke" in message.content:
        print("here")
        message_to_add=message.content.replace("!addJoke","").strip(" ")
        await message.channel.send(f'message added successfully ')
        messages.append(message_to_add)
    elif message.content =="agree":
        await message.add_reaction("\U0001F60E")
    elif "!Quizz" in message.content:
           Targeted_user=message.author
           await message.channel.send("Choose your diffuculty \n 1.easy \n2.medium \n3.hard")
    else:
        za3im=str(message.author).split("#")[0]
        # await message.channel.send(f"  {za3im} said : {message.content}")
        await message.channel.send("slm")
      
client.run(TOKEN)

    