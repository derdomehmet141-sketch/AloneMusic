#
# Copyright (C) 2021-2022 by TheAloneteam@Github, < https://github.com/TheAloneTeam >.
#
# This file is part of < https://github.com/TheAloneTeam/AloneMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheAloneTeam/AloneMusic/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import InlineKeyboardButton
import config
from AloneMusic import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url="https://t.me/The_Team_Kumsal"),
        ],
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            # Yardım Menüsünü açan asıl buton budur
            InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_2"], url="https://t.me/The_Team_Kumsal"),

InlineKeyboardButton(text=_["S_B_6"], user_id=config.OWNER_ID),
        ],
    ]
    return buttons
