import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

ROASTS = [
    "{user}, I've seen loading screens with more personality.",
    "{user}, your Wi-Fi signal has more potential than you do.",
    "{user}, you bring everyone so much joy... when you leave the server.",
    "{user}, even your NPCs are disappointed in you.",
    "{user}, you're proof that character development isn't guaranteed.",
    "{user}, I've seen potatoes with better decision-making skills.",
    "{user}, somehow you managed to make lurking look exhausting.",
    "{user}, the server was peaceful until you showed up.",
    "{user}, your brain has been running on Windows Vista since birth.",
    "{user}, if common sense were currency, you'd be financially ruined.",
]


@bot.event
async def on_ready():
    print(f"🔥 {bot.user} is online!")
    print(f"Connected to {len(bot.guilds)} server(s)")


@bot.command()
async def hello(ctx):
    await ctx.send(
        f"🌙 The Midnight Society has arrived, {ctx.author.mention}."
    )


@bot.command()
async def roast(ctx, member: discord.Member = None):

    if member is None:
        member = ctx.author

    if member.bot:
        await ctx.send(
            "🤖 Nice try. I'm not roasting one of my own kind."
        )
        return

    roast = random.choice(ROASTS).format(
        user=member.mention
    )

    await ctx.send(
        f"🔥 **ROAST OF THE MOMENT** 🔥\n\n{roast}"
    )


@bot.command()
async def roastme(ctx):

    roast = random.choice(ROASTS).format(
        user=ctx.author.mention
    )

    await ctx.send(
        f"💀 **YOU ASKED FOR THIS.**\n\n{roast}"
    )


if not TOKEN:
    print("❌ ERROR: DISCORD_TOKEN was not found in .env")
else:
    bot.run(TOKEN)