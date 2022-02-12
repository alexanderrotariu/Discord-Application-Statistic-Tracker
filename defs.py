import discord
from discord import Embed
import requests
import json
from dotenv import load_dotenv
import os
from operator import itemgetter


#DEFAULT PC, US
#NEED ADD USER INPUT FOR PLATFORM, REGION, AND BATTLETAGS.
#WILL HAVE TO CONSIDER 
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

#GETTING USER PROFILE 
def getName():
    return profile['name']

#GETTING USER LEVEL
def getLevel():
    fullLevel = profile['level'] + profile['prestige']*100
    return fullLevel

#GETTING USER RANK
def getRank():
    return profile['rating']

#GETTING TOP HEROES OF THE USER 
def getTopHeroes():
    return profile['competitiveStats']['topHeroes']

#CONVERTING HERO HOURS TO SECONDS
def hourSeconds(heroTime):
    hourSecs = 0
    splitTimes = heroTime.split(":")

    hours = int(splitTimes[0])
    hourSecs =  hours * 3600

    return hourSecs

#CONVERTING HERO MINUTES TO SECONDS 
def minutesSeconds(heroTime):
    minSecs = 0 
    splitTimes = heroTime.split(":")

    minutes = int(splitTimes[1])
    minSecs = minutes * 60 

    return minSecs

#GETTING HERO SECONDS 
def heroSeconds(heroTime):
    seconds = 0
    splitTimes = heroTime.split(":")
    
    seconds = int(splitTimes[2])
    #no further arithmetic???
    return seconds 

#ADDING ALL THE SECONDS GATHERED TO A TOTAL SECONDS 
def totalSeconds(heroTime):
    totalSeconds = 0 
    
    hourSecs = hourSeconds(heroTime)
    minSecs = minutesSeconds(heroTime)
    seconds = heroSeconds(heroTime)

    totalSeconds = hourSecs + minSecs + seconds

    return totalSeconds

#COMPUTING THE BORDER OF A USER 
def getBorder():

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

    return borderType

#SETTING UP THE EMBED AND GETTING LEVEL AND BORDER OF A USER 
def sendLevel():
    embed = Embed(title=getName()+"'s Level", color=0xf04c9e)
    embed.add_field(name="Level:", value=getLevel())
    embed.set_thumbnail(url=profile['icon'])

    borderType = getBorder()

    embed.add_field(name= "Border:", value= borderType, inline= True)

    return embed

#SETTING UP EMBEED AND GETTING RANK FOR A USER ALONG WITH A PNG OF THE RANK
def sendRank():
    embed = Embed(title=getName()+"'s Rank", color=0xf04c9e)
    embed.add_field(name="Rank:", value=getRank())
    embed.set_thumbnail(url=profile['ratingIcon'])
    
    return embed

def getTopDPS():
    heroTimeSeconds = []
    for i in dpsList:
        try:
            if(len(profile['competitiveStats']['topHeroes'][i]['timePlayed']) > 5 ):
                dpsTimes.append(profile['competitiveStats']['topHeroes'][i]['timePlayed'])
            else:
                dpsTimes.append("00:" + profile['competitiveStats']['topHeroes'][i]['timePlayed'])

        except KeyError:
            dpsTimes.append("00:00:00")

    #Making the hero time in seconds list here:
    for i in range(0, len(dpsTimes)):
        heroTimeSeconds.append(int(totalSeconds(dpsTimes[i])))

    #Making a list of lists 
    #heroNameAndSeconds = [dpsList, heroTimeSeconds]
    heroNameAndSeconds = list(zip(dpsList, heroTimeSeconds))
    print(heroNameAndSeconds)

    #new list called output that is sorted by the time list.
    output = sorted(heroNameAndSeconds, key= itemgetter(1), reverse=True)
    print(output)

    #2D ARRAY HAS BECOME SORTED, ALL THATS LEFT IS A INDEX ERROR ISSUE

   # output = heroTimeSeconds.sort()    
    return output 

#FIX THIS METHOD NEXT SESSION !!!!!!!!!!!!!!
def sendTopDPS():
    sortedDPS = getTopDPS()

    msg = ""

    for i in range(1, len(dpsList)):
        msg = msg + str(i) + ") "+ str(sortedDPS[0][i]) + " : " + str(sortedDPS[1][i]) + "seconds \n"

    return msg


    
