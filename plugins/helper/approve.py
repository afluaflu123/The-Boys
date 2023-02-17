import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, User, ChatJoinRequest
from info import CHAT_ID, TEXT, APPROVED 

gif = [
    'https://telegra.ph/file/a5a2bb456bf3eecdbbb99.mp4',
    'https://telegra.ph/file/03c6e49bea9ce6c908b87.mp4',
    'https://telegra.ph/file/9ebf412f09cd7d2ceaaef.mp4',
    'https://telegra.ph/file/293cc10710e57530404f8.mp4']

@Client.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel) & filters.private)
async def autoapprove(client, message: ChatJoinRequest):
        chat=message.chat 
        user=message.from_user 
        print("user isn't start bot(means group)")    
        await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
        if APPROVED == "on":
        img = random.choice(gif)
        await client.send_video(chat_id=chat.id,img, text=TEXT.format(mention=user.mention, title=chat.title))

