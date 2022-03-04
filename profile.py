from turtle import width
from discord import Embed
import requests
from dotenv import load_dotenv
from operator import index, itemgetter
from pathlib import Path
from heroIconLinks import heroUrl

platform = 'pc'
Region = 'us'
battleTag = None
comma = ","

dpsList = ['ashe', 'bastion', 'doomfist', 'echo', 'genji', 'hanzo', 'junkrat', 'cassidy', 'mei', 'reaper', 'soldier76', 'sombra', 'symmetra', 'torbjorn', 'tracer', 'widowmaker']
tankList = ['dVa','reinhardt', 'roadhog', 'sigma','winston', 'wreckingBall', 'zarya','orisa']
supportList = ['ana','baptiste', 'brigitte','lucio','mercy', 'moira', 'zenyatta']

dpsTimes = []
tankTimes = []
supportTimes = []

#GET https://ow-api.com/v1/stats/:platform/:region/:battletag/heroes/:heroes 
#                                                                    WHERE HEROES IS THE LIST OF HEROES YOU WOULD LIKE

response = requests.get('https://ow-api.com/v1/stats/pc/us/SkeeCoops-1827/complete')
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

def getUserIcon():
    return profile['icon']

def getRankIcon():
    return profile['ratingIcon']