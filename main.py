import os,json
import time
import discord
from discord.ext import commands
from discord.player import FFmpegPCMAudio

f = open('assets/config.json')
f = json.load(f)
prefix = f['prefix']

#ascii_banner = pyfiglet.figlet_format("TROLLKIT")
ascii_banner = " _____ ____   ___  _     _     _  _____ _____ \n|_   _|  _ \\ / _ \\| |   | |   | |/ /_ _|_   _|\n  | | | |_) | | | | |   | |   | ' / | |  | |  \n  | | |  _ <| |_| | |___| |___| . \\ | |  | |  \n  |_| |_| \\_\\\\___/|_____|_____|_|\\_\\___| |_|  \n                                              \n"
token = input(f"{ascii_banner}____________________________________________\n\nPlease input your discord token\n>>>")
os.system('cls')


client = commands.Bot(command_prefix=prefix,self_bot=True)

def leave(error=None):
    global ch
    
    print('Ended!')


@client.event
async def on_ready():
    print(f"{ascii_banner}____________________________________________\n\n")
    print(f"{client.user.name}#{client.user.discriminator} Ready to serve (prefix: {prefix})\n")



@client.command(pass_context=True)
async def play(ctx,media=None):
    global ch

    print(f'Playing {media} on')
    await ctx.message.delete()
    if ctx.author.voice:
        ch = ctx.author.voice.channel
        print(ch)
        voice = await ch.connect()
    if media:
        src = FFmpegPCMAudio(f'assets\media/{media}')
        voice.play(src,after=lambda error: leave())

@client.command(pass_context=True)
async def say(ctx,filename,delay=0.7):
    f = open(f'assets/texts/{filename}')
    await ctx.message.delete()
    print(f'saying contents of {filename}')
    for line in f:
        try:
            await ctx.send(line)
        except:
            pass
        time.sleep(delay)
    print('Ended!')




try:
    client.run(token,bot=False)
except Exception as e:
    input(e)
    exit()