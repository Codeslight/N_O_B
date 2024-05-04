import discord
from discord.ext import commands
import b

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def f_k(ctx):
    x=0
    if ctx.message.attachments:
        for dosya in ctx.message.attachments:
            await dosya.save(f"./ Süleyman{x}.png")
            await ctx.send(b.t_f(f" Süleyman{x}.png"))
            x+=1
            

    else:
        await ctx.send("Bir dosya yüklemedin.")

bot.run("")