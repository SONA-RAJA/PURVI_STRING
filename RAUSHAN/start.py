from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_photo(
        chat_id=msg.chat.id,
        photo="https://files.catbox.moe/ljyrvb.jpg",
        caption=f"""✦ » ʜᴇʏ  {msg.from_user.mention}  ✤,
✦ » ɪ ᴀᴍ {me2},

✦ » Aɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

✦ » ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴘʏᴛʜᴏɴ ʟɪʙʀᴀʀʏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ.

✦ » ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ: [⎯᪵ ꯭♡゙꯭ 𝗔꯭ ℓ ꯭ᴘ ꯭፝֠֩᷍ʜ ꯭ᴧ ꯭🥂꯭](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="▪ 𝖦ᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ ▪️", callback_data="changeToGenMsg")
                ],
                [
                    InlineKeyboardButton("🔸 𝛅ᴜᴘᴘᴏʀᴛ🔸", url="https://t.me/PURVI_SUPPORT"),
                    InlineKeyboardButton("▫️ 𝖴ᴘᴅᴀᴛᴇs▫️", url="https://t.me/PURVI_UPDATES")
                ],
                [
                    InlineKeyboardButton("🔸 𝛅ᴏᴜʀᴄᴇ 🔸", url="https://github.com/TEAMPURVI/PURVI_STRING"),
                    InlineKeyboardButton("▫️ϻᴜsɪᴄ ʙᴏᴛ▫️", url="https://t.me/PURVI_MUSIC_BOT")
                ]                
            ]
        )
    )


Sugar = "**☞︎︎︎ 𝐖ʜɪᴄʜ ᴍᴇᴛʜᴏᴅ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴs ?**\n\n**<u>❍ 𝐍ᴏᴛᴇ</u> :- Aʟᴡᴀʏs Cʜʜᴏsᴇ Tᴇʟᴇɢʀᴀᴍ Tᴏᴏʟs Mᴇᴛʜᴏᴅ 🍹**\n\n**<u>𖤍 𝐖ᴀʀɴɪɴɢ</u> :- ᴅᴏɴ'ᴛ ᴜsᴇ ʙᴏᴛ ᴍᴇᴛʜᴏᴅ ʙᴇᴄᴀᴜsᴇ ʏᴏᴜʀ ɪᴅ ᴀᴜᴛᴏ ʟᴏɢᴏᴜᴛ 😣**"
sugarButtons = [
    [
        InlineKeyboardButton(text="♽ 𝖦ᴇɴᴇʀᴀᴛᴇ ʙʏ ʙᴏᴛ", callback_data="GenByBot"),
        InlineKeyboardButton(text="♽ 𝖦ᴇɴᴇʀᴀᴛᴇ ʙʏ ᴛᴏᴏʟs", callback_data="GenByTools"),
    ],
    [
        InlineKeyboardButton("♽ 𝖡ᴀᴄᴋ ♽", callback_data="back2home"),
    ],
]



@Client.on_callback_query(filters.regex("back2home"))
async def change_to_gen_msg(bot: Client, query: CallbackQuery):
    me2 = (await bot.get_me()).mention
    
    
    text = (
        f"✦ » ʜᴇʏ {query.from_user.mention},\n"
        f"✦ » ɪ ᴀᴍ {me2},\n\n"
        f"✦ » Aɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, "
        f"ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.\n\n"
        f"✦ » ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴘʏᴛʜᴏɴ ʟɪʙʀᴀʀʏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ.\n\n"
        f"✦ » ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ: "
        f"[⎯᪵ ꯭♡゙꯭ 𝗔꯭ ℓ ꯭ᴘ ꯭፝֠֩᷍ʜ ꯭ᴧ ꯭🥂꯭](tg://user?id={OWNER_ID})!"
    )
    
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="▪ 𝖦ᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ ▪️", callback_data="changeToGenMsg")],
        [
            InlineKeyboardButton("🔸 𝛅ᴜᴘᴘᴏʀᴛ🔸", url="https://t.me/PURVI_SUPPORT"),
            InlineKeyboardButton("▫️ 𝖴ᴘᴅᴀᴛᴇs▫️", url="https://t.me/PURVI_UPDATES")
        ],
        [
            InlineKeyboardButton("🔸 𝛅ᴏᴜʀᴄᴇ 🔸", url="https://github.com/TEAMPURVI/PURVI_STRING"),
            InlineKeyboardButton("▫️ϻᴜsɪᴄ ʙᴏᴛ▫️", url="https://t.me/PURVI_MUSIC_BOT")
        ]
    ])
    
    await query.message.edit_text(
        text=text,
        reply_markup=reply_markup
    )
    
@Client.on_callback_query(filters.regex("changeToGenMsg"))
async def change_to_gen_msg(bot: Client, query: CallbackQuery):
    await query.message.edit_text(
        text=Sugar,
        reply_markup=InlineKeyboardMarkup(sugarButtons)
    )



GenByBotTxt = "**☞︎︎︎ 𝐂ʜᴏᴏsᴇ ᴏɴᴇ ᴛʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ ✔️ **"

GenByBotMarkup = [
    [
        InlineKeyboardButton("▪️𝖯ʏʀᴏɢʀᴀᴍ▪️", callback_data="pyrogram"),
        InlineKeyboardButton("▪️𝖯ʏʀᴏɢʀᴀᴍ ᴠ2▪️", callback_data="pyrogram"),
    ],
    [
        InlineKeyboardButton("🔺𝖳ᴇʟᴇᴛʜᴏɴ🔺", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("🔸𝖯ʏʀᴏɢʀᴀᴍ ʙᴏᴛ🔸", callback_data="pyrogram_bot"),
        InlineKeyboardButton("🔹𝖳ᴇʟᴇᴛʜᴏɴ ʙᴏᴛ🔹", callback_data="telethon_bot"),
    ],
]

@Client.on_callback_query(filters.regex("GenByBot"))
async def GenByBotS(bot: Client, query: CallbackQuery):
    await query.message.edit_text(
        text=GenByBotTxt,
        reply_markup=InlineKeyboardMarkup(GenByBotMarkup)
    )


from pyrogram.types import WebAppInfo



GenByToolsMarkup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "🔺𝖳ᴇʟᴇᴛʜᴏɴ🔺",
                web_app=WebAppInfo(url="https://t.me/KING_STRING_SESSION_BOT/TELETHON")
            ),
            InlineKeyboardButton(
                "🔸𝖯ʏʀᴏɢʀᴀᴍ🔸",
                web_app=WebAppInfo(url="https://t.me/KING_STRING_SESSION_BOT/PYROGRAM")
            ),
        ],
        [
            InlineKeyboardButton(
                "🔅 𝖦ᴇɴᴇʀᴀᴛᴇ ᴀʟʟ ᴛʏᴘᴇ sᴇssɪᴏɴ 🔅",
                web_app=WebAppInfo(url="https://t.me/KING_STRING_SESSION_BOT/STRING_SESSION")
            ),
        ],
    ]
)






@Client.on_callback_query(filters.regex("GenByTools"))
async def GenByToolsss(bot: Client, query: CallbackQuery):
    await query.message.edit_text(
        text=GenByBotTxt,
        reply_markup=GenByToolsMarkup,
    )






gen_button = [
    [
        InlineKeyboardButton(text="🔹𝖦ᴇɴʀᴀᴛᴇ sᴇssɪᴏɴ🔹", callback_data="Zgenerate")
    ]
]




