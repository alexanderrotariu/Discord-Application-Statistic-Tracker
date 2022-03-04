from turtle import width
import requests
from operator import itemgetter
from heroIconLinks import heroUrl
import timeConvert, heroList

dpsTimes = []
tankTimes = []
supportTimes = []

response = requests.get('https://ow-api.com/v1/stats/pc/us/SkeeCoops-1827/complete')
profile = response.json()

#GETTING TOP HEROES OF THE USER 
def getTopHeroes():
    return profile['competitiveStats']['topHeroes']
    
#DPS ------------------------------------------------------------------------------------------------------------------------------------------------------

def getTopDPS():
    heroTimeSeconds = []
    for i in heroList.dpsList:
        try:
            if(len(profile['competitiveStats']['topHeroes'][i]['timePlayed']) > 5 ):
                dpsTimes.append(profile['competitiveStats']['topHeroes'][i]['timePlayed'])
            else:
                dpsTimes.append("00:" + profile['competitiveStats']['topHeroes'][i]['timePlayed'])

        except KeyError:
            dpsTimes.append("00:00:00")

    #Making the hero time in seconds list here:
    for i in range(0, len(dpsTimes)):
        heroTimeSeconds.append(int(timeConvert.totalSeconds(dpsTimes[i])))

    #Making a list of lists 
    heroNameAndSeconds = list(zip(heroList.dpsList, heroTimeSeconds))

    #new list called output that is sorted by the time list.
    output = sorted(heroNameAndSeconds, key= itemgetter(1), reverse=True)

    #2D ARRAY HAS BECOME SORTED
    return output 

    
def getTopTanks():
    heroTimeSeconds = []
    for i in heroList.tankList:
        try:
            if(len(profile['competitiveStats']['topHeroes'][i]['timePlayed']) > 5 ):
                tankTimes.append(profile['competitiveStats']['topHeroes'][i]['timePlayed'])
            else:
                tankTimes.append("00:" + profile['competitiveStats']['topHeroes'][i]['timePlayed'])

        except KeyError:
            tankTimes.append("00:00:00")

    #Making the hero time in seconds list here:
    for i in range(0, len(tankTimes)):
        heroTimeSeconds.append(int(timeConvert.totalSeconds(tankTimes[i])))

    #Making a list of lists 
    heroNameAndSeconds = list(zip(heroList.tankList, heroTimeSeconds))

    #new list called output that is sorted by the time list.
    output = sorted(heroNameAndSeconds, key= itemgetter(1), reverse=True)

    #2D ARRAY HAS BECOME SORTED
    return output 

def getTopSupports():
    heroTimeSeconds = []
    for i in heroList.supportList:
        try:
            if(len(profile['competitiveStats']['topHeroes'][i]['timePlayed']) > 5 ):
                supportTimes.append(profile['competitiveStats']['topHeroes'][i]['timePlayed'])
            else:
                supportTimes.append("00:" + profile['competitiveStats']['topHeroes'][i]['timePlayed'])

        except KeyError:
            supportTimes.append("00:00:00")

    #Making the hero time in seconds list here:
    for i in range(0, len(supportTimes)):
        heroTimeSeconds.append(int(timeConvert(supportTimes[i])))

    #Making a list of lists 
    heroNameAndSeconds = list(zip(heroList.supportList, heroTimeSeconds))

    #new list called output that is sorted by the time list.
    output = sorted(heroNameAndSeconds, key= itemgetter(1), reverse=True)

    #2D ARRAY HAS BECOME SORTED
    return output 

def getTop3DPS():
    sortedDPS = getTopDPS()

    #for i in range(0, 2):
    #    top3DPS.append(str(i+1) +") "+ str(sortedDPS[i][0].capitalize()))
    
    top3DPSMsg = ""
    for i in range(0, 3):
        top3DPSMsg = top3DPSMsg + str(i+1) + ") "+ str(sortedDPS[i][0].capitalize()) + "\n"


    return top3DPSMsg

def getTop3Tanks():
    sortedTanks = getTopTanks()

    #for i in range(0, 2):
    #    top3Tanks.append(sortedTanks[i])

    top3TankMsg = ""
    for i in range(0, 3):
        top3TankMsg = top3TankMsg + str(i+1) + ") "+ str(sortedTanks[i][0].capitalize()) + "\n"

    return top3TankMsg

#returns a string with the top 3 in the role with the new lines in 
def getTop3Support():
    sortedSupports = getTopSupports()


    #for i in range(0, 2):
    #    top3Support.append(sortedSupport[i])

    top3SupportsMsg = ""
    for i in range(0, 3):
        top3SupportsMsg = top3SupportsMsg + str(i+1) + ") "+ str(sortedSupports[i][0].capitalize()) + "\n"

    return top3SupportsMsg






