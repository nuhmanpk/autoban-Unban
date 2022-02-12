import os
from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions



app = Client(
    "ban/unban for 24 Hour",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

@app.on_message(filters.command(["start"]))
async def start(app, Message):
    await Message.reply_text("Hello")


@app.on_message(filters.group & filters.new_chat_members)
async def ban(app,Message):
    chat_id=Message.chat.id
    user_id=Message.from_user.id
    # Kick chat member and automatically and unban after 24h
    await app.ban_chat_member(chat_id, user_id, int(time.time() + 86400))


app.run()





