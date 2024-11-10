import time

current_time = time.strftime("%H:%M:%S")

def get_time():
    if current_time < "12:00:00":
        return "Good morning! 🌄"
    elif "12:00:00" < current_time < "18:00:00":
        return "Good afternoon! 🌞"
    else:
        return "Good evening! 🌙"

async def on_message(self, message):
        if message.author == self.user:
            return
    
        if message.content.lower() == "hello" or "hi":
            await message.reply(f"Hello! {get_time()}  {message.author.mention}", mention_author=False)