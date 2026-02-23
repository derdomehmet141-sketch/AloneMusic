from pyrogram.types import InlineKeyboardButton
from AloneMusic import app

def stream_markup_timer(_, chat_id, played, dur):
    return [
        [
            InlineKeyboardButton(
                text="<b>Red Button</b>",  # HTML ile kırmızı metin
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=f"<i>{_['CLOSE_BUTTON']}</i>", callback_data="close"),  # İtalik metin
            InlineKeyboardButton(
                text="<b>💙 Kanal</b>",  # Kalın metin
                url="https://t.me/The_Team_Kumsal",
            ),
        ],
    ]

def stream_markup(_, chat_id):
    return [
        [
            InlineKeyboardButton(
                text="<b>Red Button</b>",  # HTML ile kırmızı metin
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text=f"<i>{_['CLOSE_BUTTON']}</i>", callback_data="close"),  # İtalik metin
            InlineKeyboardButton(
                text="<b>💙 Kanal</b>",  # Kalın metin
                url="https://t.me/kaygisizlarsohbet",
            ),
        ],
    ]

def track_markup(_, videoid, user_id, channel, fplay):
    return [
        [
            InlineKeyboardButton(
                text="<b>Red Button</b>",  # HTML ile kırmızı metin
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="<u>Play</u>",  # HTML altı çizili metin
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="<i>Pause</i>",  # HTML italik metin
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="<b>CLOSE</b>",  # Kalın metin
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="<i>💙 Kanal</i>",  # HTML italik metin
                url="https://t.me/kaygisizlarsohbet",
            ),
        ],
    ]

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    return [
        [
            InlineKeyboardButton(
                text="<b>Red Button</b>",  # HTML ile kırmızı metin
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="<u>Playlist 1</u>",  # HTML altı çizili metin
                callback_data=f"TuneViaPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="<i>Playlist 2</i>",  # HTML italik metin
                callback_data=f"TuneViaPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="<b>CLOSE</b>",  # Kalın metin
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="<i>💙 Kanal</i>",  # HTML italik metin
                url="https://t.me/kaygisizlarsohbet",
            ),
        ],
    ]

def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    return [
        [
            InlineKeyboardButton(
                text="<b>Red Button</b>",  # HTML ile kırmızı metin
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="<u>Start Live</u>",  # HTML altı çizili metin
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="<b>CLOSE</b>",  # Kalın metin
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="<i>💙 Kanal</i>",  # HTML italik metin
                url="https://t.me/kaygisizlarsohbet",
            ),
        ],
    ]

def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    short_query = query[:20]
    return [
        [
            InlineKeyboardButton(
                text="<b>Red Button</b>",  # HTML ile kırmızı metin
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="<u>Play</u>",  # HTML altı çizili metin
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="<i>Pause</i>",  # HTML italik metin
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="<b>CLOSE</b>",  # Kalın metin
                callback_data=f"forceclose {short_query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="<i>💙 Kanal</i>",  # HTML italik metin
                url="https://t.me/kaygisizlarsohbet",
            ),
        ],
    ]