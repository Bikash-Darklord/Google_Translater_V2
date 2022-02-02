from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "5162777332:AAFNn1Lnp48xeoAOriSNLsUstppBEqkStPc"))
API_ID = int(os.environ.get("API_ID","10585308"))

API_HASH = os.environ.get("API_HASH","c8e7cb62c10c52bfae94ed0e3223103d"))

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "GTBot",
        bot_token=TOKEN,
        api_hash=API_HASH,
        api_id=API_ID,
        plugins=plugins
    )
    app.run()
