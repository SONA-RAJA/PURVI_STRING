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
        InlineKeyboardButton("♽ 𝖡ᴀᴄᴋ ♽", callback_data="back"),
    ],
]


@Client.on_callback_query(filters.regex("changeToGenMsg"))
async def change_to_gen_msg(bot: Client, query: CallbackQuery):
    await query.message.edit_text(
        text=Sugar,
        reply_markup=InlineKeyboardMarkup(sugarButtons)
    )

@Client.on_callback_query(filters.regex("GenByBot"))
async def GenByBotS(bot: Client, query: CallbackQuery):
    await query.message.edit_text(
        text=Sugar,
        reply_markup=InlineKeyboardMarkup(sugarButtons)
    )

elif query == "generate":
            await callback_query.answer()
            await callback_query.message.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))
        elif query == "ngenerate":
            await callback_query.answer()
            await callback_query.message.reply(ask_ques, reply_markup=InlineKeyboardMarkup(alpha_ques))
        elif query == "pyrogram":
            await callback_query.answer()
            await generate_session(bot, callback_query.message)
        elif query == "pyrogram_bot":
            await callback_query.answer("» ᴛʜᴇ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴇᴅ ᴡɪʟʟ ʙᴇ ᴏғ ᴩʏʀᴏɢʀᴀᴍ ᴠ2.", show_alert=True)
            await generate_session(bot, callback_query.message, is_bot=True)
        elif query == "telethon_bot":
            await callback_query.answer()
            await generate_session(bot, callback_query.message, telethon=True, is_bot=True)
        elif query == "telethon":
            await callback_query.answer()
            await generate_session(bot, callback_query.message, telethon=True)
