import discord
from discord.ext import commands 
import os
from dotenv import load_dotenv
import pytz


load_dotenv()
token = os.getenv('Token')
if token is None:
    raise ValueError("No token found in environment variables. Make sure 'Token' is set in your .env file.")

local_timezone = pytz.timezone("Asia/Kolkata")

class MyClient(discord.Client):
    async def on_ready(self):
        print("ByteMe in now online")
    
    async def on_message(self, message):
        print(f"Message from \"{message.author}\" => \"{message.content}\" in \"{message.channel}\" at {message.created_at.astimezone(local_timezone)} of \"{message.guild}\"")
        if message.author == self.user:
            return
        
        


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)