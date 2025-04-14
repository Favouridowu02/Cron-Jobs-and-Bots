#!/usr/bin/env python3
"""
    Telegram Bot for autoreplying messages
    It leverages Gemini AI to generate responses
"""
from dotenv import load_dotenv
from os import getenv


from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

load_dotenv()

def auto_reply(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    reply_message = f"You said: {user_message}"
    
    # Send reply back to the chat
    update.message.reply_text(reply_message)

def main():
    # Replace this with your actual bot token from BotFather
    updater = Updater(getenv("BOT_TOKEN"))

    dispatcher = updater.dispatcher

    # Register a handler for any text message
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, auto_reply))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
