import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import random
import json
from pathlib import Path
import webserver
import os
import re

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

status_cycle = [
    discord.CustomActivity(name="👩‍🦽 !help for commands"),
    discord.CustomActivity(name="🧧 Join Kiln-Heart Institute now!"),
    discord.CustomActivity(name="🎧 listening to Xinyi B"),
    discord.CustomActivity(name="😒 plotting Izumi's downfall"),
    discord.CustomActivity(name="👹 arguing with Keiko"),
    discord.CustomActivity(name="🎶 listening to Regular"),
    discord.CustomActivity(name="😭 got scolded by Madam Li"),
    discord.CustomActivity(name="👹 squaring up with Yunxing"),
    discord.CustomActivity(name="🎉 HappYyYyYyy BirthdayYYyY"),
    discord.CustomActivity(name="🤬 getting arrested by Keiko"),
    discord.CustomActivity(name="🤑 DADDY MONEY PWEASE"),
    discord.CustomActivity(name="😨 getting dissed by Liuying"),
    discord.CustomActivity(name="😜 loosing the strings"),
    discord.CustomActivity(name="😭 got scolded by Madam Gu"),
]

@tasks.loop(seconds=10)
async def rotate_status():
    next_status = random.choice(status_cycle)
    await bot.change_presence(status=discord.Status.online, activity=next_status)

@bot.event
async def on_ready():
    if not rotate_status.is_running():
        rotate_status.start()
    print("You feelin me? Tang Jingmei in the building PERIODT")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()

    if "eliminated" in content:
        await message.channel.send(f"HOY ANONG ELIMINATED IKAW HA {message.author.mention}!")
    
    if "welcome back" in content:
        await message.channel.send(f"THE CHAMPION IS RETURN")
    
    if "palakpakan" in content:
        await message.channel.send(f"PALAKPAKAN ANG PUTA NG INA")

    # match only hard/harde/harder (not too short prefixes)
    if re.search(r"hard(?:e(?:r)?)?", content):
        harder_response = (
            f" {message.author.mention} 🤨 📸 Caught you in 8K UHD surround sound 32 Gigs ram, HDR GEFORCE RTX, "
            "TI-80 texas insturments, Triple A duracell battery ultrapower100 Cargador Compatible iPhone 1A 5 W 1400 + "
            "Cable 100% 1 Metro Blanco Compatible iPhone 5 5 C 5S 6 SE 6S 7 8 X XR XS XS MAX GoPro hero 1 2 terrabyte "
            "xbox series x Dell UltraSharp 49 Curved Monitor - U4919DW Sony HDC-3300R 2/3\" CCD HD Super Motion Color Camera, "
            "1080p Resolution Toshiba EM131A5C-SS Microwave Oven with Smart Sensor, Easy Clean Interior, ECO Mode and "
            "Sound On/Off, 1.2 Cu. ft, Stainless Steel HP LaserJet Pro M404n Monochrome Laser Printer with Built-in Ethernet "
            "(W1A52A) GE Voluson E10 Ultrasound Machine LG 23 Cu. Ft. Smart Wi-Fi Enabled InstaView Door-in-Door Counter-Depth "
            "Refrigerator with Craft Ice Maker GFW850SPNRS GE 28\" Front Load Steam Washer 5.0 Cu. Ft. with SmartDispense, "
            "WiFi, OdorBlock and Sanitize and Allergen - Royal Sapphire Kohler K-3589 Cimarron Comfort Height Two-Piece "
            "Elongated 1.6 GPF Toilet with AquaPiston Flush Technology"
        )
        await message.channel.send(harder_response)

    # duplicate rule for faster/faste/fast
    if re.search(r"fast(?:e(?:r)?)?", content):
        faster_response = (
            f" {message.author.mention} 🤨 📸 Caught you in 8K UHD surround sound 32 Gigs ram, HDR GEFORCE RTX, "
            "TI-80 texas insturments, Triple A duracell battery ultrapower100 Cargador Compatible iPhone 1A 5 W 1400 + "
            "Cable 100% 1 Metro Blanco Compatible iPhone 5 5 C 5S 6 SE 6S 7 8 X XR XS XS MAX GoPro hero 1 2 terrabyte "
            "xbox series x Dell UltraSharp 49 Curved Monitor - U4919DW Sony HDC-3300R 2/3\" CCD HD Super Motion Color Camera, "
            "1080p Resolution Toshiba EM131A5C-SS Microwave Oven with Smart Sensor, Easy Clean Interior, ECO Mode and "
            "Sound On/Off, 1.2 Cu. ft, Stainless Steel HP LaserJet Pro M404n Monochrome Laser Printer with Built-in Ethernet "
            "(W1A52A) GE Voluson E10 Ultrasound Machine LG 23 Cu. Ft. Smart Wi-Fi Enabled InstaView Door-in-Door Counter-Depth "
            "Refrigerator with Craft Ice Maker GFW850SPNRS GE 28\" Front Load Steam Washer 5.0 Cu. Ft. with SmartDispense, "
            "WiFi, OdorBlock and Sanitize and Allergen - Royal Sapphire Kohler K-3589 Cimarron Comfort Height Two-Piece "
            "Elongated 1.6 GPF Toilet with AquaPiston Flush Technology"
        )
        await message.channel.send(faster_response)

    await bot.process_commands(message)

#!hello
@bot.command()
async def hello(ctx):
    file_name = random.choice(['hello.png', 'hello2.png'])
    await ctx.send(file=discord.File(file_name))

#!ultrawide
@bot.command()
async def ultrawide(ctx):
    file_name = random.choice(['ultrawide.png', 'ultrawide2.png'])
    await ctx.send(file=discord.File(file_name))

#!kiss
@bot.command()
async def kiss(ctx):
    file_name = random.choice(['kiss.png', 'kiss2.png'])
    await ctx.send(file=discord.File(file_name))

#!good
@bot.command()
async def good(ctx):
    await ctx.send(file=discord.File('good.png'))

#!amazing
@bot.command()
async def amazing(ctx):
    await ctx.send(file=discord.File('amazing.png'))

#!chio
@bot.command()
async def chio(ctx):
    await ctx.send(file=discord.File('chio.png'))

#!baddie
@bot.command()
async def baddie(ctx):
    file_name = random.choice(['baddie.png', 'baddie2.png', 'baddie3.png'])
    await ctx.send(file=discord.File(file_name))

#!pettyassbih
@bot.command()
async def pettyassbih(ctx):
    await ctx.send(file=discord.File('pettyassbih.png'))

#!hehe
@bot.command()
async def hehe(ctx):
    await ctx.send(file=discord.File('hehe.png'))

#!absolute
@bot.command()
async def absolute(ctx):
    await ctx.send(file=discord.File('absolute.png'))

#!vape
@bot.command()
async def vape(ctx):
    file_name = random.choice(['vape.png', 'vape2.png'])
    await ctx.send(file=discord.File(file_name))

#!cheng
@bot.command()
async def cheng(ctx):
    await ctx.send(file=discord.File('cheng.png'))

#!huimei
@bot.command()
async def huimei(ctx):
    await ctx.send(file=discord.File('huimei.png'))

#!rabbit
@bot.command()
async def rabbit(ctx):
    await ctx.send(file=discord.File('rabbit.png'))

#!queen
@bot.command()
async def queen(ctx):
    await ctx.send(file=discord.File('queen.png'))

#!ouch
@bot.command()
async def ouch(ctx):
    await ctx.send(file=discord.File('ouch.png'))

#!talagaba
@bot.command()
async def talagaba(ctx):
    await ctx.send(file=discord.File('talagaba.png'))

#!cinema
@bot.command()
async def cinema(ctx):
    await ctx.send(file=discord.File('cinema.png'))

#!draw
@bot.command()
async def draw(ctx):
    await ctx.send(file=discord.File('draw.png'))

#!keikob
@bot.command()
async def keikob(ctx):
    await ctx.send(file=discord.File('keikob.png'))

#!xinyi
@bot.command()
async def xinyi(ctx):
    await ctx.send(file=discord.File('xinyi.png'))

#!izumi
@bot.command()
async def izumi(ctx):
    file_name = random.choice(['izumi.png', 'izumi2.png'])
    await ctx.send(file=discord.File(file_name))

#!y
@bot.command()
async def y(ctx):
    await ctx.send(file=discord.File('y.png'))

#!yuri
@bot.command()
async def yuri(ctx):
    await ctx.send(file=discord.File('yuri.png'))

#!shu
@bot.command()
async def shu(ctx):
    await ctx.send(file=discord.File('shu.png'))

#!commence
@bot.command()
async def commence(ctx):
    file_name = random.choice(['commence.png', 'commence2.png'])
    await ctx.send(file=discord.File(file_name))

#!king
@bot.command()
async def king(ctx):
    await ctx.send(file=discord.File('king.png'))

#!eunji
@bot.command()
async def eunji(ctx):
    await ctx.send(file=discord.File('eunji.png'))

#!opps
@bot.command()
async def opps(ctx):
    file_name = random.choice(['opps.png', 'opps2.png'])
    await ctx.send(file=discord.File(file_name))

#!come
@bot.command()
async def come(ctx):
    await ctx.send(file=discord.File('come.png'))

#!cyn
@bot.command()
async def cyn(ctx):
    await ctx.send(file=discord.File('cyn.png'))

#!kabayot
@bot.command()
async def kabayot(ctx):
    await ctx.send(file=discord.File('kabayot.png'))

#!stinky
@bot.command()
async def stinky(ctx):
    await ctx.send(file=discord.File('stinky.png'))

#!focused
@bot.command()
async def focused(ctx):
    await ctx.send(file=discord.File('focused.png'))

@bot.command(name="help")
async def help_cmd(ctx):
    commands_text = (
        "**Image commands**:\n"
        "`!hello`     `!ultrawide`  `!kiss`      `!good`\n"
        "`!amazing`   `!chio`       `!baddie`    `!pettyassbih`\n"
        "`!hehe`      `!absolute`   `!vape`      `!queen`\n"
        "`!cheng`     `!huimei`     `!rabbit`    `!kabayot`\n"
        "`!ouch`      `!talagaba`   `!cinema`    `!draw`\n"
        "`!keikob`    `!xinyi`      `!izumi`     `!y`\n"
        "`!yuri`      `!shu`        `!commence`  `!king`\n"
        "`!eunji`     `!opps`       `!come`      `!cyn`\n"
        "`!stinky`    `!focused`    \n"
        "\n\n"
    )
    await ctx.send(commands_text)

webserver.keep_alive()
bot.run(token)