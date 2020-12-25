import discord
import os
import requests
import json
from keep_alive import keep_alive

client = discord.Client()

kanye_words = ["ye", "Ye", "kanye", "Kanye", "yeezy", "Yeezy", "yzy", "YZY"]

def get_quote():
  response = requests.get("https://api.kanye.rest")
  json_data = json.loads(response.text)
  quote = json_data['quote']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if any(word in message.content for word in kanye_words):
    quote = get_quote()
    await message.channel.send(quote)
keep_alive()
client.run(os.getenv('TOKEN'))
