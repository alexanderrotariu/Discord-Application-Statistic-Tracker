import profile

def getAvgStats():
    elimsAvg = profile.getAvgElims()
    avgDeaths = profile.getAvgDeaths()
    finalBlowsAvg = profile.getAvgFinalBlows()
    healingDoneAvg = profile.getAvgHealingDone()
    dmgDoneAvg = profile.getAvgDmgDone()

    avgStats = [elimsAvg, avgDeaths, finalBlowsAvg, healingDoneAvg, dmgDoneAvg]
    return avgStats





