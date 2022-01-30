from pyrogram import Client, filters
import time


app = Client(
    "ban/unban for 24 Hour",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

@app.on_message(filters.command(["start"]))
async def start(bot,message):
    await message.reply_text("Hello")


@app.on_message(filters.group & filters.new_chat_members)
async def ban(bot,message):
    chat_id=message.chat.id
    user_id=message.from_user.id
    # Kick chat member and automatically and unban after 24h
    await bot.kick_chat_member(chat_id, user_id, int(time.time() + 86400))


app.run()





