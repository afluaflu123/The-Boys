import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, User, ChatJoinRequest
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from info import CHAT_ID, TEXT, APPROVED 


@Client.on_chat_join_request(filters.group | filters.channel & filters.private)
async def approve(client, message: ChatJoinRequest):
        chat=message.chat 
        user=message.from_user 
    except errors.PeerIdInvalid as e:
        print("user isn't start bot(means group)")
    except Exception as err:
        print(str(err))
        await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
        if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))
