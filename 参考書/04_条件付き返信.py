import discord
from discord.ext import commands

TOKEN = ""

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def greeting(ctx, message):
    if message == "Goodmorning":
        await ctx.send("Goodmorning!!")
    elif message == "Hello":
        await ctx.send("Hello!!")
    else:
        await ctx.send("GoodmorningかHelloを入力してください")

bot.run(TOKEN)
