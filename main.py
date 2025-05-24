# main.py

import discord
from discord.ext import commands
from translator import translate
from gemini_ai import ask_gemini
from websearch import search_web
from database import log_interaction
import os
from config import ROK_KEYWORDS

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot connected as {bot.user}")

# !ask command for general knowledge questions
@bot.command(name="ask")
async def ask(ctx, *, question):
    translated_q = translate(question, target_lang="en")
    response = ask_gemini(translated_q)
    await ctx.send(response)
    log_interaction(ctx.author.id, question, response)

# !rok command for rok-related questions
@bot.command(name="rok")
async def rok(ctx, *, question):
    translated_q = translate(question, target_lang="en")
    response = search_web(translated_q)
    await ctx.send(response)
    log_interaction(ctx.author.id, question, response, rok=True)

# Bot interaction without commands
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

    if message.content.startswith("!ask") or message.content.startswith("!rok"):
        return

    # Automatic Translation
    translated = translate(message.content, target_lang="en")

    # Detect rok-related and general questions
    if any(keyword in translated.lower() for keyword in ROK_KEYWORDS):
        response = search_web(translated)
        log_interaction(message.author.id, message.content, response, rok=True)
    else:
        response = ask_gemini(translated)
        log_interaction(message.author.id, message.content, response)
    await message.channel.send(response)
