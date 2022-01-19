from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from userbot.utils import load_module
from userbot import LOAD_PLUG, LOGS, THANOSversion
from pathlib import Path
import asyncio
import telethon.utils

os.system("pip install -U telethon")

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("🔰ՏTᗩᖇT THANOS🔰")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("⚡THANOS ՏTᗩᖇTᑌᑭ ᑕOᗰᑭᒪᗴTᗴᗪ⚡")
    else:
        bot.start()


import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

import userbot._core

print(f"""Hello sir i am THANOS!! THANOS VERSION :- {THANOSversion} YOUR THANOS IS READY! FOR CHECK YOUR BOT WORKING OR NOT PLEASE TYPE (.thanos/.ping) ENJOY YOUR BOT! JOIN FOR MORE FUTURE UPDATES @thanosBot_chats .""")



    try:
        await bot(JoinChannelRequest("@thanos_userbots"))
    except BaseException:
        pass
    try:
        if H2:
            await H2(JoinChannelRequest("@thanos_userbots"))
    except BaseException:
        pass
    try:
        if H3:
            await H3(JoinChannelRequest("@thanos_userbots"))
    except BaseException:
        pass
    try:
        if H4:
            await H4(JoinChannelRequest("@thanos_userbots"))
    except BaseException:
        pass
    try:
        if H5:
            await H5(JoinChannelRequest("@thanos_userbots"))
    except BaseException:
        pass
# Why not come here and chat??
    try:
        await bot(ImportChatInviteRequest('thanosbot_chats'))
    except BaseException:
        pass
    try:
        if H2:
            await H2(ImportChatInviteRequest('thanosbot_chats'))
    except BaseException:
        pass
    try:
        if H3:
            await H3(ImportChatInviteRequest('thanosbot_chats'))
    except BaseException:
        pass
    try:
        if H4:
            await H4(ImportChatInviteRequest('thanosbot_chats'))
    except BaseException:
        pass
    try:
        if H5:
            await H5(ImportChatInviteRequest('thanosbot_chats'))
    except BaseException:
        pass





if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
