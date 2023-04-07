import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

STRING = os.environ.get("STRING", "AQBtn4EAazDgWzlZ-KRdkoeB1bAj3SsCS_PsXtoAHzYm1opq4LXEpnLsnMDI1Pa3iSvgVTgkNi-Jxa5NWz3y286Ub9wtxwbsG9HZ--8D3fjsBFfAmb_86t2EWhD8EoGQr30w1x5QZPgUJk91dOm6zGnStW1B6GqrpPWAUEY6ChHxgn-LB9U0Kk0qzd51xG1UO8MN2qczsDoV7CdHov_MUM1bGIVqzFxeItI0E_tNwKmFFVMP4UwnxOqVOyAWD3f1Y6nRk6WO3zpQd-YTWDPQ_EAJEXhtPHafb3tn_z-MySsql-UvqEhzavDCkAdPtqJv0hn54mUyF8Y0dBZJ-zDWDqbX8FFuwgAAAAE3HbfHAA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
