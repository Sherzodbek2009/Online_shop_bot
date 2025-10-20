from aiogram.types import (
    KeyboardButton,ReplyKeyboardMarkup,
    InlineKeyboardMarkup,InlineKeyboardButton)




MENU_GENDER_BUTTON = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Male",callback_data="menu_gender_male")],
        [InlineKeyboardButton(text="Female",callback_data="menu_gender_female")],
        [InlineKeyboardButton(text="Child",callback_data="menu_gender_child")],
        [InlineKeyboardButton(text="Cancel",callback_data="menu_gender_cancel")]
    ]
)


CATEGORY_BUTTON = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👕 Shirt", callback_data="category_shirt"),
            InlineKeyboardButton(text="👟 Shoes", callback_data="category_shoes"),
        ],
        [
            InlineKeyboardButton(text="🧢 Cap", callback_data="category_cap"),
            InlineKeyboardButton(text="🧥 Jacket", callback_data="category_jacket"),
        ],
        [
            InlineKeyboardButton(text="👖 Trousers", callback_data="category_trousers"),
            InlineKeyboardButton(text="⌚ Accessory", callback_data="category_accessory"),
        ],
        [
            InlineKeyboardButton(text="🤵 Suit", callback_data="category_suit"),
            InlineKeyboardButton(text="👜 Bag", callback_data="category_bag"),
        ],
        [
            InlineKeyboardButton(text="⬅️ Back", callback_data="go_back"),
        ]
    ]
)




SEASON_BUTTON = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌸 Bahor", callback_data="season_spring"),
            InlineKeyboardButton(text="☀️ Yoz", callback_data="season_summer"),
        ],
        [
            InlineKeyboardButton(text="🍂 Kuz", callback_data="season_autumn"),
            InlineKeyboardButton(text="❄️ Qish", callback_data="season_winter"),
        ],
        [
            InlineKeyboardButton(text="🔙 Orqaga", callback_data="season_back"),
        ]
    ]
)