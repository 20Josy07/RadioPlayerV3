from pyrogram import Client
from config import Config

REPLY_MESSAGE=Config.REPLY_MESSAGE

if REPLY_MESSAGE is not None:
    USER = Client(
        Config.SESSION,  # This is the long session string
        api_id=Config.API_ID,
        api_hash=Config.API_HASH
        plugins=dict(root="plugins.userbot")
        )
else:
    USER = Client(
        Config.SESSION,
        Config.API_ID,
        Config.API_HASH
        )
USER.start()
