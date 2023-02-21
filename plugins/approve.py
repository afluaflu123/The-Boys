import os
import asyncio, random
from pyrogram import Client, filters, errors
from pyrogram.types import Message, User, ChatJoinRequest 
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
    await client.send_photo(chat_id=message.from_user.id, photo=random.(HACKER) text=TEXT.format(mention=user.mention, title=chat.title))
