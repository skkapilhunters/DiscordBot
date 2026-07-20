import os
import asyncio
from dotenv import load_dotenv
from bot_instance import bot
from page import app

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
PORT = int(os.getenv("PORT", 8080))

async def main():
    if not DISCORD_TOKEN:
        raise ValueError("DISCORD_TOKEN environment variable is missing.")

    # Run Quart web server and Discord bot concurrently
    async with bot:
        await asyncio.gather(
            app.run_task(host="0.0.0.0", port=PORT),
            bot.start(DISCORD_TOKEN)
        )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot shut down gracefully.")
