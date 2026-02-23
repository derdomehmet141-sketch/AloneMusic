from pyrogram.types import InlineKeyboardButton
from AloneMusic import app

def stream_markup_timer(_, chat_id, played, dur):
    return [
        # Üst satır: Beni Ekle ve Kanal butonları
        [
            InlineKeyboardButton(
                text="<b>Beni Ekle</b>",  # Kalın metin
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
            InlineKeyboardButton(
                text="<b>💙 Kanal</b>",  # Kalın metin
                url="https://t.me/The_Team_Kumsal",
            ),
        ],
        # İkinci satır: Play, Pause, Record, Repeat butonları
        [
            InlineKeyboardButton(
                text="⏸️",  # Pause
                callback_data="pause"
            ),
            InlineKeyboardButton(
                text="▶️",  # Play
                callback_data="play"
            ),
            InlineKeyboardButton(
                text="⏺️",  # Record
                callback_data="record"
            ),
            InlineKeyboardButton(
                text="🔂",  # Repeat
                callback_data="repeat"
            ),
        ],
        # Üçüncü satır: Geri sarma, Menü kapama ve İleri sarma
        [
            InlineKeyboardButton(
                text="⏪ -20s",  # 20 saniye geri sarma
                callback_data="rewind_20"
            ),
            InlineKeyboardButton(
                text="❌ Menüyü Kapat",  # Menü kapama
                callback_data="close_menu"
            ),
            InlineKeyboardButton(
                text="⏩ +20s",  # 20 saniye ileri sarma
                callback_data="forward_20"
            ),
        ],
    ]

def stream_markup(_, chat_id):
    return [
        # Üst satır: Beni Ekle ve Kanal butonları
        [
            InlineKeyboardButton(
                text="<b>Beni Ekle</b>",  # Kalın metin
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
            InlineKeyboardButton(
                text="<b>💙 Kanal</b>",  # Kalın metin
                url="https://t.me/kaygisizlarsohbet",
            ),
        ],
        # İkinci satır: Play, Pause, Record, Repeat butonları
        [
            InlineKeyboardButton(
                text="⏸️",  # Pause
                callback_data="pause"
            ),
            InlineKeyboardButton(
                text="▶️",  # Play
                callback_data="play"
            ),
            InlineKeyboardButton(
                text="⏺️",  # Record
                callback_data="record"
            ),
            InlineKeyboardButton(
                text="🔂",  # Repeat
                callback_data="repeat"
            ),
        ],
        # Üçüncü satır: Geri sarma, Menü kapama ve İleri sarma
        [
            InlineKeyboardButton(
                text="⏪ -20s",  # 20 saniye geri sarma
                callback_data="rewind_20"
            ),
            InlineKeyboardButton(
                text="❌ Menüyü Kapat",  # Menü kapama
                callback_data="close_menu"
            ),
            InlineKeyboardButton(
                text="⏩ +20s",  # 20 saniye ileri sarma
                callback_data="forward_20"
            ),
        ],
    ]

def track_markup(_, videoid, user_id, channel, fplay):
    return [
        # Üst satır: Beni Ekle ve Kanal butonları
        [
            InlineKeyboardButton(
                text="<b>Beni Ekle</b>",  # Kalın metin
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
            InlineKeyboardButton(
                text="<b>💙 Kanal</b>",  # Kalın metin
                url="https://t.me/kaygisizlarsohbet",
            ),
        ],
        # İkinci satır: Play, Pause, Record, Repeat butonları
        [
            InlineKeyboardButton(
                text="⏸️",  # Pause
                callback_data="pause"
            ),
            InlineKeyboardButton(
                text="▶️",  # Play
                callback_data="play"
            ),
            InlineKeyboardButton(
                text="⏺️",  # Record
                callback_data="record"
            ),
            InlineKeyboardButton(
                text="🔂",  # Repeat
                callback_data="repeat"
            ),
        ],
        # Üçüncü satır: Geri sarma, Menü kapama ve İleri sarma
        [
            InlineKeyboardButton(
                text="⏪ -20s",  # 20 saniye geri sarma
                callback_data="rewind_20"
            ),
            InlineKeyboardButton(
                text="❌ Menüyü Kapat",  # Menü kapama
                callback_data="close_menu"
            ),
            InlineKeyboardButton(
                text="⏩ +20s",  # 20 saniye ileri sarma
                callback_data="forward_20"
            ),
        ],
    ]
def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonyPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonyPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons