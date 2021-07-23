import requests

import json

import re

from discord.ext import commands

bot = commands.Bot(command_prefix='$k!')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('hello koneko'):
        await message.channel.send('Hello !')

    if bot.user.mentioned_in(message):

        msg = message.content 

        newmsg = re.sub(r"""[/<@!](.*?)[>/]""", " ", msg)

        if  newmsg == ' ' :
             return
        
        repond = newmsg.lower()

        url = f"Your api"
        
        response = requests.get(url, verify=True)
        
        data2 = json.dumps(response.json())

        res = json.loads(data2)

        await message.channel.send(res["message"])
        
        

bot.run('Your token')