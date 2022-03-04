#WILL HANDLE CREATING ALL NEW EMBED
import defs, heroTimes, timeConvert, profile, heroList, heroIconLinks
import heroIconLinks

from discord import Embed

def sendTopDPS():
    embed = Embed(title=profile.getName()+"'s top DPS heroes:", color=0xf04c9e)

    sortedDPS = heroTimes.getTopDPS()

    msg = ""

    for i in range(0, len(heroList.dpsList)):
        msg = msg + str(i+1) + ") "+ str(sortedDPS[i][0].capitalize()) + "\n"
    
    embed.add_field(name="Most played to least played:", value=msg)
    
    topHero = sortedDPS[0][0].capitalize()
    
    hUrl = heroIconLinks.heroUrl[topHero]
    embed.set_thumbnail(url=hUrl)

    return embed

def sendTopTanks():
    embed = Embed(title=profile.getName()+"'s top tank heroes:", color=0xf04c9e)

    sortedTanks = heroTimes.getTopTanks()

    msg = ""

    for i in range(0, len(heroTimes.tankTimes)):
        msg = msg + str(i+1) + ") "+ str(sortedTanks[i][0].capitalize()) + "\n"

    embed.add_field(name="Most played to least played:", value=msg)

    topHero = sortedTanks[0][0].capitalize()
        
    hUrl = heroIconLinks.heroUrl[topHero]
    embed.set_thumbnail(url=hUrl)


    return embed

def sendTopSupports():
    embed = Embed(title=profile.getName()+"'s top support heroes:", color=0xf04c9e)

    sortedSupports = heroTimes.getTopSupports()

    msg = ""

    for i in range(0, len(heroTimes.supportTimes)):
        msg = msg + str(i+1) + ") "+ str(sortedSupports[i][0].capitalize()) + "\n"

    embed.add_field(name="Most played to least played:", value=msg)

    topHero = sortedSupports[0][0].capitalize()

    hUrl = heroIconLinks.heroUrl[topHero]
    embed.set_thumbnail(url=hUrl)

    return embed

#will take top 3 heroes from each role and embed it all together 
#inclue rank and level 
#thumbnail of user icon
def sendOverall():
    top3DPS = heroTimes.getTop3DPS()
    top3Tanks = heroTimes.getTop3Tanks()
    top3Support = heroTimes.getTop3Support()

    #have 9 characters to display

    playerRank = profile.getRank()
    playerLevel = profile.getLevel()
    playerName = profile.getName()

    playerIcon = profile.getUserIcon()
    playerRankIcon = profile.getRankIcon()


    #*, name, value, inline
    embed = Embed(title=playerName+"'s Profile:", color=0xf04c9e)
    embed.add_field(name="Rank: ", value=playerRank, inline=True)
    embed.add_field(name="Level: ", value=playerLevel, inline=True)
    embed.add_field(name= " --------------------------------------------------------------------------- ", value=" \n\u200b ", inline=False)
    embed.add_field(name="Top 3 Tanks: ", value=top3Tanks, inline=True)
    embed.add_field(name="Top 3 DPS: ", value=top3DPS, inline=True)
    embed.add_field(name="Top 3 Supports: ", value=top3Support, inline=True)
    embed.set_thumbnail(url=playerIcon)
    embed.set_image(url=playerRankIcon)
    
    return embed    


# PROFILE EMBEDS ----------------------------------------------------------------------


def sendLevel():
    embed = Embed(title=profile.getName()+"'s Level", color=0xf04c9e)
    embed.add_field(name="Level:", value=profile.getLevel())
    embed.set_thumbnail(url=profile['icon'])

    borderType = profile.getBorder()

    embed.add_field(name= "Border:", value= borderType, inline= True)

    return embed

def sendRank():
    embed = Embed(title=profile.getName()+"'s Rank", color=0xf04c9e)
    embed.add_field(name="Rank:", value=profile.getRank())
    embed.set_thumbnail(url=profile['ratingIcon'])
    
    return embed





