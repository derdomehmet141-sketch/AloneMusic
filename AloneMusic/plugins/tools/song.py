import os
import asyncio
from pyrogram import filters
from pyrogram.types import Message
import yt_dlp
from yt_dlp.utils import DownloadError
import httpx  # HTTP istekleri için

from AloneMusic import app  # @app dekoratörleri için

# ----------------- AYARLAR -----------------

COOKIE_URL = "None"  # GitHub repo URL'si
COOKIE_FILE = "./cookies/example.txt"  # Cookie dosyasının kaydedileceği yol
DOWNLOAD_PATH = "./downloads"  # İndirme yapılacak yol
os.makedirs(DOWNLOAD_PATH, exist_ok=True)  # İndirilen dosyaların kaydedileceği klasör

# ----------------- COOKIE DOSYASINI İNDİRME FONKSİYONU -----------------

async def download_cookie():
    """Cookie dosyasını GitHub repo URL'sinden indir"""
    async with httpx.AsyncClient() as client:
        response = await client.get(COOKIE_URL)
        if response.status_code == 200:
            # Cookie dosyasını kaydet
            with open(COOKIE_FILE, 'wb') as f:
                f.write(response.content)
        else:
            raise Exception(f"Cookie dosyası indirilemedi. HTTP Durumu: {response.status_code}")

# ----------------- ARAMA VE GÖNDERME FONKSİYONU -----------------

async def search_and_send(message: Message, search_type: str = "music"):
    """Arama ve gönderme işlemi"""
    # Cookie dosyasının olup olmadığını kontrol et
    if not os.path.exists(COOKIE_FILE):
        await message.reply_text("❌ Cookie dosyası bulunamadı. Şu anda arama işlemi yapılamaz.")
        return

    # Komut kontrolü
    if len(message.command) < 2:
        await message.reply_text(
            "❌ ʟüᴛꜰᴇɴ ᴀʀᴀᴍᴀ ᴛᴇʀɪᴍɪ ʏᴀᴢıɴ.\n"
            f"Öʀɴ.: /{'bul' if search_type == 'music' else 'vbul'} Taladro"
        )
        return

    query = " ".join(message.command[1:])  # Arama terimi
    status_msg = await message.reply_text(
        f"🔎 `{query}` ɪçɪɴ ᴀʀᴀᴍᴀ ʏᴀᴘıʟıʏᴏʀ ᴠᴇ ɪɴᴅɪʀɪʟɪʏᴏʀ, ʟüᴛꜰᴇɴ ʙᴇᴋʟᴇʏɪɴ..."
    )

    # ----------------- ARAMA -----------------
    ydl_opts_search = {
        "quiet": True,
        "format": "bestaudio/best" if search_type == "music" else "best",
        "noplaylist": True,
        "cookiefile": COOKIE_FILE,  # Cookie dosyasını yükle
        "skip_download": True,
        "extract_flat": True,  # Playlist veya video ekstraktı yapılmaz
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts_search) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)
            entries = info.get("entries", [])

            if not entries:  # Eğer sonuç bulunmazsa
                await status_msg.edit_text("❌ ꜱᴏɴᴜç ʙᴜʟᴜɴᴀᴍᴀᴅı.")
                return

            first_result = entries[0]  # İlk sonucu al
            url = first_result.get("url")
            title = first_result.get("title") or "İsimsiz"

        # ----------------- İNDİRME -----------------
        safe_title = "".join([c if c.isalnum() or c in " _-" else "_" for c in title])
        ext = "mp3" if search_type == "music" else "mp4"
        file_name = os.path.join(DOWNLOAD_PATH, f"{safe_title}.{ext}")

        ydl_opts_download = {
            "format": "bestaudio/best" if search_type == "music" else "best",
            "outtmpl": file_name,
            "cookiefile": COOKIE_FILE,  # Cookie dosyasını kullan
            "quiet": True,
        }

        await status_msg.edit_text(f"⬇️  `{title}` ɪɴᴅɪʀɪʟɪʏᴏʀ...")
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, lambda: yt_dlp.YoutubeDL(ydl_opts_download).download([url]))

        # ----------------- CHAT'E GÖNDER -----------------
        await status_msg.edit_text(f"✅  `{title}` ɪɴᴅɪʀɪʟɪʏᴏʀ, ɢöɴᴅᴇʀɪʟɪʏᴏʀ...")
        if search_type == "music":
            await message.reply_audio(file_name, caption=title)
        else:
            await message.reply_video(file_name, caption=title)

        # Dosya temizliği
        try:
            os.remove(file_name)
        except Exception:
            pass

        await status_msg.delete()

    except DownloadError as e:
        await status_msg.edit_text(f"❌ ʏᴏᴜᴛᴜʙᴇ ʜᴀᴛᴀꜱı: {e}")
    except Exception as e:
        await status_msg.edit_text(f"❌ ʜᴀᴛᴀ ᴏʟᴜşᴛᴜ: {e}")

# ----------------- KOMUT BAĞLAMA -----------------

@app.on_message(filters.command("bul") & filters.private)
async def music_search(client, message: Message):
    await search_and_send(message, search_type="music")  # Müzik araması

@app.on_message(filters.command("vbul") & filters.private)
async def video_search(client, message: Message):
    await search_and_send(message, search_type="video")  # Video araması