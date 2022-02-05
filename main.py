import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '!')

@bot.event
async def on_ready():
    print("Ready!")

bot.run('OTMwNDA4MTA3ODAzMzA4MDcy.Yd1cEw.8P55CIY1jsxc5c9rzEfYm4BBZ_g')
