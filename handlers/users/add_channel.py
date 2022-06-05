import re
from loader import dp, db, bot
from aiogram import types
from states.st import get_about
from keyboards.default.add_films_button import menu, btn
from utils.misc.subscription import check
from data.config import ADMINS

@dp.message_handler(text="Kanal qo'shish", state=get_about.search, user_id=ADMINS)
async def k(msg: types.Message):
    await msg.answer("Meni kanalga admin qilgan bo'lsangiz kanal havolasini yuboring\nNamuna: @dramaticEng",reply_markup=menu, disable_web_page_preview=True)
    await get_about.channel.set()

@dp.message_handler(state=get_about.channel, user_id=ADMINS)
async def k(msg: types.Message):
    if re.match('^@', msg.text):
        try:
            s = await check(user_id=msg.from_user.id, channel=msg.text)
            try:
                db.add_channel(msg.text)
                await msg.answer(f"{msg.text} kanallar ro'yxatiga qo'shildi!")
                await msg.answer(f"Siz bosh menyudasiz! Kerak bo'lgan kinoni nomini kiriting:", reply_markup=btn)
            except:
                await msg.answer("Bunday havola bizning ro'yxatda mavjud!", reply_markup=menu)
        except:
            await msg.answer("Iltimos meni admin qiling!", reply_markup=menu)
    else:
        await msg.answer("Namuna shaklida yuboring!\nNamuna: @dramaticEng", reply_markup=menu)