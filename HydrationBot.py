#Hydration bot Discord
#https://github.com/riholl

import discord
from discord.ext.commands import Bot
import asyncio
import sys

Token = "NTA5OTY1OTUyMDY3MTc0NDEy.XKe9lg.YkObXpdZwFVM8IR3z2LbWCtBFAc"


client = discord.Client()
client = Bot(command_prefix = '?')


@client.command()
async def drunkhelp():
    help_message = "The first number you will input is how many times you want the command to issue, the 2nd number will be for how long you want notifications"
    await client.say(help_message)


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.command()
async def drunk(frequency, timer):
    counter = 0
    buffer = float(frequency) * 60
    await client.wait_until_ready()
    while not client.is_closed:
        if counter < float(timer):
            drinkwater = "Please drink water or you will end up like F.F. in part 6."
            total_left = "This command will issue " + str(timer) + " times every " + str(frequency) + " minutes."
            await client.say(drinkwater)
            await client.say(total_left)
            await asyncio.sleep(buffer)
            counter = counter + 1


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('----------')
    await client.change_presence(game=discord.Game(name='with my stand'))


client.run(Token)

bot_input = input()
if bot_input == "x":
    sys.exit(0)
