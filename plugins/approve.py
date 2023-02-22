import os
import asyncio, random
from pyrogram import Client, filters, errors
from pyrogram.types import Message, User, InlineKeyboardMarkup, InlineKeyboardButton
from info import TEXT

PHOTOS = [
         "https://telegra.ph/file/ad57acb6a695288baef12.jpg",
         "https://telegra.ph/file/eaa658c12d3c58834a4cb.jpg",
         "https://telegra.ph/file/98c3e37e883a7438a4ccb.jpg",
         "https://telegra.ph/file/7fe0b9b6d57c2efd04733.jpg",
         "https://telegra.ph/file/6aef82152c52e15a07ffb.jpg",
         "https://telegra.ph/file/73243b0528ed9a2bd526b.jpg"
         ]

@Client.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(client, message):
    chat=message.chat 
    user=message.from_user 
    print(f"{user.first_name} Joined (Approved)") 
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)   
    buttons = [[
                InlineKeyboardButton('🔮 Jᴏɪɴ Mᴏᴠɪᴇs Gʀᴏᴜᴘ 🔮', url='https://t.me/KL_GROUP1')
              ],[       
                InlineKeyboardButton('💥 Jᴏɪɴ Mᴏᴠɪᴇs Cʜᴀɴɴᴇʟ 💥', url='https://t.me/Team_KL')
            ]]
    await client.send_photo(
        chat_id=message.from_user.id,
        photo=random.choice(PHOTOS),
        text=TEXT.format(mention=user.mention, title=chat.title),
        reply_markup=InlineKeyboardMarkup(buttons)
        )
