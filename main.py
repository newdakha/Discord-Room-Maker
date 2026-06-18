import discord
from discord.ext import commands

# ─── CONFIG ───────────────────────────────────────────────────────────────────
GUILD_ID      = 1362847208977862726
LOBBY_CHANNEL = 1512904102537990365
BOT_TOKEN     = "your-token-here"
# ──────────────────────────────────────────────────────────────────────────────

intents = discord.Intents.default()
intents.members      = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)
temp_channels: dict[int, int] = {}

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    if member.guild.id != GUILD_ID:
        return

    guild = member.guild

    if after.channel and after.channel.id == LOBBY_CHANNEL:
        ch = await guild.create_voice_channel(
            name=f"room {member.name}",
            user_limit=10,
            category=after.channel.category,
        )
        temp_channels[ch.id] = member.id
        try:
            await member.move_to(ch)
        except discord.HTTPException:
            await ch.delete()
            temp_channels.pop(ch.id, None)

    if before.channel and before.channel.id in temp_channels:
        if len(before.channel.members) == 0:
            temp_channels.pop(before.channel.id, None)
            try:
                await before.channel.delete()
            except discord.NotFound:
                pass

bot.run(BOT_TOKEN)
