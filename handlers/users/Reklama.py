from email import message
from aiogram import types
from handlers.users.add_films import photos
from loader import dp, db, bot
from aiogram.dispatcher.storage import FSMContext
from states.st import rek, get_about
from keyboards.default.add_films_button import rek_btn, btn, btn2, menu
from keyboards.inline.nxt import allow
from data.config import ADMINS
import asyncio


@dp.message_handler(text='Reklama tarqatish', state=get_about.search, user_id=ADMINS)
async def reklama(msg: types.Message):
    await msg.answer('Fayl turini tanlang:', reply_markup=rek_btn)
    await rek.turi.set()


@dp.message_handler(state=rek.turi, user_id=ADMINS)
async def reklama(msg: types.Message, state: FSMContext):
    await state.update_data(
        {
            'turi' : msg.text
        }
    )
    if msg.text == "Video 📹":
        await msg.answer("Video yuboring:", reply_markup=menu)
        await rek.video.set()
    elif msg.text == "Foto 📷":
        await msg.answer("Foto yuboring:", reply_markup=menu)
        await rek.photo.set()
    elif msg.text == "Xabar ✍🏻":
        await msg.answer("Xabar yuboring:", reply_markup=menu)
        await rek.xabar.set()
    else:
        await msg.answer("Iltimos, fayl turini tanlang!")

@dp.message_handler(state=rek.video, content_types=['video'], user_id=ADMINS)
async def reklama(msg: types.Message, state: FSMContext):
    await state.update_data(
        {
            'video' : msg.video.file_id
        }
    )
    await msg.answer('Videoning matnini kiriting:', reply_markup=menu)
    await rek.capti.set()


@dp.message_handler(state=rek.video, user_id=ADMINS)
async def reklama(msg: types.Message, state: FSMContext):
    await msg.answer('Iltimos, video yuboring!')

@dp.message_handler(state=rek.photo, content_types=['photo'], user_id=ADMINS)
async def reklama(msg: types.Message, state: FSMContext):
    await state.update_data(
        {
            'photo' : msg.photo[-1].file_id
        }
    )
    await msg.answer('Fotoning matnini kiriting:', reply_markup=menu)
    await rek.capti.set()

@dp.message_handler(state=rek.photo, user_id=ADMINS)
async def reklama(msg: types.Message, state: FSMContext):
    await msg.answer('Iltimos, foto yuboring')

@dp.message_handler(state=rek.xabar)
async def reklama(msg: types.Message, state: FSMContext):
    await state.update_data(
        {
            'message' : msg.text
        }
    )
    await bot.send_message(msg.from_user.id, msg.text, reply_markup=allow)



@dp.message_handler(state=rek.capti, user_id=ADMINS)
async def reklama(msg: types.Message, state: FSMContext):
    await state.update_data(
        {
            'caption' : msg.text
        }
    )
    data = await state.get_data()
    video = data.get('video')
    foto = data.get('photo')
    turi = data.get('turi')
    if turi == "Video 📹":
        await bot.send_video(msg.from_user.id, video=video, caption=msg.text, reply_markup=allow)
    elif turi == "Foto 📷":
        await bot.send_photo(msg.from_user.id, photo=foto, caption=msg.text, reply_markup=allow)
    

@dp.callback_query_handler(state='*', text='send', user_id=ADMINS)
async def send(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    video = data.get('video')
    foto = data.get('photo')
    cap = data.get('caption')
    msg = data.get('message')
    turi = data.get('turi')
    user = db.select_all_users()
    for user_id in user:
        try:
            if turi == "Video 📹":
                await bot.send_video(user_id[0], video=video, caption=cap)
            elif turi == "Foto 📷":
                await bot.send_photo(user_id[0], photo=foto, caption=cap)
            elif turi == "Xabar ✍🏻":
                await bot.send_message(user_id[0], text=msg)
            await asyncio.sleep(0.05)
        except:
            pass
    if len(db.get_channel()) == 0:
        await call.message.answer(f"Siz bosh menyudasiz! Kerak bo'lgan kinoni nomini kiriting:", reply_markup=btn2)
    else:
        await call.message.answer(f"Siz bosh menyudasiz! Kerak bo'lgan kinoni nomini kiriting:", reply_markup=btn)
    await get_about.search.set()