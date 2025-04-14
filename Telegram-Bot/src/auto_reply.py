#!/usr/bin/env python3
import asyncio
from telethon import TelegramClient, events
from os import getenv
from dotenv import load_dotenv
from google import genai

load_dotenv()
PROMPT = "You are a helpful assistant. Answer the user's questions as best as you can."

# Read credentials from .env
api_id = int(getenv("API_ID"))
api_hash = getenv("API_HASH")

class CustomClient(TelegramClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__client = genai.Client(api_key=getenv("API_KEY"))

    async def start_bot(self):
        await self.start()
        print("✅ UserBot started successfully.")

        # Add event handler
        self.add_event_handler(self.auto_reply, events.NewMessage(incoming=True))

        print("💬 Listening for messages...")
        await self.run_until_disconnected()

    async def auto_reply(self, event):
        sender = await event.get_sender()
        sender_name = sender.first_name if sender else "Someone"
        message_text = event.raw_text

        print(f"📨 {sender_name} said: {message_text}")

        response = self.__client.models.generate_content(
            model="gemini-2.0-flash", contents=PROMPT + message_text
        )

        # Reply to the message
        # await event.reply("Auto-reply: I got your message!")
        await event.reply("Favour is not currently online feel free to talk to my assistant\n\n" + response.text)

# Entry point
if __name__ == '__main__':
    client = CustomClient('my_userbot', api_id, api_hash)
    asyncio.run(client.start_bot())
