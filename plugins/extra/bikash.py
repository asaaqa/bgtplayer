from pyrogram import Client, filters

from Bikash import app
from Bikash.utils.bgtmusic.bk import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command(["bikash","المطور"],prefixes= ["/", "!","","#"])
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def bikash(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/f73af9a4ffe130a83d8d2.jpg",
        caption=f"""🥀 𝐁𝐢𝐤𝐚𝐬𝐡 𝐈𝐬 𝐎𝐰𝐧𝐞𝐫 𝐎𝐟 𝐁𝐠𝐭 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 🌺, 𝐂𝐥𝐢𝐜𝐤 𝐁𝐞𝐥𝐨𝐰 𝐁𝐮𝐭𝐭𝐨𝐧 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐁𝐢𝐤𝐚𝐬𝐡 ♕, 𝐈𝐟 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬 𝐎𝐫 𝐎𝐭𝐡𝐞𝐫𝐬 𝐋𝐢𝐧𝐤, 𝐓𝐡𝐞𝐧 𝐂𝐥𝐢𝐜𝐤 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧 𝐁𝐮𝐭𝐭𝐨𝐧 𝐂𝐥𝐢𝐜𝐤 𝐎𝐭𝐡𝐞𝐫𝐬 𝐁𝐮𝐭𝐭𝐨𝐧 & 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐎𝐫 𝐆𝐫𝐨𝐮𝐩.. 🥀 [𝐘𝐨𝐮𝐭𝐮𝐛𝐞](https://youtube.com/@bikashgadgetstech)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 المطور 🥀", url=f"https://t.me/ASAKIOP")
            ],          
            [
                    InlineKeyboardButton(
                        "🥀 سورس 🥀", url=f"https://t.me/Mlze1bot")
                ],
                [
                    InlineKeyboardButton(
                        "🥀 جروب الدعم 🥀", url=f"https://t.me/ASAAQLIO"
                    ),
                    InlineKeyboardButton(
                        "🥀 قناة السورس 🥀", url=f"https://t.me/Mlze1bot")
                ]
            ]
        ),
    )
