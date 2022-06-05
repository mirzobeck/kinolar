import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS, CHANNELS
from loader import dp, db, bot
from states.st import get_about
from utils.misc.subscription import check

# @dp.message_handler(commands=['start'], state='*')
# async def bot_start(message: types.Message):
#     name = message.from_user.full_name
#     # Foydalanuvchini bazaga qo'shamiz
#     try:
#         db.add_user(id=message.from_user.id,
#                     name=name)
#         await message.answer(f"Xush kelibsiz! {name}\n\nMen siz istagan kinoingizni subtitrlisini topishga yordam beraman 🎬.\nKerak bo'lgan kinoni nomini kiriting: \n\nWelcome! \nI’m a bot who brings out the movies you’re looking for with subtitles 🎬\nEnter the name of the movie:")
#         # Adminga xabar beramiz
#         count = db.count_users()[0]
#         msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
#         await bot.send_message(chat_id=ADMINS[0], text=msg)
#         await get_about.search.set()

#     except sqlite3.IntegrityError as err:
#         await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazaga oldin qo'shilgan")
#         await message.answer(f"Xush kelibsiz! {name}\n\nMen siz istagan kinoingizni subtitrlisini topishga yordam beraman 🎬.\nKerak bo'lgan kinoni nomini kiriting: \n\nWelcome! \nI’m a bot who brings out the movies you’re looking for with subtitles 🎬\nEnter the name of the movie:")
#         await get_about.search.set()

@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
    # await message.answer(f"Salom, {message.from_user.full_name}!\nYangi e'lon berishni hohlaysizmi?", reply_markup=menu)
        p = 0
        test = True
        channels_format = str()
        for channel in db.get_channel():
            t = await check(user_id=message.from_user.id, channel=channel[0])
            test *= t
            chat = await bot.get_chat(channel[0])
            invite_link = await chat.export_invite_link()
            # logging.info(invite_link)
            if not t:
                channels_format += f"➡️ <a href='{invite_link}'><b>{chat.title}</b></a>\n"
            p += 1
        if test:
            count = db.count_users()[0]
            db.add_user(id=message.from_user.id,
                        name=name)
            msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
            await bot.send_message(chat_id=ADMINS[0], text=msg)
            name = message.from_user.full_name
            await message.answer(f"Xush kelibsiz! {name}\n\nMen siz istagan kinoingizni subtitrlisini topishga yordam beraman 🎬.\nKerak bo'lgan kinoni nomini kiriting: \n\nWelcome! \nI’m a bot who brings out the movies you’re looking for with subtitles 🎬\nEnter the name of the movie:")
            await get_about.search.set()
        else:
            if p == 1:
                await message.answer(f"Quyidagi kanalga obuna bo'ling:\nSubscribe to the following channel: \n\n"
                                    f"{channels_format}\nUlanib bo'lgach qayta /start tugmasini bosing!",
                                    disable_web_page_preview=True)
            else:
                await message.answer(f"Quyidagi kanalga obuna bo'ling:\nSubscribe to the following channels: \n\n"
                                    f"{channels_format}\nUlanib bo'lgach qayta /start tugmasini bosing!",
                                    disable_web_page_preview=True)
            await get_about.search.set()
        

    except sqlite3.IntegrityError as err:
        test = True
        channels_format = str()
        for channel in db.get_channel():
            t = await check(user_id=message.from_user.id, channel=channel[0])
            test *= t
            chat = await bot.get_chat(channel[0])
            invite_link = await chat.export_invite_link()
            # logging.info(invite_link)
            channels_format += f"➡️ <a href='{invite_link}'><b>{chat.title}</b></a>\n"
        if test:
            name = message.from_user.full_name
            await message.answer(f"Xush kelibsiz! {name}\n\nMen siz istagan kinoingizni subtitrlisini topishga yordam beraman 🎬.\nKerak bo'lgan kinoni nomini kiriting: \n\nWelcome! \nI’m a bot who brings out the movies you’re looking for with subtitles 🎬\nEnter the name of the movie:")
            await get_about.search.set()
        else:
            if p == 1:
                await message.answer(f"Quyidagi kanalga obuna bo'ling:\nSubscribe to the following channel: \n\n"
                                    f"{channels_format}\nUlanib bo'lgach qayta /start tugmasini bosing!",
                                    disable_web_page_preview=True)
            else:
                await message.answer(f"Quyidagi kanalga obuna bo'ling:\nSubscribe to the following channels: \n\n"
                                    f"{channels_format}\nUlanib bo'lgach qayta /start tugmasini bosing!",
                                    disable_web_page_preview=True)