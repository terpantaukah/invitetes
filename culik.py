import os
from pyrogram import Client
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.environ.get("API_ID", "6"))
API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
STRING_SESSION1 = os.environ.get("STRING_SESSION1")
STRING_SESSION2 = os.environ.get("STRING_SESSION2")
STRING_SESSION3 = os.environ.get("STRING_SESSION3")
STRING_SESSION4 = os.environ.get("STRING_SESSION4")
STRING_SESSION5 = os.environ.get("STRING_SESSION5")


bot1 = (
    Client(
        session_name=STRING_SESSION1,
        api_id=API_ID,
        api_hash=API_HASH
    )
    if STRING_SESSION1
    else None
)

bot2 = (
    Client(
        session_name=STRING_SESSION2,
        api_id=API_ID,
        api_hash=API_HASH
    )
    if STRING_SESSION2
    else None
)

bot3 = (
    Client(
        session_name=STRING_SESSION3,
        api_id=API_ID,
        api_hash=API_HASH
    )
    if STRING_SESSION3
    else None
)

bot4 = (
    Client(
        session_name=STRING_SESSION4,
        api_id=API_ID,
        api_hash=API_HASH
    )
    if STRING_SESSION4
    else None
)

bot5 = (
    Client(
        session_name=STRING_SESSION5,
        api_id=API_ID,
        api_hash=API_HASH
    )
    if STRING_SESSION5
    else None
)

bots = [bot for bot in [bot1, bot2, bot3, bot4, bot5] if bot]


print("Selamat datang di pyrogram adder members")

bahan = input("silahkan masukan username group yang mau di culik :\n")
target = input("silahkan masukan username yang mau di tambahkan :\n")


for bot in bots:
    client = get_client(bot)
    client.join_chat(bahan)
    client.join_chat(target)
    try:
        for member in client.iter_chat_members(bahan):
            user = member.user
            tai = ["online", "offline", "recently", "within_week"]
            if user.status in tai:
                try:
                    print(f"menambahkan member ke {target}")
                    client.add_chat_members(target, user.id, forward_limit=100)
                except Exception as e:
                    print(5)
    except:
        pass
