import os
import asyncio, random
from pyrogram import Client, filters, errors
from pyrogram.types import Message, User, InlineKeyboardMarkup, InlineKeyboardButton, ChatPermissions
from info import TEXT

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
    await client.send_message(
        chat_id=message.from_user.id,       
        text=TEXT.format(mention=user.mention, title=chat.title),
        reply_markup=InlineKeyboardMarkup(buttons)
        )
