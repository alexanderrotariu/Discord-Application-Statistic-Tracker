import requests

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
userProfile = response.json()


#GETTING USER PROFILE 
def getName():
    return userProfile['name']

#GETTING USER LEVEL
def getLevel():
    fullLevel = userProfile['level'] + userProfile['prestige']*100
    return fullLevel

#GETTING USER RANK
def getRank():
    return userProfile['rating']

#GETTING TOP HEROES OF THE USER 
def getTopHeroes():
    return userProfile['competitiveStats']['topHeroes']

def getUserIcon():
    return userProfile['icon']

def getRankIcon():
    return userProfile['ratingIcon']

def getQpAvgElims():                       
    return userProfile['quickPlayStats']['careerStats']['allHeroes']['average']['eliminationsAvgPer10Min']

def getQpAvgDeaths():
    return userProfile['quickPlayStats']['careerStats']['allHeroes']['average']['deathsAvgPer10Min']

def getQpAvgFinalBlows():
    return userProfile['quickPlayStats']['careerStats']['allHeroes']['average']['finalBlowsAvgPer10Min']

def getQpAvgHealingDone():
    return userProfile['quickPlayStats']['careerStats']['allHeroes']['average']['healingDoneAvgPer10Min']

def getQpAvgDmgDone():
    return userProfile["quickPlayStats"]['careerStats']['allHeroes']['average']["heroDamageDoneAvgPer10Min"]

#---------------------------------------------------------------------------------------------------------------------------------

def getCompAvgDmgDone():
    return userProfile["competitiveStats"]['careerStats']['allHeroes']['average']["heroDamageDoneAvgPer10Min"]
    
def getCompAvgElims():                       
    return userProfile['competitiveStats']['careerStats']['allHeroes']['average']['eliminationsAvgPer10Min']

def getCompAvgDeaths():
    return userProfile['competitiveStats']['careerStats']['allHeroes']['average']['deathsAvgPer10Min']

def getCompAvgFinalBlows():
    return userProfile['competitiveStats']['careerStats']['allHeroes']['average']['finalBlowsAvgPer10Min']

def getCompAvgHealingDone():
    return userProfile['competitiveStats']['careerStats']['allHeroes']['average']['healingDoneAvgPer10Min']

def getCompAvgDmgDone():
    return userProfile["competitiveStats"]['careerStats']['allHeroes']['average']["heroDamageDoneAvgPer10Min"]

#-----------------------------------------------------------------------------------------------------------------

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
