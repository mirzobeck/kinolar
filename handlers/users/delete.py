from loader import db, dp
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from states.st import get_about
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.default.add_films_button import menu, btn, btn2
from data.config import ADMINS

@dp.message_handler(text='Kino olib tashlash', state=get_about.search, user_id=ADMINS)
async def delete(message: types.Message):
    await message.answer("Olib tashlamoqchi bo'lgan kinoyingizni nomini yoki bironta belgisini kiriting:")
    await get_about.delete.set()

@dp.message_handler(state=get_about.delete, user_id=ADMINS)
async def delete(msg: types.Message):
    if len(msg.text) >= 4:
        btn = InlineKeyboardMarkup()
        films = db.delete_list_film(q=f"%{msg.text}%")
        f = ""
        try:
            if films is not []:
                await msg.answer(f"'{msg.text}' so'zi qatshgan kinolar ro'yxati", reply_markup=menu)
            for film in films:
                if film[1] == None:
                    f += f'<a href="{film[3]}">{film[0]}</a>\n'
                    btn.row(InlineKeyboardButton(f"❌ {film[0]} ❌", callback_data=film[3]))
                else:
                    f += f'<a href="{film[3]}">{film[0]}</a>  -  {film[1]}\n'
                    btn.row(InlineKeyboardButton(f"❌ {film[0]} ❌", callback_data=film[3]))
            await msg.answer(f, reply_markup=btn, parse_mode='html', disable_web_page_preview=True)
            await get_about.one_delete.set()
        except:
            if films is []:
                await msg.answer("Hozircha kinolar yo'q, uzr!")
            else:
                await msg.answer(f"Kinolarning nomi orasida '{msg.text}' degan so'z yoki belgi qatnashgan kino topilmadi, uzr!\nNo movies with the word '{msg.text}' included in the movie title, sorry!")
    else:
        await msg.answer(f"Kamida 4 ta belgidan iborat bo'lgan nom kiriting:\nEnter a name of at least 4 characters:")
        await get_about.delete.set()

@dp.message_handler(text='Bosh menyu', state='*', user_id=ADMINS)
async def delete(msg: types.Message):
    await get_about.search.set()
    if len(db.get_channel()) == 0:
        await msg.answer(f"Siz bosh menyudasiz! Kerak bo'lgan kinoni nomini kiriting:\nYou are in the main menu! Enter the name of the movie you want:", reply_markup=btn2)
    else:
        await msg.answer(f"Siz bosh menyudasiz! Kerak bo'lgan kinoni nomini kiriting:\nYou are in the main menu! Enter the name of the movie you want:", reply_markup=btn)
    

@dp.callback_query_handler(state=get_about.one_delete, user_id=ADMINS)
async def delete(call: types.CallbackQuery):
    db.delete_film(link=call.data)
    await call.message.delete()
    if len(db.get_channel()) == 0:
        await call.message.answer("Yana olib tashlamoqchi bo'lgan kinoyingizni nomini yoki bironta belgisini kiriting:", reply_markup=menu)
        await get_about.delete.set()
    else:
        await call.message.answer(f"Siz bosh menyudasiz! Kerak bo'lgan kinoni nomini kiriting:\nYou are in the main menu! Enter the name of the movie you want:", reply_markup=btn2)
        await get_about.del_channel.set()