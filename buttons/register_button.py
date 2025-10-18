from aiogram.types import (
    KeyboardButton,ReplyKeyboardMarkup,
    InlineKeyboardMarkup,InlineKeyboardButton)

START_BUTTONS = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Register"),KeyboardButton(text="Menu")],
        [KeyboardButton(text="Orders"),KeyboardButton(text="Contact")]
    ],
    resize_keyboard=True
)


REGISTER_SUCCESS_BUTTONS = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Menu")],
        [KeyboardButton(text="Orders")],
        [KeyboardButton(text="Contact")]
    ],
    resize_keyboard=True
)


PHONE_BUTTON = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Phone",request_contact=True)]
    ],
    resize_keyboard=True
)


LOCATION_BUTTON = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Location",request_location=True)]
    ],
    resize_keyboard=True
)


GENDER_BUTTON = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Male",callback_data="gender_male"),
        InlineKeyboardButton(text="Female",callback_data="gender_female")
    ]
    ]
)