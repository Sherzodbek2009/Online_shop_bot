from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext


user_router = Router()


@user_router.message(F.text == "Menu")
async def start_menu(message:Message):
    await message.answer("Siz menu bo'limini tanladingiz!")