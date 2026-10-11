# Bot de Discord de FarBeyond

Responde preguntas sobre el mod FarBeyond y conversa con la comunidad de El Hangar de Jeb. Usa Gemini.

**Cuándo responde:** cuando lo mencionan, le contestan a un mensaje suyo, le escriben por DM, o siempre en los canales de `CHAT_CHANNEL_IDS`.

## Puesta en marcha
1. En el [portal de desarrolladores de Discord](https://discord.com/developers/applications): crea la app → **Bot** → activa
   **Message Content Intent** → copia el token. Invítalo (OAuth2 → URL Generator → `bot`) con permiso de ver canales,
   leer historial, enviar mensajes y responder.
2. Clave de Gemini en <https://aistudio.google.com/apikey>.
3. `cp .env.example .env`, rellénalo y ejecuta:
   ```bash
   pip install -r requirements.txt
   python bot.py
   ```
   En un hosting (Railway, Fly.io, VPS...) define esas variables en su panel en vez de usar `.env`.

## Conocimiento del mod
El bot lee al arrancar los `.md` de `conocimiento/` (copia del README, `LEEME_PLAYTEST.md` y `docs/` de `ehdj-rp`).
Cuando el mod cambie, copia de nuevo esos archivos y reinicia el bot.

## Más modelos gratis (respaldo)
Además de Gemini, el bot acepta cualquier API con formato OpenAI (`/chat/completions`): un proxy como
[FreeLLMAPI](https://github.com/tashfeenahmed/freellmapi), Groq, OpenRouter, etc. Define `OPENAI_BASE_URL`, `OPENAI_API_KEY`
y `OPENAI_MODEL` en el `.env`. Si Gemini falla o se queda sin cuota, el bot prueba el siguiente proveedor.
`LLM_PROVIDERS=openai,gemini` cambia el orden.
