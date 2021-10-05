

import requests
from modules.play import call_py
from pyrogram import Client as Bot
from pyrogram import Client, idle
from AxeVcPlayer.config import API_HASH, API_ID, BG_IMAGE, BOT_TOKEN
from AxeVcPlayer.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="AxeVcPlayer.modules"),
)

bot.start()
run()
