from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from states import Register
from texts import (
    START_TEXT,REGISTERED_START_TEXT)
from buttons import (
    START_BUTTONS, PHONE_BUTTON,
    REGISTER_SUCCESS_BUTTONS,
    LOCATION_BUTTON, GENDER_BUTTON
)
from filters import is_valid_name

from database import is_register_by_id,insert_user

start_router = Router()


@start_router.message(CommandStart())
async def start_handler(message: Message):
    if is_register_by_id(message.from_user.id):
        await message.answer(REGISTERED_START_TEXT,reply_markup=REGISTER_SUCCESS_BUTTONS)
    else:
        await message.answer(START_TEXT, reply_markup=START_BUTTONS)


@start_router.message(F.text == "Register")
async def register_handler(message: Message, state: FSMContext):
    text = "Registratsiya jarayonini boshlaymiz!\nIsmingizni kiriting:"
    await state.set_state(Register.name)
    await message.answer(text, reply_markup=ReplyKeyboardRemove())


@start_router.message(Register.name)
async def get_name(message: Message, state: FSMContext):
    full_name = message.text

    if is_valid_name(full_name):
        await state.update_data(name=full_name)
        await state.set_state(Register.phone)
        await message.answer(
            "Ism qabul qilindi! Telefon raqam kiriting:\nMisol: +998901234567",
            reply_markup=PHONE_BUTTON
        )
    else:
        await message.answer("Ism to'g'ri formatda emas, qayta kiriting.")


@start_router.message(Register.phone)
async def get_phone(message: Message, state: FSMContext):
    if message.contact:
        phone = message.contact.phone_number
    else:
        phone = message.text

    await state.update_data(phone=phone)
    await state.set_state(Register.gender)
    await message.answer(f"Telefon raqam {phone} saqlandi.", reply_markup=ReplyKeyboardRemove())
    await message.answer("Jinsni tanlang:", reply_markup=GENDER_BUTTON)


@start_router.callback_query(F.data.startswith("gender_"))
async def get_gender(call: CallbackQuery, state: FSMContext):
    gender = call.data.split("_")[-1]
    await state.update_data(gender=gender)
    await state.set_state(Register.address)

    await call.answer(f"Siz {gender} ni tanladingiz")
    await call.message.edit_reply_markup()
    await call.message.edit_text(f"Siz {gender} tanladingiz")
    await call.message.answer("Manzilingizni yuboring:", reply_markup=LOCATION_BUTTON)


@start_router.message(Register.address)
async def get_address(message: Message, state: FSMContext):
    if message.location:
        lon = message.location.longitude
        lat = message.location.latitude
        
        data = await state.get_data()
        await state.clear()
        
        fullname = data.get("name")
        phone = data.get("phone")
        gender = data.get("gender")
        address = f"lon:{lon}, lat:{lat}"
        
        await state.update_data(location=(lon, lat))
        if insert_user(fullname,phone,gender,address,message.from_user.id):
            await message.answer(
            "Tabriklaymiz, siz to'liq ro'yxatdan o'tdingiz!",
            reply_markup=REGISTER_SUCCESS_BUTTONS
            )
        else:
            await message.answer("Register qilishda muammo bor qayta ro'yxatdan o'ting", reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer("Iltimos, lokatsiyani button orqali yuboring:")
