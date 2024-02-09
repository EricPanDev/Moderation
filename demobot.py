import httpx
import discord
from datetime import datetime

# Config
BOT_TOKEN = "" # All intents needed, you probably want to set the bot as private
DONT_LOG_STAFF = True # If True, it will ignore and not flag users with ban / admin perms
WEBHOOK = "" # Webhook URL to logging channel

AUTO_FLAG_TIMEOUT = 20   # Time in minutes

Automatic_Action_Config = {
    "harassment":2, # Disabled
    "hate":0.87,
    "hate/threatening":0.87,
    "self-harm":0.95,
    "sexual":0.88,
    "sexual/minors":0.88,
    "violence":2, # Disabled
    "violence/graphic":2 # Disabled
}

Automatic_Log_Config = {
    "harassment":0.85,
    "hate":0.75,
    "hate/threatening":0.75,
    "self-harm":0.75,
    "sexual":0.75,
    "sexual/minors":0.75,
    "violence":0.75,
    "violence/graphic":0.75
}

client = discord.Client(
    intents=discord.Intents.all(),
)

@client.event
async def on_message(message: discord.Message):
    if not message.content: return

    if message.author.guild_permissions.kick_members or message.author.guild_permissions.administrator:
        if DONT_LOG_STAFF: return

    async with httpx.AsyncClient() as wclient:
        res = await wclient.post(
            "http://127.0.0.1:9235/run",
            json = {
                "text": message.content
            }
        ).json()

        for type, num in Automatic_Action_Config.items():
            if res[type] >= num:
                await message.delete()

                duration = datetime.timedelta(seconds=0, minutes=AUTO_FLAG_TIMEOUT, hours=0, days=0)
                await message.author.timeout(duration, reason="Automatic Action: Message Flagged")

                wh = discord.SyncWebhook.from_url(
                    url = WEBHOOK
                )

                wh.send(
                    content=f"From {message.author.display_name} ({message.author.name}, {message.author.id})",
                    embed=discord.Embed(
                        color=discord.Color.yellow(),
                        title=":warning: Automatic Action Taken",
                        description=f"Flag Type: {type}\nMessage: {message.content}\nActions Taken: Delete Message, Timeout (20 Min)"
                    )
                )

                return
            
        for type, num in Automatic_Log_Config.items():
            if res[type] >= num:

                wh = discord.SyncWebhook.from_url(
                    url = WEBHOOK
                )

                wh.send(
                    content=f"From {message.author.display_name} ({message.author.name}, {message.author.id})\n[Jump to message]({message.jump_url})",
                    embed=discord.Embed(
                        color=discord.Color.blurple(),
                        title="Potentially bad message found",
                        description=f"Flag Type: {type}\nMessage: {message.content}\nActions Taken: None"
                    )
                )

                return

client.run(BOT_TOKEN)