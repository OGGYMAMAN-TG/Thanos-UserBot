# Thanks to @D3_krish
# Porting in THANOSBOT BY REBEL75
# CREDITS REBEL75 @D3_krish
import asyncio
import random
from telethon import events, version
from userbot import ALIVE_NAME, REBELversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "THANOSBOT"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

REBEL = bot.uid

edit_time = 6
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/96c7031243c9bbaab31eb.jpg"
file2 = "https://telegra.ph/file/97012cc8b32a2744c50b3.jpg"
file3 = "https://telegra.ph/file/ba5bc78cdf6fbc65e1cce.jpg"
file4 = "https://telegra.ph/file/4c1b9c5b5856109533635.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "  __**🔥🔥ＴＨΛＮ♢Ｓ  ＩＳ  ΛＬＩＶΣ🔥🔥**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"                💞BOSS💞\n      **『😈[{DEFAULTUSER}](tg://user?id={THANOS})😈』**\n\n"
)
pm_caption += f"╭────────────\n"
pm_caption += f"┣•➳➠ `ＴΞＬΣＴＨ♢Ｎ:` `{version.__version__}` \n"
pm_caption += f"┣•➳➠ `ＴＨΛＮ♢Ｓ:`    [ＲΞＰ♢](https://github.com/thanosuser/ThanosBot)\n"
pm_caption += f"┣•➳➠ `ＣＨΛＮＮΞＬ:` [Ｊ♢ＩＮ](https://t.me/thanos_userbots)\n"
pm_caption += f"┣•➳➠ `♢ＷＮΣＲ:` [ＲＩＳＨΛＢＨ](https://t.me/MAFIARISHABH)\n"
pm_caption += f"┣•➳➠ `ＳＵＰＰ♢ＲＴ:` [Ｊ♢ＩＮ](https://t.me/thanosbot_chats)\n"
pm_caption += f"╰────────────\n"


# @command(outgoing=True, pattern="^.thanos$")
@bot.on(admin_cmd(outgoing=True, pattern="thanos$"))
@bot.on(sudo_cmd(pattern="thanos$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    

    """ For .thanos command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add_command(
  "rebel", None, "To check am i alive with your favorite alive pic"
).add()
