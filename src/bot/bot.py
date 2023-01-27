import discord #importamos para conectarnos con el bot
from discord.ext import commands #importamos los comandos
import datetime, random, os
from dotenv import load_dotenv #importamos token
load_dotenv()

TOKEN = os.getenv('TOKEN')
PREFIX = '!'
bot = commands.Bot(command_prefix = PREFIX, description="Robot Asistente de prueba", help_command=None, intents=discord.Intents.all())

#Status
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="como aprobar Python"))
    print('Bot en funcionamiento')


#Comandos
async def cmd(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)[1:]
    
    #Saludos y 
    if user_message.lower() == "hola" or user_message.lower() == "ey":
        await message.channel.send(f'Hola {username}')
        return
    
    elif user_message.lower() == "adios" or user_message.lower() == "bye":
        await message.channel.send(f'Adiós {username}')
        return
    
    elif user_message.lower() == "chiste":
        jokes = [" Can someone please shed more light on how my lamp got stolen?",
                 "Why is she called llene? She stands on equal legs.",
                 "What do you call a gazelle in a lions territory? Denzel."]
        await message.channel.send(random.choice(jokes))
        return
    



#IA
async def ia(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    await message.channel.send('PRUEBA DE RESPUESTA IA')
    return


#MENSAJES
@bot.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
  
    print(f'Message {user_message} by {username} on {channel}')
  
    if message.author == bot.user:
        return
    
    if PREFIX in user_message.lower():
        await cmd(message)
    
    if channel == "chatbot":
        await ia(message)

# #Run y token
# bot.run(f'{TOKEN}')


