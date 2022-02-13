import discord
from discord import Embed
import requests
import json
from dotenv import load_dotenv
import os
from operator import itemgetter
from pathlib import Path


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

file = None

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


#DPS ------------------------------------------------------------------------------------------------------------------------------------------------------

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
    heroNameAndSeconds = list(zip(dpsList, heroTimeSeconds))

    #new list called output that is sorted by the time list.
    output = sorted(heroNameAndSeconds, key= itemgetter(1), reverse=True)

    #2D ARRAY HAS BECOME SORTED
    return output 

def sendTopDPS():
    embed = Embed(title=getName()+"'s top DPS heroes:", color=0xf04c9e)

    sortedDPS = getTopDPS()

    msg = ""

    for i in range(0, len(dpsList)):
        msg = msg + str(i+1) + ") "+ str(sortedDPS[i][0].capitalize()) + "\n"
    
    embed.add_field(name="Most played to least played:", value=msg)
    
    topHero = sortedDPS[0][0].capitalize()

    heroUrl= {
        'Ashe': "https://cdn.discordapp.com/attachments/737088061250207859/942213813774716958/Icon-Ashe.png",
        'Bastion': "https://cdn.discordapp.com/attachments/737088061250207859/942213939641585704/Icon-Bastion.png",
        'Doomfist':"https://cdn.discordapp.com/attachments/737088061250207859/942213940090392576/Icon-Doomfist.png",
        'Echo':"https://cdn.discordapp.com/attachments/737088061250207859/942213940610465822/Icon-Echo.png", 
        'Genji':"https://cdn.discordapp.com/attachments/737088061250207859/942213940795047996/Icon-Genji.png",
        'Hanzo':"https://cdn.discordapp.com/attachments/737088061250207859/942213939167649792/Icon-Hanzo.png",
        'Junkrat':"https://cdn.discordapp.com/attachments/737088061250207859/942214168377962557/Icon-Junkrat.png",
        'Cassidy':"https://cdn.discordapp.com/attachments/737088061250207859/942217757578121286/Icon-Cassidy.png",
        'Mei':"https://cdn.discordapp.com/attachments/737088061250207859/942214168935800862/Icon-Mei.png",
        'Reaper':"https://cdn.discordapp.com/attachments/737088061250207859/942214170575790090/Icon-Reaper.png",
        'Soldier76':"https://cdn.discordapp.com/attachments/737088061250207859/942214212904689694/Icon-Soldier_76.png",
        'Sombra':"https://cdn.discordapp.com/attachments/737088061250207859/942214213223469096/Icon-Sombra.png",
        'Symmetra':"https://cdn.discordapp.com/attachments/737088061250207859/942214213416398868/Icon-Symmetra.png",
        'Torbjorn':"https://cdn.discordapp.com/attachments/737088061250207859/942214213739372604/Icon-Torbjorn.png",
        'Tracer':"https://cdn.discordapp.com/attachments/737088061250207859/942214213999403038/Icon-Tracer.png",
        'Widowmaker':"https://cdn.discordapp.com/attachments/737088061250207859/942214214230081556/Icon-Widowmaker.png"
    }
    
    hUrl = heroUrl[topHero]
    embed.set_thumbnail(url=hUrl)


    return embed

#DPS ------------------------------------------------------------------------------------------------------------------------------------------------------

#TANK -----------------------------------------------------------------------------------------------------------------------------------------------------
    
def getTopTanks():
    heroTimeSeconds = []
    for i in tankList:
        try:
            if(len(profile['competitiveStats']['topHeroes'][i]['timePlayed']) > 5 ):
                tankTimes.append(profile['competitiveStats']['topHeroes'][i]['timePlayed'])
            else:
                tankTimes.append("00:" + profile['competitiveStats']['topHeroes'][i]['timePlayed'])

        except KeyError:
            tankTimes.append("00:00:00")

    #Making the hero time in seconds list here:
    for i in range(0, len(tankTimes)):
        heroTimeSeconds.append(int(totalSeconds(tankTimes[i])))

    #Making a list of lists 
    heroNameAndSeconds = list(zip(tankList, heroTimeSeconds))

    #new list called output that is sorted by the time list.
    output = sorted(heroNameAndSeconds, key= itemgetter(1), reverse=True)

    #2D ARRAY HAS BECOME SORTED
    return output 

def sendTopTanks():
    embed = Embed(title=getName()+"'s top tank heroes:", color=0xf04c9e)

    sortedTanks = getTopTanks()

    msg = ""

    for i in range(0, len(tankTimes)):
        msg = msg + str(i+1) + ") "+ str(sortedTanks[i][0].capitalize()) + "\n"

    embed.add_field(name="Most played to least played:", value=msg)


    topHero = sortedTanks[0][0].capitalize()

    heroUrl= {
        'Dva':"https://cdn.discordapp.com/attachments/737088061250207859/942213940383989801/Icon-Dva.png",
        'Reinhardt':"https://cdn.discordapp.com/attachments/737088061250207859/942214171011973120/Icon-Reinhardt.png",
        'Roadhog':"https://cdn.discordapp.com/attachments/737088061250207859/942214212334256139/Icon-Roadhog.png",
        'Sigma':"https://cdn.discordapp.com/attachments/737088061250207859/942214212623695944/Icon-Sigma.png",
        'Winston':"https://cdn.discordapp.com/attachments/737088061250207859/942214214527909979/Icon-Winston.png",
        'Wreckingball':"https://cdn.discordapp.com/attachments/737088061250207859/942214228960501790/Icon-Wrecking_Ball.png",
        'Zarya':"https://cdn.discordapp.com/attachments/737088061250207859/942214229157609502/Icon-Zarya.png",
        'Orisa':"https://cdn.discordapp.com/attachments/737088061250207859/942214169904685106/Icon-Orisa.png"
    }
        
    hUrl = heroUrl[topHero]
    embed.set_thumbnail(url=hUrl)


    return embed

#TANK -----------------------------------------------------------------------------------------------------------------------------------------------------
#SUPPORT --------------------------------------------------------------------------------------------------------------------------------------------------
def getTopSupports():
    heroTimeSeconds = []
    for i in supportList:
        try:
            if(len(profile['competitiveStats']['topHeroes'][i]['timePlayed']) > 5 ):
                supportTimes.append(profile['competitiveStats']['topHeroes'][i]['timePlayed'])
            else:
                supportTimes.append("00:" + profile['competitiveStats']['topHeroes'][i]['timePlayed'])

        except KeyError:
            supportTimes.append("00:00:00")

    #Making the hero time in seconds list here:
    for i in range(0, len(supportTimes)):
        heroTimeSeconds.append(int(totalSeconds(supportTimes[i])))

    #Making a list of lists 
    heroNameAndSeconds = list(zip(supportList, heroTimeSeconds))

    #new list called output that is sorted by the time list.
    output = sorted(heroNameAndSeconds, key= itemgetter(1), reverse=True)

    #2D ARRAY HAS BECOME SORTED
    return output 

def sendTopSupports():
    embed = Embed(title=getName()+"'s top support heroes:", color=0xf04c9e)

    sortedSupports = getTopSupports()

    msg = ""

    for i in range(0, len(supportTimes)):
        msg = msg + str(i+1) + ") "+ str(sortedSupports[i][0].capitalize()) + "\n"

    embed.add_field(name="Most played to least played:", value=msg)

    topHero = sortedSupports[0][0].capitalize()

    heroUrl= {
        'Ana':"https://cdn.discordapp.com/attachments/737088061250207859/942213722011742218/Icon-Ana.png",
        'Baptiste':"https://cdn.discordapp.com/attachments/737088061250207859/942213939406716948/Icon-Baptiste.png",
        'Brigitte':"https://cdn.discordapp.com/attachments/737088061250207859/942213939859718164/Icon-Brigitte.png",
        'Lucio':"https://cdn.discordapp.com/attachments/737088061250207859/942214168646418512/Icon-Lucio.png",
        'Mercy':"https://cdn.discordapp.com/attachments/737088061250207859/942214169162309672/Icon-Mercy.png",
        'Moira':"https://cdn.discordapp.com/attachments/737088061250207859/942214169577533500/Icon-Moira.png",
        'Zenyatta':"https://cdn.discordapp.com/attachments/737088061250207859/942214229337976912/Icon-Zenyatta.png"
    }
        
    hUrl = heroUrl[topHero]
    embed.set_thumbnail(url=hUrl)


    return embed

#SUPPORT --------------------------------------------------------------------------------------------------------------------------------------------------
