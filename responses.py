import requests
from telegram.ext import *

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "hey"):
        return "Hello! I am a bot nice to meet you"
    if user_message in ("check price", "bitcoin", "etheruam"):
        return "I am still in development do come back later"
   # if user_message in ("/p"):
        
    return "I dont understand bro."


