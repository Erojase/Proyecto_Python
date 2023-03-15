import discord #importamos para conectarnos con el bot
from discord.ext import commands #importamos los comandos
import datetime, random, os
from dotenv import load_dotenv #importamos EL token
from chatterbot import ChatBot #importamos el chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer #importamos el entrenador
import json
from flask import jsonify
from src.services.dbManager import *
load_dotenv()

db:DbManager = DbManager()

TOKEN = os.getenv('TOKEN')

PREFIX = '!'

bot = commands.Bot(command_prefix = PREFIX, description="Robot Asistente de prueba", help_command=None, intents=discord.Intents.all())

ia_bot = ChatBot(name='Tick', read_only=True, logic_adapters=['chatterbot.logic.MathematicalEvaluation','chatterbot.logic.BestMatch'])
trainer = ChatterBotCorpusTrainer(ia_bot)
trainer.train(
    "src/bot/spanish/conver.yml",
    "src/bot/spanish/dinero.yml",
    "src/bot/spanish/emociones.yml",
    "src/bot/spanish/greetings.yml",
    "src/bot/spanish/ia.yml",
    "src/bot/spanish/perfil.yml",
    "src/bot/spanish/psicologia.yml",
    "src/bot/spanish/trivia.yml"
)

#Status
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="como aprobar Python"))
    print('Bot en funcionamiento')

#IA
@bot.event
async def on_message(message):
    channel = str(message.channel.name)
    username = str(message.author).split("#")[0]
    user_message = str(message.content)

    if message.author == bot.user:
        return

    if channel == "chatbot" and not user_message.startswith(PREFIX):
        await message.channel.send(ia_bot.get_response(user_message))
        
    #PING
    if user_message == '!ping':
        await message.channel.send("PONG!")
        
    #HOLA
    if user_message == '!hola':
        await message.channel.send(f'Hola {username}')
        
    #ADIOS
    if user_message == '!adios':
        await message.channel.send(f'Adiós {username}')
        
    #CHISTE
    if user_message == '!chiste':
        jokes = ["¿Qué le dice el uno al diez? Para ser como yo tenés que ser sincero",
                  "¿Qué le dijo un pato a otro pato? Estamos empatados",
                  "¿Qué le dijo un mosquito a un grupo de niños? No aplaudas, que todavía no es mi cumpleaños"]
        await message.channel.send(random.choice(jokes))
        
    #LIST_USERS
    if user_message == '!list_users':
        users = db.listUsersNick()
        for i in users:
            await message.channel.send(json.dumps(i['nick']))
            
    #LIST_USERS
    if user_message.startswith('!list_users'):       
        user_message = user_message.split()[1]
        print(user_message)
        users = db.listOneUserStats(user_message)
        for i in users:
            await message.channel.send(json.dumps(i['nick']))
            await message.channel.send(json.dumps(i['nombre']))
            await message.channel.send(json.dumps(i['mail']))
            await message.channel.send(json.dumps(i['tipo']))
            await message.channel.send(json.dumps(i['asignaturas']))
            await message.channel.send(json.dumps(i['horario']))
            
    #LIST_GRUPOS
    if user_message == '!list_grupos':
        users = db.listGruposName()
        for i in users:
            await message.channel.send(json.dumps(i['nombre']))
            
    #LIST_ASIGNATURAS
    if user_message == '!list_asignaturas':
        users = db.listAsignaturasName()
        for i in users:
            await message.channel.send(json.dumps(i['nombre']))
    
            
    # await bot.process_commands(message)


# #Run y token
# bot.run(f'{TOKEN}')


#PING
# @bot.command()
# async def ping(ctx):
#     await ctx.channel.send("PONG!")

# #HOLA
# @bot.command()
# async def hola(ctx):
#     username = str(ctx.author).split("#")[0]
#     await ctx.channel.send(f'Hola {username}')

# #ADIOS
# @bot.command()
# async def adios(ctx):
#     username = str(ctx.author).split("#")[0]
#     await ctx.channel.send(f'Adiós {username}')

# #CHISTE 
# @bot.command()
# async def chiste(ctx):
#     jokes = ["¿Qué le dice el uno al diez? Para ser como yo tenés que ser sincero",
#                  "¿Qué le dijo un pato a otro pato? Estamos empatados",
#                  "¿Qué le dijo un mosquito a un grupo de niños? No aplaudas, que todavía no es mi cumpleaños"]
#     await ctx.channel.send(random.choice(jokes))


# #LISTAR USUARIOS 
# @bot.command()
# async def list_users(ctx):
#     users = db.listUsers()
#     for i in users:
#         await ctx.channel.send(json.dumps(i['nombre']))