from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "5224143005:AAGefdyzWsEBx38YRcgMg4Kuk1Pl8KaG0VE")

API_ID = int(os.environ.get("API_ID",10585308)

API_HASH = os.environ.get("API_HASH", "c8e7cb62c10c52bfae94ed0e3223103d")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "GTBot",
        bot_token=("5224143005:AAGefdyzWsEBx38YRcgMg4Kuk1Pl8KaG0VE")
        api_hash=("c8e7cb62c10c52bfae94ed0e3223103d")
        api_id=("10585308")
        plugins=("true")
    )
    app.run("true")
