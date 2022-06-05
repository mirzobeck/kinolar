from loader import dp, db
from aiogram import types
from states.st import get_about

@dp.message_handler(state=get_about.search)
async def s(message: types.Message):
    if len(message.text) >= 4:
        try:
            films = db.search_film(q=f"%{message.text}%")
            for film in films:
                try:    
                    if film[1] == None:
                        await message.answer_photo(film[2], caption=f"<a href='{film[3]}'>{film[0]}</a>\n\nBizning ijtimoiy tarmoqlar:\nOur social networks:\n<a href='https://t.me/dramaticEng'>Telegram</a>  |  <a href='https://www.youtube.com/channel/UCtHZPqD5u4MlzPRABEuFtjw'>YouTube</a>")
                    else:
                        await message.answer_photo(film[2], caption=f"<a href='{film[3]}'>{film[0]}</a>\n\n {film[1]}\n\nBizning ijtimoiy tarmoqlar:\nOur social networks:\n<a href='https://t.me/dramaticEng'>Telegram</a>  |  <a href='https://www.youtube.com/channel/UCtHZPqD5u4MlzPRABEuFtjw'>YouTube</a>")
                except:
                    if film[1] == None:
                        await message.answer(f"<a href='{film[3]}'>{film[0]}</a>\n\nBizning ijtimoiy tarmoqlar:\nOur social networks:\n<a href='https://t.me/dramaticEng'>Telegram</a>  |  <a href='https://www.youtube.com/channel/UCtHZPqD5u4MlzPRABEuFtjw'>YouTube</a>", disable_web_page_preview=True)
                    else:
                        await message.answer(f"<a href='{film[3]}'>{film[0]}</a>\n\n {film[1]}\n\nBizning ijtimoiy tarmoqlar:\nOur social networks:\n<a href='https://t.me/dramaticEng'>Telegram</a>  |  <a href='https://www.youtube.com/channel/UCtHZPqD5u4MlzPRABEuFtjw'>YouTube</a>", disable_web_page_preview=True)
            if len(films) == 0:
                await message.answer(f"Kinolarning nomi orasida '{message.text}' degan so'z yoki belgi qatnashgan kino topilmadi, uzr!")
        except:
            await message.answer(f"Kinolarning nomi orasida '{message.text}' degan so'z yoki belgi qatnashgan kino topilmadi, uzr!")
    else:
        await message.answer(f"Kamida 4 ta belgidan iborat bo'lgan so'z kiriting:")
        await get_about.search.set()
    