# bot.py
import os

import discord
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('SERVER')

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    garlicBreadMemes = [
        'https://cdn.discordapp.com/attachments/736215823840051265/962597257331499018/unknown.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962597132748087296/breaking-news-nasa-find-garlic-bread-on-mars-can-new-64697979.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962597129140994068/funny-meme-about-being-a-garlic-bread-expert.jpg'
        'https://cdn.discordapp.com/attachments/736215823840051265/962597087764176906/image0.jpg',
        'https://cdn.discordapp.com/attachments/736215823840051265/962597001713811496/image0.jpg',
        'https://cdn.discordapp.com/attachments/736215823840051265/962596951000490014/unknown.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962596859178807296/1f2i130hrwu61.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962596858729996298/unknown.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962596842682609674/image0.jpg',
        'https://cdn.discordapp.com/attachments/736215823840051265/962596751229988964/unknown.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962596662562402334/image0.jpg',
        'https://cdn.discordapp.com/attachments/736215823840051265/962596518454526042/ascm15w1zed51.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962596462066282546/runners-are-trying-to-steal-and-then-i-get-super-my-garlic-bread-scared-usain-bolt-gbmemes-2o16.jpg',
        'https://cdn.discordapp.com/attachments/736215823840051265/962596339223494656/image0.jpg',
        'https://cdn.discordapp.com/attachments/736215823840051265/962596229018169384/unknown.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962596196231286844/wmool5107dk71.jpg',
        'https://cdn.discordapp.com/attachments/736215823840051265/962596194259980318/32b1a2d68c335a5cad3dd96a5d54b045.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962596098550153216/image0.jpg',
        'https://cdn.discordapp.com/attachments/736215823840051265/962595948855439421/aaab22331cc830279c8bb597719c983c.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962595924603977768/mmm-garlic-bread.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962595846959022170/image0.jpg',
        'https://cdn.discordapp.com/attachments/736215823840051265/962595810577621044/tumblr_oubbdabwCB1wrt8hqo1_500.jpg',
        'https://cdn.discordapp.com/attachments/736215823840051265/962595805557047427/ab450faa171295b2b6249bbc6584651e.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962595715488567326/image0.jpg',
        'https://cdn.discordapp.com/attachments/736215823840051265/962595668269092884/unknown.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962595628158967828/images.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962595523846602762/unknown.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962595475368861696/image0.jpg',
        'https://cdn.discordapp.com/attachments/736215823840051265/962595471187124224/Deo2jh8WkAMWHOD.jpg',
        'https://cdn.discordapp.com/attachments/736215823840051265/962595398369804348/unknown.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962595383345840138/images.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962595223597359155/unknown.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962595197924032542/images.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962595092395343882/b62c05cebd349c26a832e448cb11994e.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962595070920511498/jesusbread.jpg',
        'https://cdn.discordapp.com/attachments/736215823840051265/962595033289195520/image0.jpg',
        'https://cdn.discordapp.com/attachments/736215823840051265/962594777910632449/senatebread.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962594729030217758/03e87ec5da15f0dc2e930986dc4b6e15.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962594641683824690/download.jpg',
        'https://cdn.discordapp.com/attachments/736215823840051265/962594580488945694/ssrcoslim_fit_t_shirtmens10101001c5ca27c6frontsquare_product600x600.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962594304847675402/unknown.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962594163893895248/85038433cc13607c51fdad39c3130e15.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962594137092268102/unknown.png',
        'https://cdn.discordapp.com/attachments/736215823840051265/962594058298089492/image0.jpg'
    ]

    messageFromUser = message.content
    messageFromUserLowerCase = messageFromUser.lower()

    if "garlic" in messageFromUserLowerCase:
        response = random.choice(garlicBreadMemes)
        await message.channel.send(response)
        # await message.channel.send("There are a total of " + str(len(garlicBreadMemes)) + " garlic bread memes")


client.run(TOKEN)