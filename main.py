import discord
from discord.ext import commands, tasks
import os
import logging
import asyncio
from dotenv import load_dotenv
from config import NSFW_KEYWORDS, BOT_CONFIG

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configure Discord intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True

# Initialize bot
bot = commands.Bot(
    command_prefix=BOT_CONFIG['command_prefix'],
    intents=intents,
    help_command=None
)

@bot.event
async def on_ready():
    """Event triggered when bot successfully connects to Discord"""
    if bot.user:
        logger.info(f'Bot logged in as {bot.user.name} (ID: {bot.user.id})')
    logger.info(f'Connected to {len(bot.guilds)} servers')
    
    # Set bot status
    activity = discord.Game(name=BOT_CONFIG['status_message'])
    await bot.change_presence(
        status=discord.Status.online,
        activity=activity
    )
    
    # Start keep-alive task
    if not keep_alive.is_running():
        keep_alive.start()
    
    logger.info('Bot is ready and monitoring for NSFW content')

@bot.event
async def on_guild_join(guild):
    """Event triggered when bot joins a new server"""
    logger.info(f'Joined new server: {guild.name} (ID: {guild.id})')

@bot.event
async def on_guild_remove(guild):
    """Event triggered when bot is removed from a server"""
    logger.info(f'Removed from server: {guild.name} (ID: {guild.id})')

@bot.event
async def on_message(message):
    """Event triggered for every message sent in servers where bot is present"""
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return
    
    # Ignore messages from other bots (optional)
    if message.author.bot:
        return
    
    # Check for NSFW content
    content = message.content.lower()
    detected_keywords = []
    
    for keyword in NSFW_KEYWORDS:
        if keyword.lower() in content:
            detected_keywords.append(keyword)
    
    if detected_keywords:
        try:
            # Delete the message
            await message.delete()
            
            # Send warning message
            warning_msg = (
                f"{message.author.mention}, your message has been removed as it contains "
                f"inappropriate content. Please keep the conversation family-friendly. 🛡️"
            )
            
            warning = await message.channel.send(warning_msg)
            
            # Log the incident
            logger.warning(
                f'NSFW content detected and removed - User: {message.author} '
                f'({message.author.id}), Server: {message.guild.name}, '
                f'Channel: {message.channel.name}, Keywords: {detected_keywords}'
            )
            
            # Auto-delete warning message after 10 seconds to reduce spam
            await asyncio.sleep(10)
            try:
                await warning.delete()
            except discord.NotFound:
                pass  # Message already deleted
                
        except discord.Forbidden:
            logger.error(
                f'Missing permissions to delete message in {message.guild.name} '
                f'#{message.channel.name}'
            )
        except discord.NotFound:
            logger.warning('Message was already deleted')
        except Exception as e:
            logger.error(f'Error processing NSFW content: {e}')
    
    # Process commands
    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    """Global error handler for bot commands"""
    if isinstance(error, commands.CommandNotFound):
        return  # Ignore unknown commands
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You don't have permission to use this command.")
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send("❌ I don't have the required permissions to execute this command.")
    else:
        logger.error(f'Command error: {error}')
        await ctx.send("❌ An error occurred while processing the command.")

@tasks.loop(minutes=5)
async def keep_alive():
    """Periodic task to keep bot active and log status"""
    server_count = len(bot.guilds)
    user_count = 0
    for guild in bot.guilds:
        if guild.member_count is not None:
            user_count += guild.member_count
    logger.info(f'Bot status: Online | Servers: {server_count} | Users: {user_count}')

@keep_alive.before_loop
async def before_keep_alive():
    """Wait for bot to be ready before starting keep-alive task"""
    await bot.wait_until_ready()

# Bot Commands
@bot.command(name='ping')
async def ping_command(ctx):
    """Test command to check if bot is responsive"""
    latency = round(bot.latency * 1000)
    embed = discord.Embed(
        title="🏓 Pong!",
        description=f"Bot latency: {latency}ms",
        color=0x00ff00
    )
    await ctx.send(embed=embed)

@bot.command(name='status')
async def status_command(ctx):
    """Display bot status and statistics"""
    embed = discord.Embed(
        title="🤖 Bot Status",
        color=0x0099ff
    )
    
    # Calculate user count safely
    user_count = 0
    for guild in bot.guilds:
        if guild.member_count is not None:
            user_count += guild.member_count
    
    embed.add_field(name="Servers", value=len(bot.guilds), inline=True)
    embed.add_field(name="Users", value=user_count, inline=True)
    embed.add_field(name="Latency", value=f"{round(bot.latency * 1000)}ms", inline=True)
    embed.add_field(name="Status", value="🟢 Online & Monitoring", inline=False)
    embed.set_footer(text="Keeping your server family-friendly!")
    
    await ctx.send(embed=embed)

@bot.command(name='help')
async def help_command(ctx):
    """Display help information"""
    embed = discord.Embed(
        title="🛡️ NSFW Moderation Bot",
        description="I automatically detect and remove inappropriate content to keep your server family-friendly!",
        color=0xff6b6b
    )
    
    embed.add_field(
        name="🤖 Automatic Features",
        value="• Detects NSFW keywords in messages\n• Automatically deletes inappropriate content\n• Sends warning messages to users",
        inline=False
    )
    
    embed.add_field(
        name="💬 Commands",
        value=f"`{BOT_CONFIG['command_prefix']}ping` - Test bot response\n"
              f"`{BOT_CONFIG['command_prefix']}status` - Show bot statistics\n"
              f"`{BOT_CONFIG['command_prefix']}help` - Show this help message",
        inline=False
    )
    
    embed.add_field(
        name="⚠️ Permissions Required",
        value="• Read Messages\n• Send Messages\n• Manage Messages (to delete inappropriate content)",
        inline=False
    )
    
    embed.set_footer(text="Thank you for keeping your community safe!")
    
    await ctx.send(embed=embed)

def main():
    """Main function to start the bot"""
    # Get Discord token from environment variables
    token = os.getenv('DISCORD_TOKEN')
    
    if not token:
        logger.error("DISCORD_TOKEN not found in environment variables!")
        logger.error("Please set your Discord bot token in the .env file")
        return
    
    logger.info("Starting NSFW Moderation Bot...")
    
    try:
        # Run the bot
        bot.run(token, log_handler=None)  # We handle logging ourselves
    except discord.LoginFailure:
        logger.error("Invalid Discord token provided!")
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
