import discord
from discord.ext import commands 
import os
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('Token')

if token is None:
    raise ValueError("No token found in environment variables. Make sure 'Token' is set in your .env file.")


class MyClient(discord.Client):
    async def on_ready(self):
        print("ByteMe in now online")
    
    from funx.hello import on_message
    from funx.pong import on_message

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)