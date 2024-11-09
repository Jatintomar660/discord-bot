import discord
from discord.ext import commands
import asyncio
from utils import logger
from config import CHANNEL_ID, BOT_TOKEN as TOKEN, LEETCODE_API_BASE_URL, SLEEP_TIME
from profile_info_extractor import LeetCodeProfileExtractor

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)

username_list=['aryaman0098','Jatin660']

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    logger.info(f"CHANNEL_ID={CHANNEL_ID}, BOT_TOKEN:{TOKEN}, BASEURL={LEETCODE_API_BASE_URL}")
    
    if not TOKEN:
        logger.error('BOT_TOKEN not found')
        logger.info('Please set env BOT_TOKEN and try again')
        return 
    if not CHANNEL_ID:
        logger.error('CHANNEL_ID not found')
        logger.info('Please set env CHANNEL_ID and try again')
        return

    try:
        channel = await client.fetch_channel(CHANNEL_ID)

        if channel:
            logger.info(f"Found channel: {channel.name}")

            while True:
                for user in username_list:
                    message= LeetCodeProfileExtractor(user).get_stats_message()
                    logger.info(message)
                    await channel.send(message)
                await asyncio.sleep(SLEEP_TIME)  
        else:
            logger.info("Channel not found!")
    except discord.NotFound:
        logger.info("Channel not found!")
    except Exception as e:
        logger.info(f"An error occurred: {e}")



@client.command()
async def add_user(ctx, username: str):
    """Adds a new LeetCode username to the list."""
    if username not in username_list:
        username_list.append(username)
        await ctx.send(f"Added {username} to the list.")
        logger.info(f"Added {username} to the username list.")
    else:
        await ctx.send(f"{username} is already in the list.")
        logger.info(f"{username} is already in the username list.")

@client.command()
async def list_users(ctx):
    """Lists all current LeetCode usernames."""
    await ctx.send("Current LeetCode users: " + ", ".join(username_list))
    logger.info(f"Current users: {', '.join(username_list)}")

client.run(TOKEN)
