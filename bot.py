import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from google import genai

# var
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# gemini init
ai_client = genai.Client(api_key=GEMINI_API_KEY)

# bot init
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="-", intents=intents)

@bot.event
async def on_ready():
    print(f"bot inicializado {bot.user.name}")

@bot.command(name="ai")
async def ask_ai(ctx, *, prompt: str):
    """Responde al comando -ai con Gemini 2.5 Flash"""
    # procesando flnsmdfr
    async with ctx.typing():
        try:
            # gemini 2.5 flash
            response = ai_client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            
            # limite de 200 para menos tokens
            if len(response.text) > 200:
                await ctx.send("era escribir algo corto, no la biblia")
            else:
                await ctx.send(response.text)
                
        except Exception as e:
            await ctx.send(f"me jodi, llama a alonso, error: {e}")

bot.run(DISCORD_TOKEN)
