import discord
from discord.ext import commands

TOKEN = ""

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def hello(ctx):
    await ctx.send("こんにちは！")

bot.run(TOKEN)
