import discord
from discord.ext import commands
from config import *

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='/', intents=intents)

cogs = ['commands']
for cog in cogs:
    try:
        bot.load_extension(f'cogs.{cog}')
    except Exception as e:
        print(f'Failed to load cog {cog}: {e}')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

bot.run(token)
