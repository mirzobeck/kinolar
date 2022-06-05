import asyncio
from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot
import pandas as pd
from keyboards.default.add_films_button import btn, btn2
from states.st import get_about
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import CHANNELS
from utils.misc.subscription import check

@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    id = []
    name = []
    for user in users:
        id.append(user[0])
        name.append(user[1])
    data = {
        "Telegram ID": id,
        "Name": name
    }
    pd.options.display.max_rows = 10000
    df = pd.DataFrame(data)
    if len(df) > 50:
        for x in range(0, len(df), 50):
            await bot.send_message(message.chat.id, df[x:x + 50])
    else:
       await bot.send_message(message.chat.id, df)
       

@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text="@dramaticEng kanaliga obuna bo'ling!")
        await asyncio.sleep(0.05)

@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")



@dp.message_handler(commands=['start'], state='*', user_id=ADMINS)
async def admnn(message: types.Message):
    if len(db.get_channel()) == 0:
        await message.answer("Salom ADMIN! Xush kelibsiz", reply_markup=btn2)
    else:
        await message.answer("Salom ADMIN! Xush kelibsiz", reply_markup=btn)
    await get_about.search.set()
    try:
        p = 0
        test = True
        channels_format = str()
        for channel in db.get_channel():
            t = await check(user_id=message.from_user.id, channel=channel[0])
            test *= t
            chat = await bot.get_chat(channel[0])
            invite_link = await chat.export_invite_link()
            channels_format += f"➡️ <a href='{invite_link}'><b>{chat.title}</b></a>\n"
            p += 1
        if test:
            name = message.from_user.full_name
            await message.answer(f"Xush kelibsiz! {name}\n\nMen siz istagan kinoingizni subtitrlisini topishga yordam beraman 🎬.\nKerak bo'lgan kinoni nomini kiriting: \n\nWelcome! \nI’m a bot who brings out the movies you’re looking for with subtitles 🎬\nEnter the name of the movie:")
            await get_about.search.set()
        else:
            if p == 1:
                await message.answer(f"Quyidagi kanalga obuna bo'ling:\nSubscribe to the following channel:\nSubscribe to the following channel: \n\n"
                                    f"{channels_format}",
                                    disable_web_page_preview=True)
            else:
                await message.answer(f"Quyidagi kanalga obuna bo'ling:\nSubscribe to the following channels:\nSubscribe to the following channels: \n\n"
                                    f"{channels_format}",
                                    disable_web_page_preview=True)
            await get_about.search.set()
        db.add_user(id=message.from_user.id,
                        name=message.from_user.full_name)
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)
    except:
        pass


@dp.callback_query_handler(text='main menu', state='*')
async def d(call: types.CallbackQuery):
    if len(db.get_channel()) == 0:
        await call.message.answer(f"Siz bosh menyudasiz! Kerak bo'lgan kinoni nomini kiriting:\nYou are in the main menu! Enter the name of the movie you want:", reply_markup=btn2)
    else:
        await call.message.answer(f"Siz bosh menyudasiz! Kerak bo'lgan kinoni nomini kiriting:\nYou are in the main menu! Enter the name of the movie you want:", reply_markup=btn)
    await get_about.search.set()
        