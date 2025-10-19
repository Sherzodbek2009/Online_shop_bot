from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.types.input_file import FSInputFile

user_router = Router()


@user_router.message(F.text == "Menu")
async def start_menu(message:Message):
    
    image_path = "media/image/image.png"
    
    await message.answer_photo(photo=FSInputFile(path=image_path))
    
    
    
    await message.answer("Siz menu bo'limini tanladingiz!")
    