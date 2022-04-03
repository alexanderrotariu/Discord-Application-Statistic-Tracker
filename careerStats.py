import profile

def getQpAvgStats():
    elimsAvg = profile.getQpAvgElims()
    avgDeaths = profile.getQpAvgDeaths()
    finalBlowsAvg = profile.getQpAvgFinalBlows()
    healingDoneAvg = profile.getQpAvgHealingDone()
    dmgDoneAvg = profile.getQpAvgDmgDone()

    avgStats = [elimsAvg, avgDeaths, finalBlowsAvg, healingDoneAvg, dmgDoneAvg]
    return avgStats

def getCompAvgStats():
    elimsAvg = profile.getCompAvgElims()
    avgDeaths = profile.getCompAvgDeaths()
    finalBlowsAvg = profile.getCompAvgFinalBlows()
    healingDoneAvg = profile.getCompAvgHealingDone()
    dmgDoneAvg = profile.getCompAvgDmgDone()

    avgStats = [elimsAvg, avgDeaths, finalBlowsAvg, healingDoneAvg, dmgDoneAvg]
    return avgStats





