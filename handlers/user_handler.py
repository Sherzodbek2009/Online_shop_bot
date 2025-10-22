from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from texts import GENDER_TEXT, CATEGORY_TEXT, REGISTERED_START_TEXT, SEASON_TEXT, select_filter,product_text

from buttons import MENU_GENDER_BUTTON, REGISTER_SUCCESS_BUTTONS,SEASON_BUTTON, category_button,plus_minus_for_product
from states import MenuOption
from database import get_filter_products, get_category_by_id

user_router = Router()


@user_router.message(F.text == "Menu")
async def start_menu(message:Message,state:FSMContext):
    
    await state.set_state(MenuOption.gender)
    image_path = "media/image/image.png"
    await message.answer(text="Siz menu ni tanladingiz!",reply_markup=ReplyKeyboardRemove())
    
    await message.answer_photo(photo=FSInputFile(path=image_path),caption=GENDER_TEXT,reply_markup=MENU_GENDER_BUTTON,parse_mode="HTML")
    
    
    @user_router.callback_query(F.data.startswith("menu_gender_"))
    async def get_gender_menu(call:CallbackQuery,state:FSMContext):
        gender = call.data.split("_")[-1]
        
        if gender == "cancel":
            await state.clear()
            await call.message.edit_reply_markup(reply_markup=None)
            await call.message.answer(REGISTERED_START_TEXT,reply_markup=REGISTER_SUCCESS_BUTTONS)
            await call.answer("Cancel")
        else:
            await state.update_data(gender=gender)
            await state.set_state(MenuOption.category)
            
            await call.message.edit_caption(CATEGORY_TEXT)
            await call.message.edit_reply_markup(reply_markup=category_button())
            
            

    
@user_router.callback_query(F.data.startswith("category_"))
async def get_category_menu(call:CallbackQuery,state:FSMContext):
    category = call.data.split("_")[-1]
    
    if category == "back":
        await call.message.edit_caption(caption=GENDER_TEXT,parse_mode="HTML")
        await call.message.edit_reply_markup(reply_markup=MENU_GENDER_BUTTON)
    else:
        await state.update_data(category = category)
        await state.set_state(MenuOption.season)        
        
        await call.message.edit_caption(text = SEASON_TEXT)
        await call.message.edit_reply_markup(reply_markup=SEASON_BUTTON) 
        
        
        

@user_router.callback_query(F.data.startswith("season_"))
async def send_product_by_filter(call:CallbackQuery,state:FSMContext):
    
    season = call.data.split("_")[-1]
    
    if season == "back":
        await call.message.edit_caption(CATEGORY_TEXT)
        await call.message.edit_reply_markup(reply_markup=category_button())
    else:
        data = await state.get_data()
        gender = data.get("gender")
        category_id = data.get("category")
        await state.clear()
        
        
        await call.message.edit_reply_markup(reply_markup=None)
        category_name = get_category_by_id(category_id)[0]
        
        await call.message.answer(text=select_filter(gender.capitalize(),category_name,season))
        
        data = get_filter_products(category_id,season,gender)
        
        for product in data:
            await call.message.answer_photo(
                photo=FSInputFile(path=f"media/image/main.jpg"),
            caption=product_text(product[1],product[8],category_name,gender,product[5],season,product[3]),
            reply_markup=plus_minus_for_product(product[0]),
            )
            


@user_router.callback_query(F.data.startswith("plus_"))
async def plus_product(call:CallbackQuery):
    number = int(call.data.split("_")[1])
    product_id = call.data.split("_")[-1]
    
    if number >=10:
        await call.answer("Mahsulot 10 tadan ko'p bo'lishi mumkin emas")
    else:
        number+=1
    
    await call.message.edit_reply_markup(reply_markup=plus_minus_for_product(product_id,number))

@user_router.callback_query(F.data.startswith("minus_"))
async def plus_product(call:CallbackQuery):
    number = int(call.data.split("_")[1])
    product_id = call.data.split("_")[-1]
    
    if number <=1:
        await call.answer("Mahsulot 1 tadan kam bo'lishi mumkin emas")
    else:
        number-=1
    
    await call.message.edit_reply_markup(reply_markup=plus_minus_for_product(product_id,number))