import discord
from discord.ext import commands

TOKEN = ""

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def loop(ctx, num: int):
    for i in range(num, 0, -1):
        await ctx.send(i)

bot.run(TOKEN)
