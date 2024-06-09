from typing import Final
from telegram import Update,Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes,ConversationHandler

from utils.event_info import event_infor_message, help_info_message
from utils.registation import register, name, email, tickets, cancel, NAME,EMAIL, TICKETS

from dotenv import load_dotenv
import os

load_dotenv()

Token:Final=os.getenv('TOKEN')
BOT_USERNAME: Final=os.getenv('BOT_USERNAME')

# Commands
async def start_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(event_infor_message(),parse_mode="HTML")

async def help_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(help_info_message(),parse_mode="HTML")

#Cansel the registation process
async def cancel_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await cancel(update,context)
    await update.message.reply_text(
        "Registration process canceled. \nTo start a new process, use the /register command."
    )

if __name__=='__main__':
    app=Application.builder().token(Token).build()

    #commands
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('cancel',cancel_command))

    # Registration conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('register', register)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, name)],
            EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, email)],
            TICKETS: [MessageHandler(filters.TEXT & ~filters.COMMAND, tickets)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    app.add_handler(conv_handler)
    
    
    #Polls the bot
    print("polling")
    app.run_polling()

    
