import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from PritiMusic.utils.decorators.language import language


BOT_LINK = "https://t.me/DikshachatBot"

# ✅ Helper to safely get Random Start Image
def get_random_start_img():
    if config.START_IMG_URL:
        if isinstance(config.START_IMG_URL, list):
            return random.choice(config.START_IMG_URL)
        return config.START_IMG_URL
    return "https://i.ibb.co/cS9VsWRp/file-000000006730720884c2c21b7473f6bb.png" # Fallback Image

@Client.on_message(filters.command("clone"))
@language
async def ping_clone(client: Client, message: Message, _):
    # ✅ Random Photo + Spoiler Logic
    await message.reply_photo(
        photo=get_random_start_img(),
        caption=_["NO_CLONE_MSG"],
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("ɢᴏ ᴀɴᴅ ᴄʟᴏɴᴇ", url=BOT_LINK)]
            ]
        ),
        has_spoiler=True  # ✨ Spoiler Added
    )