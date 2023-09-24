import discord
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True 
client = discord.Client(intents=intents)

# Prints when the bot is ready for use.
@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    
    message.content = message.content.upper();
    # Debugging message to see the content of the message.
    print(f'Message content: {message.content}')

    # prevents from self looping because the bot send a message itself.
    if message.author == client.user:
        return
    # sends local files which are pictures.
    elif message.content.startswith('!ERIK'):
        await message.channel.send(file=discord.File('Erik.JPG'))

    elif message.content.startswith('!DAVID'):
        await message.channel.send('I hate David',file=discord.File('David.JPEG'))

    elif message.content.startswith('!JOHN'):
        await message.channel.send(file=discord.File('John.JPG'))
        
    elif message.content.startswith('!RAFA'):
        await message.channel.send(file=discord.File('Rafa.JPG'))

    elif message.content.startswith('!MOMO'):
        await message.channel.send(file=discord.File('Momo.JPG'))

    elif message.content.startswith('!ESTELA'):
        await message.channel.send(file=discord.File('Estela.PNG'))
    
    # Works with different APIs to get insults and random cat facts.    
    elif message.content.startswith('!CAT FACT'):
        responce = requests.get("https://meowfacts.herokuapp.com/").json()
        json_fact = responce['data'][0]
        await message.channel.send(f"{message.author.mention} {json_fact}")
    
client.run(TOKEN)