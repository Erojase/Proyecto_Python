import discord #importamos para conectarnos con el bot
from discord.ext import commands #importamos los comandos
import datetime, random

TOKEN = "MTA2ODE5NjM5NDY4NDQwMzcxMg.GYn8CD.2mkqKwUufUzX0WS-bKTRJWUaL7KjuMioLAQ_kQ"
ID_CANAL = "1068194499454578840"


bot = commands.Bot(command_prefix='¡', description="Robot Asistente de prueba", help_command=None, intents=discord.Intents.all())

#Status
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="como aprobar Python"))
    print('Bot en funcionamiento')

#Saludos
@bot.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
  
    print(f'Message {user_message} by {username} on {channel}')
  
    if message.author == bot.user:
        return
  
    if channel == "general":
        if user_message.lower() == "hola" or user_message.lower() == "ey":
            await message.channel.send(f'Hola {username}')
            return
        elif user_message.lower() == "adios":
            await message.channel.send(f'Adiós {username}')
        elif user_message.lower() == "chiste":
            jokes = [" Can someone please shed more\
            light on how my lamp got stolen?",
                     "Why is she called llene? She\
                     stands on equal legs.",
                     "What do you call a gazelle in a \
                     lions territory? Denzel."]
            await message.channel.send(random.choice(jokes))

# #Run y token
# bot.run(f'{TOKEN}')

