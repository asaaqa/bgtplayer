from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Bikash import app

def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            # text=_["BACK_BUTTON"],
            text="🏠 قناة السورس 🏠",
            url=f"https://t.me/Mlze1bot",
        ),
        InlineKeyboardButton(
            text="المطور",
            url=f"t.me/A_S_A_S_K",
        ),
        InlineKeyboardButton(
            text="اغلاق", callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="الادمن",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="𝐀𝐮𝐭𝐡",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="𝐁𝐥𝐚𝐜𝐤𝐋𝐢𝐬𝐭",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="𝐆𝐛𝐚𝐧",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="𝐄𝐱𝐭𝐫𝐚",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="البنج",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="التشغيل 🔊",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="البث",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="الفيديو",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="البدء",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="𝐒𝐮𝐝𝐨",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    # text=_["BACK_BUTTON"],
                    text="▷ رجوع ◁",
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷ ررجوع◁",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
