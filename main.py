
import constants as keys
from telegram.ext import *
import Responses as R



print("Bot started....")


def start_command(update,context):
    update.message.reply_text('Hello there!\U0001F44B\n\U0001F601This is a sample implementation of a chat bot for our stream seminar\nThis bot has been made by\n\nAshish Kumar Singh\U0001F60E\nAtul Gautam\nSiddharth Sharma\n\nThis bot will give you information about the McDonald\'s menu and you can also contact the customer service using this bot\n\nTo use this bot\n1.Type "menu" to see the menu\n2.Type "about" to see the aboust section')
   

def help_command(update,context):
    update.message.reply_text('how can i help you')


def handle_message(update,context):
    text=str(update.message.text).lower()
    response=R.sample_responses(text)

    update.message.reply_text(response) 
    
    
def error(update,context):
    print(f"Update {update} caused error {context.error}")
    
    
    
def main():
    updater=Updater(keys.API_KEY,use_context=True)
    dp=updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    
    
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    
    dp.add_error_handler(error)
    
    updater.start_polling()
    updater.idle()
    
    
    
main()