import os
import asyncio, random
from pyrogram import Client, filters, errors
from pyrogram.types import Message, User, InlineKeyboardMarkup, InlineKeyboardButton
from info import TEXT

HACKER = [
    'https://telegra.ph/file/39e246de80d814ff8bdfd.jpg'
]

@Client.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(client, message):
    chat=message.chat 
    user=message.from_user 
    print(f"{user.first_name} Joined (Approved)") 
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)   
    buttons = [[
                InlineKeyboardButton('⚜ ᴄʜᴀɴɴᴇʟ', url='https://t.me/kerala_rockers'),        
                InlineKeyboardButton('ɢʀᴏᴜᴘ ⚜️', url='https://t.me/+XiEBk6zT8RM5MjI9')
            ],[
                InlineKeyboardButton('🎭 ᴄʜᴀɴɴᴇʟ', url=f'https://t.me/+CeY_RGCtK1g0ZWQ9'),
                InlineKeyboardButton('sʜᴀʀᴇ ᴍᴇ 🤝', url=f'https://t.me/share/url?url=https://t.me/Oru_adaar_Robot')
            ]]
    await client.send_message(
        chat_id=message.from_user.id, 
        text=TEXT.format(mention=user.mention, title=chat.title),
        reply_markup=InlineKeyboardMarkup(buttons)
        )
          
