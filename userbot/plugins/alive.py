""".admin Plugin for @XtraTgBot"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, check pinned in @XtraTgBot"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
#     await alive.edit("**`YO BRO JABTAK YE KHEL KHATAM NHI HOTA APUN IDHARICH HAI**\n"
#                      "`Telethon version: 6.9.0\nPython: 3.7.3\n`Database Status: Userbot Working Great!\n\nAlways with you, my master!\n`"
#                      f"`My owner`: {DEFAULTUSER}\n")
    await alive.client.send_message(
            alive.chat_id,
            f"Python: 3.7.3\nEdited by @Techistore\n`Database Status: Databases functioning normally!\n\nAlways with you, my master!\n`My owner`: {DEFAULTUSER}`",
            file="https://i.imgur.com/pU8BE9B.png"
        )
    await alive.delete()
