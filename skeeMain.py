import discord
from dotenv import load_dotenv
import os
import defs
import embeds
import profile

#CREDENTIALS 
load_dotenv('.env')

#FORMATING TO DO:
#ADD USER INPUT FOR THE PLAYER!

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    #WORK ON THIS NEXT SESSION
    #THIS FUNCTION STILL IN DEVELOPMENT
    if message.content.startswith('!setProfile'):
        defs.getUserInput(message.content)

    if message.content.startswith('!name'):
        await message.channel.send(profile.getName())

    if message.content.startswith('!level'):
        embed = embeds.sendLevel()
        await message.channel.send(embed=embed)

    if message.content.startswith('!rank'):
        embed = embeds.sendRank()
        await message.channel.send(embed=embed)

    # -------------------------------------------------------------------------- TOP DPS 
    if message.content.startswith('!topDPS'):
        embed = embeds.sendTopDPS()
        await message.channel.send(embed=embed)
    # -------------------------------------------------------------------------- TOP DPS 
    # -------------------------------------------------------------------------- TOP TANKS 
    if message.content.startswith('!topTanks'):
        embed = embeds.sendTopTanks()
        await message.channel.send(embed=embed)
    # -------------------------------------------------------------------------- TOP TANKS 
    # -------------------------------------------------------------------------- TOP SUPPORTS 
    if message.content.startswith('!topSupports'):
        embed = embeds.sendTopSupports()
        await message.channel.send(embed=embed)
    # -------------------------------------------------------------------------- TOP SUPPORTS 
    #----------------------------------------------------------------------------OVERALL TOP HEROS
    if message.content.startswith('!pf'):
        embed = embeds.sendOverall()
        await message.channel.send(embed=embed)
    #----------------------------------------------------------------------------OVERALL TOP HEROS 
    #----------------------------------------------------------------------------AVERAGE PROFILE STATS QUICK PLAY
    if message.content.startswith('!avgStatsQP'):
        embed = embeds.sendAvgStatsQP()
        await message.channel.send(embed=embed)
    #----------------------------------------------------------------------------AVERAGE PROFILE STATS QUICK PLAY
    if message.content.startswith("!avgStatsComp"):
        embed = embeds.sendAvgStatsComp()
        await message.channel.send(embed=embed)

client.run(os.getenv('TOKEN'))