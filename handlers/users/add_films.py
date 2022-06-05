from loader import dp, db
from aiogram import types
from states.st import get_about
from aiogram.dispatcher.storage import FSMContext
from keyboards.default.add_films_button import next, btn, menu, btn2
from aiogram.types import ReplyKeyboardRemove
from data.config import ADMINS
import re

@dp.message_handler(text="Kino qo'shish", state=get_about.search, user_id=ADMINS)
async def add_film(message: types.Message, state: FSMContext):
    await message.answer("Kinoni nomini kiriting:", reply_markup=menu)
    await get_about.name.set()


@dp.message_handler(state=get_about.name, user_id=ADMINS)
async def add_film(message: types.Message, state: FSMContext):
    if len(message.text) >= 4:
        await state.update_data(
            {
                'name' : message.text
            }
        )
        await message.answer("Kino haqida ma'lumot bering(ixtiyoriy): ", reply_markup=next)
        await get_about.about.set()
    else:
        await message.answer(f"Kamida 4 ta belgidan iborat bo'lgan nom kiriting:")
        await get_about.name.set()

@dp.message_handler(text="Keyingisi",state=get_about.about, user_id=ADMINS)
async def add_film(message: types.Message, state: FSMContext):
    await state.update_data(
        {
            'about' : None
        }
    )
    await message.answer("Kinoning rasmini jo'nating:", reply_markup=next)
    await get_about.photo.set()



@dp.message_handler(state=get_about.about, user_id=ADMINS)
async def add_film(message: types.Message, state: FSMContext):
    if len(message.text) >= 15:
        await state.update_data(
            {
                'about' : message.text
            }
        )
        await message.answer("Kinoning rasmini jo'nating:", reply_markup=next)
        await get_about.link.set()
    else:
        await message.answer(f"Kamida 15 ta belgidan iborat bo'lishi kerak!")

@dp.message_handler(text="Keyingisi",state=get_about.photo, user_id=ADMINS)
async def add_film(message: types.Message, state: FSMContext):
    await state.update_data(
        {
            'about' : None
        }
    )
    await message.answer("Kinoning havolasini jo'nating:", reply_markup=menu)
    await get_about.link.set()

@dp.message_handler(state=get_about.photo, content_types=['photo'])
async def photos(msg: types.Message, state: FSMContext):
    await state.update_data(
        {
            'photo' : msg.photo[-1].file_id
        }
    )
    await msg.answer("Kinoning havolasini jo'nating:", reply_markup=menu)
    await get_about.link.set()

@dp.message_handler(state=get_about.link, user_id=ADMINS)
async def add_film(message: types.Message, state: FSMContext):
    data = await state.get_data() 
    try:
        if re.match("^https://", message.text) or re.match("^http://", message.text):
            name = data.get('name')
            about = data.get('about')
            photo = data.get('photo')
            link = message.text
            db.add_film(name=name, photo=photo, about=about, link=link)
            await get_about.search.set()
            await message.answer(f"<a href='{message.text}'>Kino</a> muvaffaqiyatli qo'shildi!", parse_mode='html',reply_markup=btn, disable_web_page_preview=True)
        else:
            await message.answer("Qaytadan!\nFaqat havola kiriting:")
            await get_about.link.set()
    except:
        await message.answer(f"{message.text} bu havolada turgan kino bor! Qaytadan boshqa kino kiriting:", disable_web_page_preview=True)
        await get_about.search.set()
        if len(db.get_channel()) == 0:
            await message.answer(f"Siz bosh menyudasiz! Kerak bo'lgan kinoni nomini kiriting:", reply_markup=btn2)
        elif len(db.get_channel()) == 0:
            await message.answer(f"Siz bosh menyudasiz! Kerak bo'lgan kinoni nomini kiriting:", reply_markup=btn)
