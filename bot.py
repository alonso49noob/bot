import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from google import genai
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# --- up time robot ---
class KeepAliveHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Bot esta vivo")

    def log_message(self, format, *args):
        return # Silencia visitas web en la consola

def run_web_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), KeepAliveHandler)
    print(f"Servidor de keep-alive corriendo en el puerto {port}")
    server.serve_forever()
# ----------------------

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

@bot.command(name="a")
async def ask_nigga(ctx, *, prompt: str):
    """Responde al comando -a con Gemini 2.5 Flash"""
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

# --- Iniciar el servidor web en paralelo antes de encender el bot ---
web_thread = threading.Thread(target=run_web_server, daemon=True)
web_thread.start()

bot.run(DISCORD_TOKEN)
