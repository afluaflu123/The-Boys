import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, User, ChatJoinRequest
from info import TEXT, APPROVED 


@Client.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def autoapprove(bot, message: ChatJoinRequest):
    chat=message.chat 
    user=message.from_user 
    print(f"{user.first_name} Joined (Approved)") 
    await bot.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await bot.send_message(message.from_user, text=TEXT.format(mention=user.mention, title=chat.title))
