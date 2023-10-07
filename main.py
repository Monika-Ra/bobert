import discord
from discord.ext import commands
from keep_alive import keep_alive
import os
import random
import odpovede
import apis

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix="!")


@bot.event
async def on_ready():
  print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  if bot.user.mentioned_in(message):
    if message.content.endswith('?'):
      await message.channel.send(random.choice(odpovede.ano_nie_odpovede))

  await bot.process_commands(message)


@bot.command(name="cingcong")
async def rasist(ctx):
  await ctx.send("rasista!")

@bot.command(name="coinflip", brief="Flips a coin")
async def coinflip(ctx):
  await ctx.send(random.choice(["heads", "tails"]))


@bot.command(name="ping", brief="Replies with Pong!")
async def ping(ctx):
  await ctx.send("Pong!")

@bot.command(name="catfact", brief="Gives random cat fact")
async def catfact(ctx):
  await ctx.send(apis.get_cat_fact())
  
keep_alive()
bot.run(os.environ['BOT_TOKEN'])
