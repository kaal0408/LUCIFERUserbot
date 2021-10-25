import sys

import userbot
from userbot import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID

from .Config import Config
from .funcs.logger import logging
from .funcs.session import luciferub
from .utils import (
    add_bot_to_logger_group,
    ipchange,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("lucifer")

print(userbot.__copyright__)
print("Licensed under the terms of the " + userbot.__license__)

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("Starting Userbot")
    luciferub.loop.run_until_complete(setup_bot())
    LOGS.info("TG Bot Startup Completed")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()


class luciferCheck:
    def __init__(self):
        self.sucess = True


lucifercheck = luciferCheck()


async def startup_process():
    check = await ipchange()
    if check is not None:
        lucifercheck.sucess = False
        return
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("Yay your lucifer Userbot is officially working.!!!")
    print(
        f"Congratulation, now type {cmdhr}alive to see message if luciferub is live\
        \nIf you need assistance, head to https://t.me/lucifer_Support_group"
    )
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    lucifercheck.sucess = True
    return


luciferub.loop.run_until_complete(startup_process())

if len(sys.argv) not in (1, 3, 4):
    luciferub.disconnect()
elif not lucifercheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        luciferub.run_until_disconnected()
    except ConnectionError:
        pass
