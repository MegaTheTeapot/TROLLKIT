# Made by Mega145
# github.com/mega145
# original repository:
# github.com/mega145/TROLLKIT

# If you made a fork of this dont delete the above


import os,json
import time
from rich import print
import discord
from discord.ext import commands
from discord.player import FFmpegPCMAudio

f = open('assets/config.json')
f = json.load(f)
prefix = f['prefix']

buglist = "BUGS:\nPlay command doesnt work on the exe file (source file works)\nDiscord [red]PATCHED[/] crash gifs/videos so the command was deleted"
commands_list = "Commands:\n- play - Plays an audio file in your current vc (works with mp4's too)\n- spam - Sends contents of txt file in assets/texts (you can also specify the delay)\n"
#ascii_banner = pyfiglet.figlet_format("TROLLKIT")
ascii_banner = " _____ ____   ___  _     _     _  _____ _____ \n|_   _|  _ \\ / _ \\| |   | |   | |/ /_ _|_   _|\n  | | | |_) | | | | |   | |   | ' / | |  | |  \n  | | |  _ <| |_| | |___| |___| . \\ | |  | |  \n  |_| |_| \\_\\\\___/|_____|_____|_|\\_\\___| |_|  \n                                              \n"
print(buglist)
token = input(f"{ascii_banner}____________________________________________\n\nPlease input your discord token\nIf you dont know how to get it (github.com/mega145/TROLLKIT#how-to-get-my-discord-token)\n>>>")
os.system('cls')


client = commands.Bot(command_prefix=prefix,self_bot=True)

def leave(error=None):
    global ch
    
    print('Ended!')


@client.event
async def on_ready():
    print(f"{ascii_banner}____________________________________________\n\n")
    print(f"{client.user.name}#{client.user.discriminator} Ready to serve (prefix: {prefix})\n")
    print(commands_list)
    print(buglist)


#Play command not working properly in the exe file
#TODO: Make pynacl library import properly in the exe ; Asked stack Overflow (https://stackoverflow.com/questions/67581012/pyinstaller-error-while-trying-to-import-pynacl)
@client.command(pass_context=True,description="Plays an audio file in your current vc (works with mp4's too)")
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
async def spam(ctx,filename,delay=0.7):
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

@client.command(pass_context=True,description='sends a crash gif/video (you can use a custom one in the assets folder)')
async def crash(ctx,filename : str):
    await ctx.message.delete()
    file = discord.File(f'assets/crash/{filename}')
    await ctx.send(file=file)

try:
    client.run(token,bot=False)
except Exception as e:
    input(e)
    exit()