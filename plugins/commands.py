from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters


REPO = "**šļø SABKA BAAP :** [GANGSTER](https://t.me/VIKRANT_OP)\n\nš[Group](https://t.me/anokhi_dosti)  &  [Channel](https://t.me/about_riya)   š**"
HOME_TEXT = "š **Hi [{}](tg://user?id={})**,\n\nI'm **ZALA KI MAA KAA RAPIST** \nI Can Play Radio/Stream Music In Channels & Groups 24x7 Nonstop!\n\n**š Happy Streaming š**"
HELP = """**Join @The_HellBot and @Its_Fuckin_Hell to get more help!!

š·ļø **Users Commands**:
\u2022 `/SURU`  -  Reply to an audio to play or add to queue.
\u2022 `/help`  -  Shows help for commands.
\u2022 `/playlist`  -  Shows the playlist.
\u2022 `/current`  -  Shows playing time of current track.
\u2022 `/song song name`  -  Download the song.

š·ļø **Admin Commands**:
\u2022 `/skip x`  -  Skip current or x song. [ x >= 2 ]
\u2022 `/join|okkk`  -  Join voice chat of current group.
\u2022 `/leave`  -  Leave current voice chat.
\u2022 `/vc`  -  Check which VC is joined.
\u2022 `/stop`  -  Stop playing music.
\u2022 `/radio`  -  Start radio stream.
\u2022 `/stopradio`  -  Stop radio stream.
\u2022 `/replay`  -  Play from the beginning.
\u2022 `/clean`  -  Remove unused RAW PCM files.
\u2022 `/pause`  -  Pause playing music.
\u2022 `/resume`  -  Resume playing music.
\u2022 `/mute`  -  Mute the VC Bot.
\u2022 `/unmute`  -  Unmute the VC Bot.
\u2022 `/restart`  -  Restart the bot.
"""


@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('šŗ CHANNEL', url='https://t.me/HYPERS_CHAT_ROOM'),
        InlineKeyboardButton('šļø Group', url='https://t.me/HYPERS_CHAT_ROOM'),
    ],
    [
        InlineKeyboardButton('š land lele', url='xvideos.com'),
        InlineKeyboardButton('š GAND DEGA', url='https://jsjdjsjsjsjs'),
    ],
    [
        InlineKeyboardButton('āļø HELP āļø', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)


@Client.on_message(filters.command("lavadaaa"))
async def repo(client, message):
    await message.reply_text(REPO, disable_web_page_preview=True)


@Client.on_message(filters.command("help"))
async def show_help(client, message):
    await message.reply_text(HELP)
