from pyrogram import Client
from config import Config

REPLY_MESSAGE = Config.REPLY_MESSAGE

if REPLY_MESSAGE is not None:
    USER = Client(
        "user_session",  # Nombre de sesión corto y válido
        session_string=Config.SESSION,  # Cadena de sesión
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=dict(root="plugins.userbot")
    )
else:
    USER = Client(
        "user_session",  # Nombre de sesión corto y válido
        session_string=Config.SESSION,  # Cadena de sesión
        api_id=Config.API_ID,
        api_hash=Config.API_HASH
    )

USER.start()
