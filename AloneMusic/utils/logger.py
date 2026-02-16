from pyrogram.enums import ParseMode
from AloneMusic import app
from AloneMusic.utils.database import is_on_off
from config import LOGGER_ID, LOG  # LOG ve LOGGER_ID'nin doğru şekilde import edildiğinden emin olun

#############################################
from AloneMusic import app
from AloneMusic.utils.database import (
    get_served_chats,
    is_on_off,
)
from AloneMusic.utils.database import get_active_chats, get_active_video_chats


async def play_logs(message, streamtype):
    chat_id = message.chat.id
    sayı = await app.get_chat_members_count(chat_id)
    toplamgrup = len(await get_served_chats())
    aktifseslisayısı = len(await get_active_chats())
    aktifvideosayısı = len(await get_active_video_chats())

    # LOG değişkeni True ise loglama yapılacak
    if await is_on_off(LOG):  
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Gizli Grup"
        logger_text = f"""

Grup: {message.chat.title} [`{message.chat.id}`]
Üye Sayısı:➜ {sayı}
Kullanıcı: {message.from_user.mention}
Kullanıcı Adı: @{message.from_user.username}
Kullanıcı ID: `{message.from_user.id}`
Grup Linki: {chatusername}
Sorgu: {message.text}

🌹🌹🌹🌹🌹🌹🌹🌹🌹

Toplam Grup Sayısı:➜  {toplamgrup}

Aktif Ses: {aktifseslisayısı}  ❄️  Aktif Video: {aktifvideosayısı}"""
        
        # Eğer grup LOGGER_ID değilse, log gönderilir
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    LOGGER_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
                # Güncel aktif ses sayısını chat başlığına ekleyin
                await app.set_chat_title(LOGGER_ID, f"AKTİF SES - {aktifseslisayısı}")
            except Exception as e:
                # Hata durumunda daha açıklayıcı loglama
                print(f"Hata oluştu: {e}")
        return