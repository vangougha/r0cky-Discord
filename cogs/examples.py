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

import os
text = ["https://cdn.discordapp.com/attachments/1097607988140839043/1100412272494530682/kttz6ex44pl91.jpg",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412272804901054/w2qug13hicpa1.jpeg",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412273018818590/pii8zzs1n4ta1.jpeg",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412273018818590/pii8zzs1n4ta1.jpeg",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412273274650694/iyocxtu3doua1.png",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412273874456617/7f61g8gz1vua1.jpeg",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412274176426015/otlb0neqw2va1.jpeg",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412274503594096/t5dtwxch93va1.jpeg",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412274780426250/pbhg6nz9tby91.webp",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412275145310228/8nb6nfv40ly91.webp",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412275606696067/w6c53oz3v3ta1.webp",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412328836599868/uyj5duwxqgva1.png",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412329050505226/tvz094p9njva1.png",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412329247645717/96bbhvhzmjva1.jpeg",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412329432191108/uka0i52xmjva1.jpeg",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412329641902161/6e9j49usmjva1.png",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412329843236954/skrmbu26zgva1.jpeg",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412330149417120/jqk3hzr3zgva1.jpeg",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412330392682516/lt9dzxu7ugva1.jpeg",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412330614988880/msc4f0lptgva1.jpeg",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412330828890203/rsn1gfgktgva1.jpeg",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412403197431838/p8b3w8u7njva1.jpeg",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412403398746122/bhg8j08pmjva1.jpeg",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412403587493938/fmvqe9l2zgva1.jpeg",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412403780440264/x2u0euv7rgva1.png",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412403977560115/gjk626fjchva1.jpeg",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412404250193993/6u7pinsxpgva1.jpeg",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412404472500285/i2skg6aorgva1.jpeg",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412404673818734/zaq5vtxmrgva1.png",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412404879347792/z7qrkmghzgva1.webp",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412405290377227/j1sz127mthqa1.png",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412436785406052/yi3y0djla1ta1.webp",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412437112565830/675m06mq82ta1.webp",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412437494251670/x3qc5c4yqata1.webp",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412437783650404/3smu5oqxqata1.webp",
"https://cdn.discordapp.com/attachments/1097607988140839043/1100412438094032986/8bhjtdg4v3ta1.webp"]
class Examples(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command()
    async def photo(self, ctx, arg=None):
        file_send = random.choice(text)
        await ctx.send(file_send)

async def setup(client):
    await client.add_cog(Examples(client))