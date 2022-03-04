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