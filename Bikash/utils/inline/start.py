from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Bikash import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀 ❰ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 ❱ 💥",
                url=f"https://t.me/{BOT_USERNAME}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚙ اعدادات البوت ⚙", callback_data="settings_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="💖 قناتي 💖", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="💖 الدعم 💖", url=config.SUPPORT_GROUP
            )
        ], 
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ❰أضفني الى جروبك❱ ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="💖 مساعده 💖", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="♕ المطور ♕", user_id=OWNER
            )
        ]
     ]
    return buttons
