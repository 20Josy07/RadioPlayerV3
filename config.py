import os
import re
import heroku3
from dotenv import load_dotenv
import yt_dlp as youtube_dl
YoutubeDL = youtube_dl.YoutubeDL

load_dotenv()

ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
}
ydl = YoutubeDL(ydl_opts)
links = []
finalurl = ""
STREAM = os.environ.get("STREAM_URL", "http://peridot.streamguys.com:7150/Mirchi")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex, STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl = links[0]
else:
    finalurl = STREAM

class Config:
    # Mendatory Variables
    ADMIN = os.environ.get("AUTH_USERS", "")
    if not ADMIN:
        raise ValueError("AUTH_USERS environment variable is required")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    ADMINS.append(1316963576)

    API_ID = os.environ.get("API_ID", "")
    if not API_ID:
        raise ValueError("API_ID environment variable is required")
    API_ID = int(API_ID)

    API_HASH = os.environ.get("API_HASH", "")
    if not API_HASH:
        raise ValueError("API_HASH environment variable is required")

    CHAT_ID = os.environ.get("CHAT_ID", "")
    if not CHAT_ID:
        raise ValueError("CHAT_ID environment variable is required")
    CHAT_ID = int(CHAT_ID)

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN environment variable is required")

    SESSION = os.environ.get("SESSION_STRING", "")
    if not SESSION:
        raise ValueError("SESSION_STRING environment variable is required")

    # Optional Variables
    LOG_GROUP = os.environ.get("LOG_GROUP", "")
    if LOG_GROUP:
        LOG_GROUP = int(LOG_GROUP)
    else:
        LOG_GROUP = None

    STREAM_URL = finalurl
    ADMIN_ONLY = os.environ.get("ADMIN_ONLY", "False")
    REPLY_MESSAGE = os.environ.get("REPLY_MESSAGE", None)
    if REPLY_MESSAGE:
        REPLY_MESSAGE = REPLY_MESSAGE
    else:
        REPLY_MESSAGE = None
    DELAY = int(os.environ.get("DELAY", 10))
    EDIT_TITLE = os.environ.get("EDIT_TITLE", True)
    if EDIT_TITLE == "False":
        EDIT_TITLE = None
    RADIO_TITLE = os.environ.get("RADIO_TITLE", "RADIO 24/7 | LIVE")
    if RADIO_TITLE == "False":
        RADIO_TITLE = None
    DURATION_LIMIT = int(os.environ.get("MAXIMUM_DURATION", 15))

    # Extra Variables (For Heroku)
    API_KEY = os.environ.get("HEROKU_API_KEY", None)
    APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    if not API_KEY or not APP_NAME:
        HEROKU_APP = None
    else:
        HEROKU_APP = heroku3.from_key(API_KEY).apps()[APP_NAME]

    # Temp DB Variables (Don't Touch)
    msg = {}
    playlist = []
