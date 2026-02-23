from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from AloneMusic import app  # Assuming the app instance from AloneMusic
from asyncio import sleep

running_tags = {}  # Active tagging operations
MAX_MSG_LEN = 4000  # Safety margin for Telegram message character limits

def get_reason(message: Message) -> str:
    """
    Retrieve the reason from the command's message, e.g., "/utag hello" -> "hello"
    Supports captions if media is included.
    """
    text = (message.text or message.caption or "").strip()
    if not text:
        return "Grup etiketi"
    parts = text.split(maxsplit=1)
    return parts[1].strip() if len(parts) > 1 else "Grup etiketi"

async def safe_send(client: Client, chat_id: int, text: str):
    """Send message safely, handling flood wait errors."""
    try:
        await client.send_message(chat_id, text, disable_web_page_preview=True)
    except FloodWait as e:
        await sleep(int(getattr(e, "value", 3)))  # Wait before retrying
        await client.send_message(chat_id, text, disable_web_page_preview=True)
    except Exception as e:
        print(f"Error sending message: {e}")

# ====== BULK TAGGING ======
@app.on_message(filters.command(["utag", "mentionall"]) & filters.group)
async def tag_all(client: Client, message: Message):
    chat_id = message.chat.id
    reason = get_reason(message)

    if chat_id in running_tags:
        await safe_send(client, chat_id, "⚠️ Zaten bir etiketleme işlemi devam ediyor.")
        return

    running_tags[chat_id] = True

    members = []
    async for member in client.get_chat_members(chat_id):
        if not member.user.is_bot and member.user.username:
            members.append(member.user)

    await safe_send(client, chat_id, f"🔖 {len(members)} üye etiketleniyor...\n📝 Sebep: {reason}")

    count = 0
    body = ""
    for user in members:
        if user.username:
            body += f"❤️‍🔥 @{user.username}\n"
        else:
            body += f"❤️‍🔥 [‎]({f'tg://user?id={user.id}'})\n"

        count += 1

        # Send in blocks of 5 or if the length exceeds the message limit
        header = f"📝 Sebep: {reason}\n"
        if count % 5 == 0 or len(header) + len(body) > MAX_MSG_LEN:
            if chat_id not in running_tags:
                break
            await safe_send(client, chat_id, header + body)
            body = ""
            await sleep(3)

        if chat_id not in running_tags:
            break

    if body and chat_id in running_tags:
        await safe_send(client, chat_id, f"📝 Sebep: {reason}\n{body}")

    running_tags.pop(chat_id, None)
    await safe_send(client, chat_id, "✅ Etiketleme işlemi tamamlandı.")

# ====== SINGLE TAGGING ======
@app.on_message(filters.command(["tag", "singletag"]) & filters.group)
async def single_tag(client: Client, message: Message):
    chat_id = message.chat.id
    reason = get_reason(message)

    if chat_id in running_tags:
        await safe_send(client, chat_id, "⚠️ Zaten bir etiketleme işlemi devam ediyor.")
        return

    running_tags[chat_id] = True

    members = []
    async for member in client.get_chat_members(chat_id):
        if not member.user.is_bot and (member.user.username or True):
            members.append(member.user)

    await safe_send(client, chat_id, f"🔖 {len(members)} üye tek tek etiketleniyor...\n📝 Sebep: {reason}")

    for user in members:
        if chat_id not in running_tags:
            break

        if user.username:
            text = f"📝 Sebep: {reason}\n❤️‍🔥 @{user.username}"
        else:
            text = f"📝 Sebep: {reason}\n❤️‍🔥 [‎]({f'tg://user?id={user.id}'})"

        await safe_send(client, chat_id, text)
        await sleep(2)

    running_tags.pop(chat_id, None)
    await safe_send(client, chat_id, "✅ Tek tek etiketleme tamamlandı.")

# ====== CANCEL TAGGING ======
@app.on_message(filters.command(["cancel"]) & filters.group)
async def cancel_tag(client: Client, message: Message):
    chat_id = message.chat.id
    if chat_id in running_tags:
        running_tags.pop(chat_id, None)
        await safe_send(client, chat_id, "❌ Etiketleme işlemi iptal edildi.")
    else:
        await safe_send(client, chat_id, "⚠️ Şu anda aktif bir etiketleme işlemi yok.")