import random
import asyncio

async def on_message(self, message):
    if message.author == self.user:
        return
    
    if message.content.startswith('&guess'):
        await message.reply('Guess a number b/w 1 to 10')

        def is_correct(m):
            return m.author == message.author and m.content.isdigit()

        ans = random.randint(1, 10)

        try:
            guess = await self.wait_for('message', check=is_correct, timeout=5.0)
        except asyncio.TimeoutError:
            return await message.channel.send(f"Sorry, you took too long it was `**{ans}**`.")
        
        if int(guess.content) == ans:
            await guess.reply("Bang! You got it right 🎉")
        else:
            await guess.reply(f"Oops. Its actually **`{ans}`**")