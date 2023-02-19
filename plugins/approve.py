import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, User, ChatJoinRequest
from info import TEXT, APPROVED 

@Client.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(bot, Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await bot.approve_chat_join_request(op.id, kk.id)
        img = random.choice(gif)
        await bot.send_video(kk.id,img, "**Hello {}!\nWelcome To {}\n\n__Powerd By : @SdBotz__**".format(m.from_user.mention, m.chat.title))
        add_user(kk.id)
    except errors.PeerIdInvalid as e:
        print("user isn't start bot(means group)")
    except Exception as err:
        print(str(err))
