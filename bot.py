import discord
from dotenv import load_dotenv
import os
from openai_api import get_openai_response

load_dotenv()

token = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} is now running!')
    await send_introduction_message()

async def send_introduction_message():
    for guild in client.guilds:  # Loop through all guilds (servers) the bot is in
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                # Check if bot can send messages in the channel
                await channel.send("Hmm... Kept you waiting, huh. I can help with your code. Start your message with '!explain' to explain your code, '!code' to give suggestions on how to code something, '!debug' to debug your code, or 'stop' for me to leave")
                return

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.lower() == 'stop':
        await message.channel.send("Snake, out")
    
    elif message.content.startswith('!explain'):
        code_snippet = message.content[len('!explain '):]
        response = get_openai_response(code_snippet, purpose='explain')
        await message.channel.send(response)

    elif message.content.startswith('!debug'):
        code_snippet = message.content[len('!debug '):]
        response = get_openai_response(code_snippet, purpose='debug')
        await message.channel.send(response)
        
    elif message.content.startswith('!code'):
        task_description = message.content[len('!code '):]
        response = get_openai_response(task_description, purpose='code')
        await message.channel.send(response)
    
    else:
        await message.channel.send("Hmm... Wrong response. Try again.")

client.run(token)