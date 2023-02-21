import os
import asyncio
from pyrogram import Client, filters, errors
from pyrogram.types import Message, User, ChatJoinRequest 
from info import TEXT

@Client.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(client, message):
    chat=message.chat 
    user=message.from_user 
    print(f"{user.first_name} Joined (Approved)") 
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    await client.send_message(chat_id=message.from_user.id, text="Hello {}!\nWelcome To {}\n\n__Powerd By : @SdBotz__".format(mention=user.mention, title=chat.title))
