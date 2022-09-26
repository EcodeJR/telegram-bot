# telegram-bot
It's a basic telegram bot that's supposed to get the information from users and passes the info to rapid api and send the data as a message to the user in telegram

ISSUE
#passing the users input into the api
#here i tried spliting the input of the user so as to get just the second
#and third data eg(/p bitcoin usd)this is supposed to be the users input
#and this is the output: {"bitcoin":{"usd":19119.03}}
#but the code doesn't work and i need assistance

HOW TO USE:
Create a bot with Botfather on telegram
insert you bot key in constants.py

Setting up rapid api

-create an account on https://rapidapi.com/

-add your rapidapi key to main.py

OR

-goto https://rapidapi.com/coingecko/api/coingecko
-after you're logged in and copy your api key from there
#you'll see it in the code snippet section:
    headers = {
        "X-RapidAPI-Key": "You're key would be here",
        "X-RapidAPI-Host": "coingecko.p.rapidapi.com"
    }


And run the main.py script

-Search for the name of your bot on telegram

-And HELP me out on the isssue
