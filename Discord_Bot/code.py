import discord
import asyncio
import os
import random
import datetime

bot = discord.Client()  #Now initialize a bot of desired functions with events.

@bot.event
async def on_member_join(member):
    if member.id == bot.id:
        return
    channel = discord.utils.get(bot.guilds[0].channels, name ="general")
    response = f"Welcome to Priya's Server, {member.name}."
    await channel.send(response)

@bot.event
async def on_message(message):
    if member.author == bot.user:
        return    
    keywords =["atmanirbhar","workout","diet","yoga","study","code","chai"]
    channel = message.channel
    for keyword in keywords:
        if keyword.lower() in message.content.lower():
            response = f"Did someone say {keyword.lower()}? Drop and give me 10 <@{message}>"
            await channel.send(response)
@bot.event
async def pushup_reminder():
    while(True):
        await bot.wait_until_ready()
        online_members=[]
        for member in bot.get_all_members():
            if member.status!= discord.Status.offline and member.id !=bot.user.id:
                online_members.append(member.id)
        if len(online_members) > 0:
            user = random.choice(online_members)
            current_time = int(datetime.datetime.now().strftime("%I"))
            channel = discord.utils.get(bot.guilds[0].channels, name ="general")
            message = f"It's {current_time} o' clock! Time to study<@{user}>!"
        await channel.send(message)
        await asyncio.sleep(3600)

bot.loop.create_task()
token= os.getenv(key.default)
bot.run(token)
