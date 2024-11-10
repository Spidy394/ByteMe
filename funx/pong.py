async def on_message(self, message):
    if message.author == self.user:
        return
    
    if message.content.lower() == 'ping':
        latency = round(self.latency * 1000) 
        await message.reply(f"Pong! 🏓 {latency}ms", mention_author=True)