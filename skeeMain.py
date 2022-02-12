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

    #Will handle cleaning up top3 commands when sorting alg is finished.

    # -------------------------------------------------------------------------- TOP DPS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if message.content.startswith('!topDPS'):
        topDps = defs.sendTopDPS()
        await message.channel.send(topDps)

    # -------------------------------------------------------------------------- TOP DPS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if message.content.startswith('!topTanks'):
        for i in defs.tankList:
            try:
                if(len(defs.profile['competitiveStats']['topHeroes'][i]['timePlayed']) > 5 ):
                    defs.tankTimes.append(defs.profile['competitiveStats']['topHeroes'][i]['timePlayed'])
                else:
                    defs.tankTimes.append("00:" + defs.profile['competitiveStats']['topHeroes'][i]['timePlayed'])

            except KeyError:
                defs.tankTimes.append("00:00:00")

        defs.tankTimes.sort(reverse = True)

        #trying to find the total seconds on each tank
        await message.channel.send(defs.tankTimes)
        await message.channel.send(defs.tankList)


        tankListSecondTotals = []
        for i in range(0, len(defs.tankTimes)):
            tankListSecondTotals.append(defs.totalSeconds(defs.tankTimes[i]))

        await message.channel.send(tankListSecondTotals)
        
        
    if message.content.startswith('!topSupport'):
        for i in defs.supportList:
            try:
                if(len(defs.profile['competitiveStats']['topHeroes'][i]['timePlayed']) > 5 ):
                    defs.supportTimes.append(defs.profile['competitiveStats']['topHeroes'][i]['timePlayed'])
                else:
                    defs.supportTimes.append("00:" + defs.profile['competitiveStats']['topHeroes'][i]['timePlayed'])

            except KeyError:
                defs.supportTimes.append("00:00:00")
            
        
        defs.supportTimes.sort(reverse = True)

        await message.channel.send(defs.supportTimes)
        await message.channel.send(defs.supportList)

        supportListSecondTotals = []
        for i in range(0, len(defs.supportTimes)):
            supportListSecondTotals.append(defs.totalSeconds(defs.supportTimes[i]))

        await message.channel.send(supportListSecondTotals)

client.run(os.getenv('TOKEN'))