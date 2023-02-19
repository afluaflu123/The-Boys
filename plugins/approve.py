import os
import asyncio
from pyrogram import Client, errors, filters
from pyrogram.types import Message, User, ChatJoinRequest
from database.users_chats_db.py import add_user, add_group
from info import TEXT, APPROVED 

gif = [
    'https://telegra.ph/file/a5a2bb456bf3eecdbbb99.mp4',
    'https://telegra.ph/file/03c6e49bea9ce6c908b87.mp4',
    'https://telegra.ph/file/9ebf412f09cd7d2ceaaef.mp4',
    'https://telegra.ph/file/293cc10710e57530404f8.mp4',
    'https://telegra.ph/file/506898de518534ff68ba0.mp4',
    'https://telegra.ph/file/dae0156e5f48573f016da.mp4',
    'https://telegra.ph/file/3e2871e714f435d173b9e.mp4',
    'https://telegra.ph/file/714982b9fedfa3b4d8d2b.mp4',
    'https://telegra.ph/file/876edfcec678b64eac480.mp4',
    'https://telegra.ph/file/6b1ab5aec5fa81cf40005.mp4',
    'https://telegra.ph/file/b4834b434888de522fa49.mp4'
]

@Client.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(bot, message):
    chat=message.chat 
    user=message.from_user 
    try:
        add_chat(message.chat.id)
        await bot.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
        img = random.choice(gif)
        await bot.send_video(user.id,img, "**Hello {}!\nWelcome To {}\n\n__Powerd By : @SdBotz__**".format(m.from_user.mention, m.chat.title))
        add_user(user.id)
    except errors.PeerIdInvalid as e:
        print("user isn't start bot(means group)")
    except Exception as err:
        print(str(err))
