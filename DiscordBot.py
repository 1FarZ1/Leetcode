import discord
from discord.ext import commands
import random
import asyncio

# bot = commands.Bot(command_prefix='!')
intents=discord.Intents.default()
intents.message_content=True
bot=commands.Bot(command_prefix ="-",intents=intents)
TOKEN = 'Your Token'
## will change this to  local database sqllflite  later on 
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
levels={
  "1":"Easy",
  "2":"Medium",
  "3":"Hard"
}
Targeted_user=" "
@bot.event
async def on_ready():
   
    print('Logged in as {0.user}'.format(bot))
    
@bot.event
async def on_message(message):
    if message.author ==bot.user:
      return
    # elif "1" in message.content or "2" in message.content or "3" in message.content:
    #     if message.author==Targeted_user:
    #         try :
    #           diff=levels[message.content]
    #           await message.channel.send(f"The {diff} Quizz Begin ")
    #         except:
    #            await message.channel.send(f"Enter only numbers pls ")  
        
    elif message.content == "agree":
        await message.add_reaction("\U0001F60E")
        
        
    elif message.content == '-Guess':
      
            
            await message.channel.send('Guess a number between 1 and 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)
            try:
                guess = await bot.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Sorry, you took too long it was {answer}.')

            if int(guess.content) == answer:
                await message.reply('You are right!',mention_author=True)
            else:
                await message.reply(f'Oops. It is actually {answer}.',mention_author=True)
    elif "judenMorden" == message.content:
          await message.channel.send("Yes")
          if "do" in message.content:
            await message.channel.send(" i should kill juden")    
    
    
        
    ## THIS CODE  is commented  to not annoy anyone
    # za3im=str(message.author).split("#")[0]
    # await message.channel.send(f"  {za3im} said : {message.content}")
    # await message.channel.send("slm")
    await bot.process_commands(message)
    
    
@bot.command()
async def Joke(ctx):
      print("here1")
      random_int=random.randint(0,len(messages)-1)
      await ctx.send(messages[random_int])
      
@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))
@bot.command()
async def Hikma(ctx):
     random_int=random.randint(0,len(hikm)-1)
     await ctx.send(hikm[random_int])
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
@bot.command()
async def AddJoke(ctx):
      message_to_add=ctx
      print(message_to_add)
      await ctx.send(f'message added successfully ')
      messages.append(message_to_add)
@bot.command()
async def Quizz(ctx):
      await ctx.send("Choose your diffuculty \n 1.easy \n2.medium \n3.hard")


bot.run(TOKEN)

    