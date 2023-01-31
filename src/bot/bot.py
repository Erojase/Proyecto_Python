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

#DEVUELVE MENSAJE
@bot.command()
async def copy(ctx, arg):
    await ctx.channel.send(arg)

#PING
@bot.command()
async def ping(ctx):
    await ctx.channel.send("PONG!")

#HOLA
@bot.command()
async def hola(ctx):
    username = str(ctx.author).split("#")[0]
    await ctx.channel.send(f'Hola {username}')

#ADIOS
@bot.command()
async def adios(ctx):
    username = str(ctx.author).split("#")[0]
    await ctx.channel.send(f'Adiós {username}')

#CHISTE 
@bot.command()
async def chiste(ctx):
    jokes = [" Can someone please shed more light on how my lamp got stolen?",
                 "Why is she called llene? She stands on equal legs.",
                 "What do you call a gazelle in a lions territory? Denzel."]
    await ctx.channel.send(random.choice(jokes))



#IA
@bot.event
async def on_message(message):
    channel = str(message.channel.name)
    username = str(message.author).split("#")[0]
    user_message = str(message.content)

    if message.author == bot.user:
        return

    if channel == "chatbot" and not user_message.startswith(PREFIX):
        await message.channel.send('PRUEBA DE RESPUESTA IA')
            
    await bot.process_commands(message)


# #Run y token
# bot.run(f'{TOKEN}')


