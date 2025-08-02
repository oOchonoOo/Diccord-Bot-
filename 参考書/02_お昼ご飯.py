import discord
from discord.ext import commands

TOKEN = ""

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = "!", intents = intents)

@bot.command()
async def lunch(ctx, number):
    lunch = ["ラーメン",
            "カレー",
            "パスタ",
            "おにぎり",
            "焼きそば"
            ]
    index = int(number) % 5
    await ctx.send(lunch[index])

bot.run(TOKEN)
