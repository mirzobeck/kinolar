from loader import db, dp, bot
from aiogram import types
from states.st import get_about
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.config import ADMINS
from keyboards.default.add_films_button import menu, btn2

@dp.message_handler(text='Kanal olib tashlash' ,state=get_about.search, user_id=ADMINS)
async def delete_ch(msg: types.Message):
    s = "Kanallar ro'yxati:\n\n"
    btn = InlineKeyboardMarkup()
    channels = db.get_channel()
    for channel in channels:
        kanal = await bot.get_chat(channel[0])
        title = kanal.title
        btn.row(InlineKeyboardButton(f"❌ {title} ❌", callback_data=channel[0]))
        invite_link = await kanal.export_invite_link()
        s += f"<a href='{invite_link}'>{title}</a>\n"
    await msg.answer(s, parse_mode='html', reply_markup=btn, disable_web_page_preview=True)
    await get_about.del_channel.set()


@dp.callback_query_handler(state=get_about.del_channel, user_id=ADMINS)
async def delete(call: types.CallbackQuery):
    db.delete_channel(link=call.data)
    await call.message.delete()
    if len(db.get_channel()) == 0:
        await call.message.answer(f"Siz bosh menyudasiz! Kerak bo'lgan kinoni nomini kiriting:\nYou are in the main menu! Enter the name of the movie you want:", reply_markup=btn2)
        await get_about.search.set()
    else:
        s = "Kanallar ro'yxati:\n\n"
        btn = InlineKeyboardMarkup()
        channels = db.get_channel()
        for channel in channels:
            kanal = await bot.get_chat(channel[0])
            title = kanal.title
            btn.row(InlineKeyboardButton(f"❌ {title} ❌", callback_data=channel[0]))
            invite_link = await kanal.export_invite_link()
            s += f"<a href='{invite_link}'>{title}</a>\n"
        await call.message.answer(s, parse_mode='html', reply_markup=btn, disable_web_page_preview=True)
        await get_about.del_channel.set()