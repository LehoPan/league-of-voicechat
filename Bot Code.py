
import discord
import random

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

# insert your token, Looks like: radomstuffiop3421ihof81h4.oicalc.random-dashes-too-108hnco18nc-198hcs
# Either a google api token or its the discord bot token oops, I think it's discord bot
# TOKEN = 

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

client = gspread.authorize(creds)

sheet = client.open("League Prox Database").sheet1

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    member = message.author
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'league-proximity-setup':
        if user_message.lower() == 'hello':
            await message.channel.send(f'blow up {member.mention}')
            sheet.update_cell(2, 3, 1)

            return

client.run(TOKEN)