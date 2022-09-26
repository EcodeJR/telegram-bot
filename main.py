
import constants as keys
from telegram.ext import *
import responses as R
import requests




print("Bot is live...")


def start_command(update, context):
    update.message.reply_text("Welcome to crypto ckecker")
    
def help_command(update, context):
    update.message.reply_text("Check any coin by entering /p name of coin and currency you want it in.")

def p_command(update, context):
    N = 3

    url = "https://coingecko.p.rapidapi.com/simple/price"

#passing the users input into the api
#here i tried spliting the input of the user so as to get just the second
#and third data eg(/p bitcoin usd)this is supposed to be the users input
#and this is the output: {"bitcoin":{"usd":19119.03}}
#but the code doesn't work and i need assistance
    querystring = {"ids":str(update.message.split(' ')[N-2]).lower(),"vs_currencies":str(update.message.split(' ')[N-3]).lower()}

    headers = {
        "X-RapidAPI-Key": "YOUR RAPID API KEY HERE",
        "X-RapidAPI-Host": "coingecko.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return(response)



def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} Caused error: {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("p", p_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle

main()