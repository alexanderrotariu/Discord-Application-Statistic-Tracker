import profile

#WHAT IS THE FUCKING POINT OF THIS FILE I DONT REMEMBER WHY I WROTE THIS

#ONLY GOD KNOWS WHY THIS FILE EXISTS



def getAvgStats():
    elimsAvg = profile.getAvgElims()
    avgDeaths = profile.getAvgDeaths()
    finalBlowsAvg = profile.getAvgFinalBlows()
    healingDoneAvg = profile.getAvgHealingDone()
    dmgDoneAvg = profile.getAvgDmgDone()

    avgStats = [elimsAvg, avgDeaths, finalBlowsAvg, healingDoneAvg, dmgDoneAvg]
    return avgStats





