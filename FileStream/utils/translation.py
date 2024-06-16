from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FileStream.config import Telegram

class LANG(object):

    START_TEXT = """
<b>👋 Hᴇʏ, </b>{}\n 
<b>I'ᴍ Tᴇʟᴇɢʀᴀᴍ Fɪʟᴇs Sᴛʀᴇᴀᴍɪɴɢ Bᴏᴛ As Wᴇʟʟ Dɪʀᴇᴄᴛ Lɪɴᴋs Gᴇɴᴇʀᴀᴛᴏʀ</b>\n
<b>Wᴏʀᴋɪɴɢ Oɴ Cʜᴀɴɴᴇʟs</b>\n
<b>💕 @{}</b>\n"""

    HELP_TEXT = """
<b>- Aᴅᴅ Mᴇ As Aɴ Aᴅᴍɪɴ Oɴ Tʜᴇ Cʜᴀɴɴᴇʟ</b>
<b>- Sᴇɴᴅ Mᴇ Aɴʏ Dᴏᴄᴜᴍᴇɴᴛ Oʀ Mᴇᴅɪᴀ</b>
<b>- I'ʟʟ Pʀᴏᴠɪᴅᴇ Sᴛʀᴇᴀᴍᴀʙʟᴇ Lɪɴᴋ</b>\n
<b>🔞 Aᴅᴜʟᴛ Cᴏɴᴛᴇɴᴛ Sᴛʀɪᴄᴛʟʏ Pʀᴏʜɪʙɪᴛᴇᴅ.</b>\n
<i><b> Rᴇᴘᴏʀᴛ Bᴜɢs Tᴏ <a href='https://telegram.me/Sujan_Bots'>Dᴇᴠᴇʟᴏᴘᴇʀ</a></b></i>"""

    ABOUT_TEXT = """
<b>⚜ Mʏ Nᴀᴍᴇ : {}</b>\n
<b>✦ Vᴇʀsɪᴏɴ : {}</b>
<b>✦ Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://telegram.me/Sujan_BotZ'>Sujan BotZ</a></b>\n
"""

    STREAM_TEXT = """
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <b>{}</b>\n
<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <code>{}</code>\n
"""

    STREAM_TEXT_X = """
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <b>{}</b>\n
<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <code>{}</code>\n
"""


    BAN_TEXT = "__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ.__\n\n**[Cᴏɴᴛᴀᴄᴛ Dᴇᴠᴇʟᴏᴘᴇʀ](tg://user?id={}) Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**"


class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Hᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('Aʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close')
        ],
            [InlineKeyboardButton("📢 Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Hᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('Aʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close'),
        ],
            [InlineKeyboardButton("📢 Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Hᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('Hᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close'),
        ],
            [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
