import xdrlib
import discord 
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
from time import sleep
import os
import pyautogui
from pyscreeze import screenshot 
import subprocess
import nest_asyncio

nest_asyncio.apply()
loop = asyncio.new_event_loop()

class FEU:
  def __init__(self, name, age,):
    self.name = name
    self.age = age
    self.screen = pyautogui.screenshot()
    
p1 = FEU("FEU", 0)

print(p1.name)
print(p1.age)


#def RSDRIVER():
    #if p1.name == "VERT" or p1.age == 110:
        #print("hola 11")
    #RSDRIVER()

def RSMARIO():
    
    intents = discord.Intents.default()
    client = discord.Client(command_prefix='!' , intents = intents)
    
    


    @client.event
    async def on_ready():
        print("We Have logged in as {0.user}" .format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content.startswith("hi"):
            time.sleep(5)
            await message.channel.send("Hello")

        if message.content.startswith("secteur banyuls"):
            time.sleep(5)
            await message.channel.send("clefs : u r s")

        if message.content.startswith("secteur canet"):
            time.sleep(5)
            await message.channel.send("clefs : u r s")

        if message.content.startswith("secteur saleilles"):
            time.sleep(5)
            await message.channel.send("clefs : u r s")

        if message.content.startswith("secteur ille sur tet"):
            time.sleep(5)
            await message.channel.send("clefs : u r s")
        
        if (message.channel.id == 1080191540820975677):
            #new_var = pyautogui.screenshot()
            #new_var.save('11.png')
            time.sleep(5)
            p1 = FEU("VERT", 110)
            print(p1.name)
            time.sleep(5)
        
        if p1.name == "VERT" or p1.age == 110:
            print("Received , waiting on driver")
            p1 = FEU("FEU", 0)

            if (message.channel.id == 1080191540820975677):
                time.sleep(10)
                await message.channel.send(file = discord.File("11.PNG"))

            while(True):
                asyncio.run(on_message())
                pass

    client.run('MTA3NTU1ODUxMDIzMTgxODI5MA.GJ4yXj.op9RlYUkt8wWkfQCcrr19_59pC6GqhA6W4Jjjk')
    
RSMARIO()
#RSDRIVER()
