import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import database  # Import the database module

# Load environment variables
load_dotenv()

# Get the TOKEN
TOKEN = os.getenv('TOKEN') 

intents = discord.Intents.default()
intents.members = True 
intents.guilds = True
intents.messages = True
intents.reactions = True 
intents.message_content = True

# Initialize the bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Initialize the database
database.initialize()

ROLE_ID = 1234 # Here is your roles ID

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@commands.has_role(ROLE_ID)
@bot.command()
async def test(ctx):
    await ctx.send("Bot is working.")

# Warn command (stores a warning in the database)
@commands.has_role(ROLE_ID)
@bot.command()
async def warn(ctx, member: discord.Member, *, reason=None):
    if reason is None:
        await ctx.send("Please provide a reason for the warning.")
        return
    database.add_warning(member.id, ctx.guild.id, reason)
    await ctx.send(f"{member.mention} has been warned for: {reason}")
    
# Warnings command (shows all warnings for a user)
@commands.has_role(ROLE_ID)
@bot.command()
async def warnings(ctx, member: discord.Member):
    # Get warnings for the user from the database
    results = database.get_warnings(member.id, ctx.guild.id)
    if not results:
        await ctx.send(f"{member.mention} has no warnings.")
    else:
        warning_list = "\n".join([f"{idx + 1}. {row[0]}" for idx, row in enumerate(results)])
        await ctx.send(f"{member.mention} has the following warnings:\n{warning_list}")

# Clear Warnings command (deletes all warnings for a user)
@commands.has_role(ROLE_ID)
@bot.command()
async def clearwarnings(ctx, member: discord.Member):
    # Clear all warnings for the user in the database
    database.clear_warnings(member.id, ctx.guild.id)
    await ctx.send(f"All warnings for {member.mention} have been cleared!")

# Clean up SQLite when the bot closes
@bot.event
async def on_disconnect():
    database.close_connection()

# Run the bot
bot.run(TOKEN)
