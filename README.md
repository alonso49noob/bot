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

## Varios proveedores (respaldos)
El bot prueba los proveedores en el orden de `LLM_PROVIDERS` y usa la primera respuesta válida. Gemini va con `GEMINI_API_KEY`.
Cualquier servicio con formato OpenAI (`/chat/completions`: Groq, OpenRouter, un proxy como
[FreeLLMAPI](https://github.com/tashfeenahmed/freellmapi)...) se añade con tres variables `NOMBRE_BASE_URL`, `NOMBRE_API_KEY`
y `NOMBRE_MODEL`, y poniendo `nombre` en `LLM_PROVIDERS`. Mira `.env.example`.

- Un proveedor que falla se salta durante 1 minuto (5 si fue por límite de uso, 429), para no retrasar cada mensaje.
- A los que no son Gemini se les manda solo un extracto de la documentación (`OPENAI_CONTEXT_CHARS`), porque las capas gratis limitan los tokens.
- Un `OPENAI_BASE_URL` antiguo sigue funcionando: es el proveedor `openai`.
- La terminal muestra qué proveedor y modelo respondió cada mensaje, y el error exacto cuando uno falla.
