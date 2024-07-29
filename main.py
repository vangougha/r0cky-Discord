import discord
from discord.ext import commands,tasks
from colorama import Back, Fore, Style
from pathlib import Path
import os
import time
import platform
import random
from colorama import Back, Fore, Style
import time
import platform
import asyncio
from discord import Interaction

client = commands.Bot(
    command_prefix = "*",
    case_insensitive = True,
    intents = discord.Intents.all(),
)

status = ["     https://www.instagram.com/umutyurdugull/", "    https://github.com/vangougha", " https://twitter.com/xanaxhunter", "  https://www.youtube.com/channel/UCAtmH7g6N8uweY4MBzW2wDQ"]

@tasks.loop(seconds=2)
async def change_status():
    stat = random.choice(status)
    activity = discord.Activity(type=discord.ActivityType.playing, name=stat)
    await client.change_presence(activity=activity)

async def load_extensions():
    cog_list = [p.stem for p in Path(".").glob("./cogs/*.py")]
    for cog in cog_list:
        await client.load_extension(f"cogs.{cog}")
        print(f"Loaded {cog}.")



@client.command()
async def wheel(ctx):
    correct_number = random.randint(1, 32)
    attempts = 5

    await ctx.send('**WHEEL OF FORTUNE**\nGuess the correct number between 1 and 32!\nYou have 5 attempts.')

    while attempts > 0:
        try:
            message = await client.wait_for('message', timeout=10.0,
                                            check=lambda message: message.author == ctx.author)
            guess = int(message.content)

            if guess < 1 or guess > 32:
                await ctx.send("Please enter a number between 1 and 32.")
            elif guess == correct_number:
                await ctx.send(f"Congratulations {ctx.author.mention}! You guessed the correct number.")
                return
            elif guess < correct_number:
                await ctx.send("Your guess is too low. Try again.")
                attempts -= 1
            else:
                await ctx.send("Your guess is too high. Try again.")
                attempts -= 1
        except asyncio.TimeoutError:
            await ctx.send("Sorry, time's up! Game over.")
            return

    await ctx.send(f"Sorry {ctx.author.mention}, you ran out of attempts. The correct number was {correct_number}.")


@client.event
async def on_ready():
    await load_extensions()
    prfx = (Back.BLACK + Fore.GREEN + time.strftime("%H:%M:%S UTC ", time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
    synced = await client.tree.sync()
    print(prfx + " Logged in as " + Fore.YELLOW + client.user.name + "#" + client.user.discriminator)
    print(prfx + " Bot ID " + Fore.YELLOW + str(client.user.id))
    print(prfx + " Discord Version " + Fore.YELLOW + discord.__version__)
    print(prfx + " Python Version " + Fore.YELLOW + str(platform.python_version()))
    print(prfx + " Slash Commands Synced, " + Fore.YELLOW + str(len(synced)) + " Commands")
    print(prfx + " Joined Servers " + Fore.YELLOW + str(len(client.guilds)))

    change_status.start()

@client.hybrid_command(name="avatar",description="Returns your avatar")
@discord.app_commands.describe(member="The member whose avatar will be sent")
async def avatar(ctx,member:discord.Member = None):
    if member == None:
        member = ctx.message.author

    await ctx.send(member.display_avatar)
#token = 
# client.run(token)