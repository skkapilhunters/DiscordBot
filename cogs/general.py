import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Cog General initialized.")

    @commands.command(name="ping", help="Responds with bot latency.")
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.send(f"🏓 Pong! Latency: **{latency}ms**")

    # Slash Command Example
    @discord.app_commands.command(name="hello", description="Say hello to the bot")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello there! 👋")

async def setup(bot):
    await bot.add_cog(General(bot))
