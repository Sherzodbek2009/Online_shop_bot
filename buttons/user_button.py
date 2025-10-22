from aiogram.types import (
    KeyboardButton,ReplyKeyboardMarkup,
    InlineKeyboardMarkup,InlineKeyboardButton)

from database import get_category



MENU_GENDER_BUTTON = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Male",callback_data="menu_gender_male")],
        [InlineKeyboardButton(text="Female",callback_data="menu_gender_female")],
        [InlineKeyboardButton(text="Child",callback_data="menu_gender_child")],
        [InlineKeyboardButton(text="Cancel",callback_data="menu_gender_cancel")]
    ]
)


def category_button():
    inline_keyboard = []
    button = []
    data = get_category()
    
    for i in range(1,len(data)+1):
        button.append(InlineKeyboardButton(text=data[i-1][1],callback_data=f"category_{data[i-1][0]}"))
        if i % 2 == 0:
            inline_keyboard.append(button)
            button = []
            
    if button:
        inline_keyboard.append(button)
            
    inline_keyboard.append(InlineKeyboardButton(text="⬅️ Back", callback_data="go_back"))
    
    return InlineKeyboardMarkup(
        inline_keyboard=inline_keyboard
    )


SEASON_BUTTON = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌤️ All", callback_data="season_All"),
        ],
        [
            InlineKeyboardButton(text="🌸 Bahor", callback_data="season_Spring"),
            InlineKeyboardButton(text="☀️ Yoz", callback_data="season_Summer"),
        ],
        [
            InlineKeyboardButton(text="🍂 Kuz", callback_data="season_Autumn"),
            InlineKeyboardButton(text="❄️ Qish", callback_data="season_Winter"),
        ],
        [
            InlineKeyboardButton(text="🔙 Orqaga", callback_data="season_back"),
        ]
    ]
)

def plus_minus_for_product(product_id,number=1):
    return InlineKeyboardMarkup(
        [
            InlineKeyboardButton(text="➖",callback_data=f"minus_{number}_{product_id}"),
            InlineKeyboardButton(text=f"{number}",callback_data="send_plus_minus"),
            InlineKeyboardButton(text="➕",callback_data=f"plus_{number}_{product_id}"),
        ],
        [
            InlineKeyboardButton(text="❌ Cancel",callback_data=f"cancel_{number}_{product_id}"),
            InlineKeyboardButton(text="✅ Save",callback_data=f"save_{number}_{product_id}")
        ]
    )