# Zed-Thon - ZelZal
# Copyright (C) 2022 Zedthon . All Rights Reserved
#
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/blob/main/LICENSE/>.
# الملــف محمــي بحقــوق النشـــر والملـكيـه
# تخمــط بــدون ذكــر المصــدر ابلــع حســابـك بانـــد
""" 
CC Checker & Generator for SPIDER™ t.me/EE_20
Write file by t.me/WWWL5
hhh o ya beby

"""

import asyncio
import os
import sys
import urllib.request
from datetime import timedelta
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from WWWL5 import WWWL5 

from ..core.managers import edit_or_reply

plugin_category = "البوت"


# code by t.me/WWWL5
@WWWL5.ar_cmd(pattern="os(?:\s|$)([\s\S]*)")
async def song2(event):
    song = event.pattern_match.group(1)
    chat = "@OpenAI_GPT_Chatbot" # code by t.me/WWWL5
    reply_id_ = await reply_id(event)
    zed = await edit_or_reply(event, "**𓅓╎جـارِ البحث عن المطلوب ...**")
    async with event.client.conversation(chat) as conv:
        try:
            gool = "{}".format(song)
            await conv.send_message(gool)
        except YouBlockedUserError:
            await WWWL5(unblock("OpenAI_GPT_Chatbot"))
            gool = "{}".format(song)
            await conv.send_message(gool)
        await asyncio.sleep(10)
        response = await conv.get_response()
        if response.text.startswith("ANTI_SPAM:"):
        	return await zed.edit("**- حاول مجـدداً ولا تستخـدم سبـام ...**")
        if response.text.startswith("RISK:"):
        	return await zed.edit("**- خطـأ :**\n**أعد محاولة فحص هذه البطاقه ...لاحقًا**")
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await zed.delete()


# code by t.me/WWWL5
