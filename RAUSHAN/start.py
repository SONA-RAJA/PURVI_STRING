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


from RAUSHAN.generate import sugar, Zask_ques


@Client.on_callback_query(filters.regex("changeToGenMsg"))
async def change_to_gen_msg(bot: Client, query: CallbackQuery):
    await query.message.edit_text(
        text=zask_ques,
        reply_markup=InlineKeyboardMarkup(sugar)
    )

