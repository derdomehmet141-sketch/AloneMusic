from pyrogram.types import InlineKeyboardButton
from AloneMusic import app

# Genel buton oluşturma fonksiyonu
def create_button(text, callback_data=None, url=None):
    if url:
        return InlineKeyboardButton(text=text, url=url)
    if callback_data:
        return InlineKeyboardButton(text=text, callback_data=callback_data)
    return None

def stream_markup_timer(_, chat_id, played, dur):
    return [
        [
            create_button("<b>Beni Ekle</b>", url=f"https://t.me/{app.username}?startgroup=true"),
            create_button("<b>💙 Kanal</b>", url="https://t.me/The_Team_Kumsal"),
        ],
        [
            create_button("⏸️", callback_data="pause"),
            create_button("▶️", callback_data="play"),
            create_button("⏺️", callback_data="record"),
            create_button("🔂", callback_data="repeat"),
        ],
        [
            create_button("⏪ -20s", callback_data="rewind_20"),
            create_button("❌ Menüyü Kapat", callback_data="close_menu"),
            create_button("⏩ +20s", callback_data="forward_20"),
        ],
    ]

def stream_markup(_, chat_id):
    return [
        [
            create_button("<b>Beni Ekle</b>", url=f"https://t.me/{app.username}?startgroup=true"),
            create_button("<b>💙 Kanal</b>", url="https://t.me/kaygisizlarsohbet"),
        ],
        [
            create_button("⏸️", callback_data="pause"),
            create_button("▶️", callback_data="play"),
            create_button("⏺️", callback_data="record"),
            create_button("🔂", callback_data="repeat"),
        ],
        [
            create_button("⏪ -20s", callback_data="rewind_20"),
            create_button("❌ Menüyü Kapat", callback_data="close_menu"),
            create_button("⏩ +20s", callback_data="forward_20"),
        ],
    ]

def track_markup(_, videoid, user_id, channel, fplay):
    return [
        [
            create_button("<b>Beni Ekle</b>", url=f"https://t.me/{app.username}?startgroup=true"),
            create_button("<b>💙 Kanal</b>", url="https://t.me/kaygisizlarsohbet"),
        ],
        [
            create_button("⏸️", callback_data="pause"),
            create_button("▶️", callback_data="play"),
            create_button("⏺️", callback_data="record"),
            create_button("🔂", callback_data="repeat"),
        ],
        [
            create_button("⏪ -20s", callback_data="rewind_20"),
            create_button("❌ Menüyü Kapat", callback_data="close_menu"),
            create_button("⏩ +20s", callback_data="forward_20"),
        ],
    ]

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    return [
        [
            create_button(_["P_B_1"], callback_data=f"AnonyPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}"),
            create_button(_["P_B_2"], callback_data=f"AnonyPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}"),
        ],
        [
            create_button(_["CLOSE_BUTTON"], callback_data=f"forceclose {videoid}|{user_id}"),
        ],
    ]

def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    return [
        [
            create_button(_["P_B_3"], callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}"),
        ],
        [
            create_button(_["CLOSE_BUTTON"], callback_data=f"forceclose {videoid}|{user_id}"),
        ],
    ]

def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    return [
        [
            create_button(_["P_B_1"], callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"),
            create_button(_["P_B_2"], callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}"),
        ],
        [
            create_button("◁", callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}"),
            create_button(_["CLOSE_BUTTON"], callback_data=f"forceclose {query}|{user_id}"),
            create_button("▷", callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}"),
        ],
    ]