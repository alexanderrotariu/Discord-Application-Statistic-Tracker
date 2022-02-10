from distutils.command.config import config
from email import message
from importlib.metadata import requires
from operator import indexOf
import discord
from discord import Embed
import requests
import json
from dotenv import load_dotenv
import os

#CREDENTIALS 
load_dotenv('.env')


client = discord.Client()


platform = 'pc'
Region = 'us'
battleTag = 'Krusher99-1111'
comma = ","

dpsList = ['ashe', 'bastion', 'doomfist', 'echo', 'genji', 'hanzo', 'junkrat', 'cassidy', 'mei', 'reaper', 'soldier76', 'sombra', 'symmetra', 'torbjorn', 'tracer', 'widowmaker']
tankList = ['dVa','reinhardt', 'roadhog', 'sigma','winston', 'wreckingBall', 'zarya','orisa']
supportList = ['ana','baptiste', 'brigitte','lucio','mercy', 'moira', 'zenyatta']

dpsTimes = []
tankTimes = []
supportTimes = []

response = requests.get('https://ow-api.com/v1/stats/pc/us/SkeeCoops-1827/heroes/'+comma.join(dpsList))
profile = response.json()

def getName():
    return profile['name']

def getLevel():
    fullLevel = profile['level'] + profile['prestige']*100
    return fullLevel

def getRank():
    return profile['rating']


def getTopHeroes():
    return profile['competitiveStats']['topHeroes']

def hourSeconds(heroTime):
    hourSecs = 0
    splitTimes = heroTime.split(":")

    hours = int(splitTimes[0])
    hourSecs =  hours * 3600

    return hourSecs

def minutesSeconds(heroTime):
    minSecs = 0 
    splitTimes = heroTime.split(":")

    minutes = int(splitTimes[1])
    minSecs = minutes * 60 

    return minSecs

def heroSeconds(heroTime):
    seconds = 0
    splitTimes = heroTime.split(":")
    
    seconds = int(splitTimes[2])
    #no further arithmetic???
    return seconds 

def totalSeconds(heroTime):
    totalSeconds = 0 
    
    hourSecs = hourSeconds(heroTime)
    minSecs = minutesSeconds(heroTime)
    seconds = heroSeconds(heroTime)

    totalSeconds = hourSecs + minSecs + seconds

    return totalSeconds

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
        await message.channel.send(getName())

    if message.content.startswith('!level'):
        embed = Embed(title=getName()+"'s Level", color=0xf04c9e)
        embed.add_field(name="Level:", value=getLevel())
        embed.set_thumbnail(url=profile['icon'])

        # Determining the players border
        borderType = "Bronze"
        if 600 < getLevel() < 1200:
            borderType = "Silver"
        elif 1200 < getLevel() < 1800:
            borderType = "Gold"
        elif 1800 < getLevel() < 2400:
            borderType = "Platinum"
        elif 2400 < getLevel() < 3000:
            borderType = "Diamond"

        embed.add_field(name= "Border:", value= borderType, inline= True)
    
        await message.channel.send(embed=embed)
        #await message.channel.send(getLevel())

    if message.content.startswith('!rank'):
        embed = Embed(title=getName()+"'s Rank", color=0xf04c9e)
        embed.add_field(name="Rank:", value=getRank())
        embed.set_thumbnail(url=profile['ratingIcon'])
        
        await message.channel.send(embed=embed)

    if message.content.startswith('!top3DPS'):
        for i in dpsList:
            try:
                if(len(profile['competitiveStats']['topHeroes'][i]['timePlayed']) > 5 ):
                    dpsTimes.append(profile['competitiveStats']['topHeroes'][i]['timePlayed'])
                else:
                    dpsTimes.append("00:" + profile['competitiveStats']['topHeroes'][i]['timePlayed'])

            except KeyError:
                dpsTimes.append("00:00:00")

        #display the times of each hero
        await message.channel.send(dpsTimes)
        await message.channel.send(dpsList)

        dpsListSecondTotals = []
        for i in range(0, len(dpsTimes)):
            dpsListSecondTotals.append(totalSeconds(dpsTimes[i]))

        await message.channel.send(dpsListSecondTotals)

    if message.content.startswith('!top3Tanks'):
        for i in tankList:
            try:
                if(len(profile['competitiveStats']['topHeroes'][i]['timePlayed']) > 5 ):
                    tankTimes.append(profile['competitiveStats']['topHeroes'][i]['timePlayed'])
                else:
                    tankTimes.append("00:" + profile['competitiveStats']['topHeroes'][i]['timePlayed'])

            except KeyError:
                tankTimes.append("00:00:00")

        #trying to find the total seconds on each tank
        await message.channel.send(tankTimes)
        await message.channel.send(tankList)


        tankListSecondTotals = []
        for i in range(0, len(tankTimes)):
            tankListSecondTotals.append(totalSeconds(tankTimes[i]))

        await message.channel.send(tankListSecondTotals)
        
        
    if message.content.startswith('!top3Support'):
        for i in supportList:
            try:
                if(len(profile['competitiveStats']['topHeroes'][i]['timePlayed']) > 5 ):
                    supportTimes.append(profile['competitiveStats']['topHeroes'][i]['timePlayed'])
                else:
                    supportTimes.append("00:" + profile['competitiveStats']['topHeroes'][i]['timePlayed'])

            except KeyError:
                supportTimes.append("00:00:00")
            
        await message.channel.send(supportTimes)
        await message.channel.send(supportList)

        supportListSecondTotals = []
        for i in range(0, len(supportTimes)):
            supportListSecondTotals.append(totalSeconds(supportTimes[i]))

        await message.channel.send(supportListSecondTotals)

    if message.content.startswith('!printTopHeroesTC'):
        heroList = ['ashe', 'baptiste', 'brigitte', 'dVa', 'doomfist', 'echo',
                    'genji', 'hanzo', 'junkrat', 'lucio', 'mccree', 'mei',
                    'mercy', 'moira', 'reaper', 'reinhardt', 'roadhog', 'sigma',
                    'soldier76', 'sombra', 'symmetra', 'torbjorn', 'tracer', 'widowmaker',
                    'winston', 'wreckingBall', 'zarya', 'zenyatta']
        for i in range(0, len(heroList)):
            print(profile['competitiveStats']['topHeroes'][heroList[i]]['timePlayed']+"\n")



client.run(os.getenv('TOKEN'))