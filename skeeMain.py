from xml.sax import default_parser_list
import discord
from discord import Embed
import requests
import json
from dotenv import load_dotenv
import os
import defs

#CREDENTIALS 
load_dotenv('.env')

#FORMATING TO DO:
#GET THE DEFS INTO ANOTHER FILE AND CLEAR THE CLUTTER
#MAKE THE LISTS GLOBAL TO THE PROJECT 
#ADD USER INPUT FOR THE PLAYER!
#CLEAN UP THE CODE THIS LOOKS HORRIBLE!

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!name'):
        await message.channel.send(defs.getName())

    if message.content.startswith('!level'):
        embed = defs.sendLevel()
        await message.channel.send(embed=embed)

    if message.content.startswith('!rank'):
        embed = defs.sendRank()
        await message.channel.send(embed=embed)

    # -------------------------------------------------------------------------- TOP DPS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if message.content.startswith('!topDPS'):
        embed = defs.sendTopDPS()
        await message.channel.send(embed=embed)
    # -------------------------------------------------------------------------- TOP DPS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # -------------------------------------------------------------------------- TOP TANKS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if message.content.startswith('!topTanks'):
        embed = defs.sendTopTanks()
        await message.channel.send(embed=embed)
    # -------------------------------------------------------------------------- TOP TANKS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # -------------------------------------------------------------------------- TOP SUPPORTS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if message.content.startswith('!topSupports'):
        embed = defs.sendTopSupports()
        await message.channel.send(embed=embed)
    # -------------------------------------------------------------------------- TOP SUPPORTS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        

client.run(os.getenv('TOKEN'))