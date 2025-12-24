import discord
from discord.ext import commands
import Levenshtein  # For similarity check

# ===== CONFIG =====
with open("bot_token.txt") as f:
    TOKEN = f.read().strip()

# Threshold for similarity (0.0 to 1.0)
SIMILARITY_THRESHOLD = 0.85

# Logging channel (create a text channel named 'mod-log' in your server)
LOG_CHANNEL_NAME = "mod-log"

# Official admins: "name": user_id
OFFICIAL_ADMINS = {
    "byte__wizard": 1079431158116384848,  # Replace with real admin IDs
    }

# ===== INTENTS =====
intents = discord.Intents.default()
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ===== HELPER FUNCTIONS =====
def similarity(a, b):
    """Return similarity ratio between 0 and 1"""
    return Levenshtein.ratio(a.lower(), b.lower())

async def log_action(guild, message):
    """Send log message to mod-log channel"""
    channel = discord.utils.get(guild.text_channels, name=LOG_CHANNEL_NAME)
    if channel:
        await channel.send(message)

async def check_impersonation(member):
    """Check if a member is impersonating an admin"""
    for admin_name, admin_id in OFFICIAL_ADMINS.items():
        name_sim = similarity(member.name, admin_name)
        display_sim = similarity(member.display_name, admin_name)

        if (name_sim >= SIMILARITY_THRESHOLD or display_sim >= SIMILARITY_THRESHOLD) and member.id != admin_id:
            try:
                await member.kick(reason="Admin impersonation detected")
                await log_action(
                    member.guild,
                    f"🚨 **Impersonation Blocked**\n"
                    f"User: `{member}`\n"
                    f"Matched Admin: `{admin_name}`\n"
                    f"Similarity: `{max(name_sim, display_sim):.2f}`"
                )
            except Exception as e:
                print(f"Failed to kick {member}: {e}")

# ===== EVENTS =====
@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")
    for guild in bot.guilds:
        print(f"Connected to guild: {guild.name} (ID: {guild.id})")

@bot.event
async def on_member_join(member):
    print(f"🟢 New member joined: {member.name} | ID: {member.id}")
    await check_impersonation(member)

@bot.event
async def on_member_update(before, after):
    if before.display_name != after.display_name:
        print(f"✏️ Name changed: {before.display_name} → {after.display_name}")
        await check_impersonation(after)

with open("bot_token.txt") as f:
    TOKEN = f.read().strip()

bot.run(TOKEN)

