import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Debug print to check if the token is loaded
print(f"Loaded DISCORD_TOKEN: {os.getenv('DISCORD_TOKEN')}")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# List of NSFW keywords to watch for
NSFW_KEYWORDS = [
    'sex', 'porn', 'nude', 'boobs', 'dick', 'fuck', 'shit', 'cunt', 'cock', 'pussy',
    'bitch', 'ass', 'tits', 'clit', 'cum', 'dildo', 'fucking', 'suck', 'blowjob',
    'hardcore', 'erotic', 'orgasm', 'masturbation', 'gangbang', 'threesome', 'lesbian',
    'gay', 'bisexual', 'trans', 'shemale', 'tranny', 'milf', 'hentai', 'yiff','rainbow flag','pride month'
]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name='Watching for NSFW content'))

@tasks.loop(seconds=60)
async def keep_alive():
    print("Bot is staying alive.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()
    for keyword in NSFW_KEYWORDS:
        if keyword in content:
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please avoid NSFW content. Your message has been deleted.")
            break

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Get the bot token from the environment variables
token = os.getenv('DISCORD_TOKEN')
if token is None:
    raise ValueError("No DISCORD_TOKEN found in environment variables.")

bot.run(token)