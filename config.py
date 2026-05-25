import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "14050586"))
API_HASH = getenv("API_HASH","42a60d9c657b106370c79bb0a8ac560c")

BOT_TOKEN = getenv("BOT_TOKEN")
BOT_ID = getenv("BOT_ID")

OWNER_USERNAME = getenv("OWNER_USERNAME", "RishuCoder")
BOT_USERNAME = getenv("BOT_USERNAME", "AnuuMusic_Bot")
BOT_NAME = getenv("BOT_NAME", "˹𓆩🎧𓆪 ᴀɴᴜᴜ ꭙ ᴍᴜꜱɪᴄ˼ ♪")
ASSUSERNAME = getenv("ASSUSERNAME", "")
BOT_LINK = getenv("BOT_LINK", "https://t.me/AnuuMusic_Bot")

MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority")

YTPROXY_URL = getenv("YTPROXY_URL", 'https://tgapi.xbitcode.com') ## xBit Music Endpoint.
YT_API_KEY = getenv("YT_API_KEY" , "xbit_l36jZXKzzKHEuGjBv54LzVx2xmjx9tnb" ) ## Your API key like: xbit_10000000xx0233 Get from  https://t.me/tgmusic_apibot

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

LOGGER_ID    = int(getenv("LOGGER_ID","-1001992970818"))
CLONE_LOGGER     = LOGGER_ID
CLONE_GC         = int(getenv("CLONE_GC", "-1001992970818"))
OWNER_ID = int(getenv("OWNER_ID", "5738579437"))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/the-matrix9/mclone",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", "")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/PikachuClone")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/PikachuSupports")
GITHUB = getenv("GITHUB", "https://t.me/PikachuSupports")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
PLAYLIST_ID = -1001980154960

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", None)

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# --- Updated Image URLs ---
_IMG_LIST = [
    "https://i.ibb.co/B526Tdn7/x.jpg",
    "https://i.ibb.co/WNM2vdXt/x.jpg",
    "https://i.ibb.co/gZhRJ7tj/x.jpg",
    "https://i.ibb.co/ynjHqNnC/x.jpg",
    "https://i.ibb.co/JWQHrDGm/x.jpg",
    "https://i.ibb.co/TDnf52PB/x.jpg",
    "https://i.ibb.co/nNmrt07t/x.jpg",
    "https://i.ibb.co/KQt6Pdj/x.jpg",
    "https://i.ibb.co/chzkmrnx/x.jpg",
    "https://i.ibb.co/FNcR4HQ/x.jpg",
]
START_IMG_URL = getenv("START_IMG_URL", _IMG_LIST)
HELP_IMG_URL = getenv("HELP_IMG_URL", "https://i.ibb.co/fVBRnNSt/x.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", _IMG_LIST)

PLAYLIST_IMG_URL = getenv("PLAYLIST_IMG_URL", "https://i.ibb.co/fVBRnNSt/x.jpg")
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://i.ibb.co/fVBRnNSt/x.jpg")
TELEGRAM_AUDIO_URL = getenv("TELEGRAM_AUDIO_URL", "https://i.ibb.co/fVBRnNSt/x.jpg")
TELEGRAM_VIDEO_URL = getenv("TELEGRAM_VIDEO_URL", "https://i.ibb.co/fVBRnNSt/x.jpg")
STREAM_IMG_URL = getenv("STREAM_IMG_URL", "https://i.ibb.co/fVBRnNSt/x.jpg")
SOUNCLOUD_IMG_URL = getenv("SOUNCLOUD_IMG_URL", "https://i.ibb.co/fVBRnNSt/x.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://i.ibb.co/fVBRnNSt/x.jpg")
SPOTIFY_ARTIST_IMG_URL = getenv("SPOTIFY_ARTIST_IMG_URL", "https://i.ibb.co/fVBRnNSt/x.jpg")
SPOTIFY_ALBUM_IMG_URL = getenv("SPOTIFY_ALBUM_IMG_URL", "https://i.ibb.co/fVBRnNSt/x.jpg")
SPOTIFY_PLAYLIST_IMG_URL = getenv("SPOTIFY_PLAYLIST_IMG_URL", "https://i.ibb.co/fVBRnNSt/x.jpg")

def time_to_seconds(time):
    return sum(int(x) * 60**i for i, x in enumerate(reversed(str(time).split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - SUPPORT_CHANNEL url must start with https://")

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - SUPPORT_CHAT url must start with https://")

CMBOT = [
    "💞", "🩷", "🩷", "🩷", "🩷", "🩵", "🩵", "🩶", "🩵", "🩶",
    "🩶", "🩷", "🩵", "🩶", "🩷", "🩶", "🩵", "🩷", "🩷", "🩵",
    "🩶", "🩶", "🩵", "🩶", "🩶", "🩷", "🩵", "🩶"
]

EFFECT_ID = [
    5104841245755180586,
    5107584321108051014,
    5104841245755180586,
    5107584321108051014,
    5104841245755180586,
    5107584321108051014,
    5104841245755180586,
    5107584321108051014,
]