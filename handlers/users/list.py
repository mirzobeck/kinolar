from loader import db, dp
from aiogram import types
from states.st import get_about
from django.core.paginator import Paginator
from aiogram.dispatcher.storage import FSMContext
from keyboards.inline.nxt import next2, back, back_next


@dp.message_handler(commands=['movie_list'], state=get_about.search)
async def al(msg: types.Message, state: FSMContext):
    films = db.sorted_movie()
    n = db.count_movies()[0]
    obj = Paginator(films, 20)
    await state.update_data(
        {
            'page' : 1
        }
    )
    get_pages = await state.get_data()
    page = get_pages.get('page')
    f = ""
    for film in obj.page(page).object_list:
        if film[1] == None:
            f += f'<a href="{film[3]}">{film[0]}</a>\n'
        else:
            f += f'<a href="{film[3]}">{film[0]}</a>  -  {film[1]}\n'
    if obj.page(page).has_other_pages():
        await msg.answer(f"{f}\nBizning ijtimoiy tarmoqlar:\nOur social networks:\n<a href='https://t.me/dramaticEng'>Telegram</a>  |  <a href='https://www.youtube.com/channel/UCtHZPqD5u4MlzPRABEuFtjw'>YouTube</a>", parse_mode='html', reply_markup=next2, disable_web_page_preview=True)
    else:
        await msg.answer(f"{f}\nBizning ijtimoiy tarmoqlar:\nOur social networks:\n<a href='https://t.me/dramaticEng'>Telegram</a>  |  <a href='https://www.youtube.com/channel/UCtHZPqD5u4MlzPRABEuFtjw'>YouTube</a>", parse_mode='html', disable_web_page_preview=True)



@dp.callback_query_handler(text='next' , state=get_about.search)
async def al(call: types.CallbackQuery, state: FSMContext):
    try:
        films = db.sorted_movie()
        obj = Paginator(films, 20)
        get_pages = await state.get_data()
        page = get_pages.get('page')
        t = obj.page(page)
        if t.has_next():
            page1 = page + 1
            await state.update_data(
                {
                    'page' : page1
                }
            )
        f = ""
        get_pages = await state.get_data()
        page = get_pages.get('page')
        for film in obj.page(page).object_list:
            if film[1] == None:
                f += f'<a href="{film[3]}">{film[0]}</a>\n'
            else:
                f += f'<a href="{film[3]}">{film[0]}</a>  -  {film[1]}\n'
        t = obj.page(page)
        if t.has_next() and t.has_previous():
            await call.message.edit_text(f"\n{f}\nBizning ijtimoiy tarmoqlar:\nOur social networks:\n<a href='https://t.me/dramaticEng'>Telegram</a>  |  <a href='https://www.youtube.com/channel/UCtHZPqD5u4MlzPRABEuFtjw'>YouTube</a>",parse_mode='html', disable_web_page_preview=True)
            await call.message.edit_reply_markup(reply_markup=back_next)
        elif t.has_next():
            await call.message.edit_text(f"{f}\nBizning ijtimoiy tarmoqlar:\nOur social networks:\n<a href='https://t.me/dramaticEng'>Telegram</a>  |  <a href='https://www.youtube.com/channel/UCtHZPqD5u4MlzPRABEuFtjw'>YouTube</a>",parse_mode='html', disable_web_page_preview=True)
            await call.message.edit_reply_markup(reply_markup=next2)
        elif t.has_previous():
            await call.message.edit_text(f"{f}\nBizning ijtimoiy tarmoqlar:\nOur social networks:\n<a href='https://t.me/dramaticEng'>Telegram</a>  |  <a href='https://www.youtube.com/channel/UCtHZPqD5u4MlzPRABEuFtjw'>YouTube</a>",parse_mode='html', disable_web_page_preview=True)
            await call.message.edit_reply_markup(reply_markup=back)
    except:
        await call.message.answer("⚠️⚠️⚠️\n/movie_list buyrug'ini yuboring")
    

@dp.callback_query_handler(text='back' , state=get_about.search)
async def al(call: types.CallbackQuery, state: FSMContext):
    try:
        films = db.sorted_movie()
        obj = Paginator(films, 20)
        get_pages = await state.get_data()
        page = get_pages.get('page')
        t = obj.page(page)
        if t.has_previous():
            page1 = page - 1
            await state.update_data(
                {
                    'page' : page1
                }
            )
        f = ""
        get_pages = await state.get_data()
        page = get_pages.get('page')
        for film in obj.page(page).object_list:
            if film[1] == None:
                f += f'<a href="{film[3]}">{film[0]}</a>\n'
            else:
                f += f'<a href="{film[3]}">{film[0]}</a>  -  {film[1]}\n'
        t = obj.page(page)
        if t.has_next() and t.has_previous():
            await call.message.edit_text(f"{f}\nBizning ijtimoiy tarmoqlar:\nOur social networks:\n<a href='https://t.me/dramaticEng'>Telegram</a>  |  <a href='https://www.youtube.com/channel/UCtHZPqD5u4MlzPRABEuFtjw'>YouTube</a>",parse_mode='html', disable_web_page_preview=True)
            await call.message.edit_reply_markup(reply_markup=back_next)
        elif t.has_next():
            await call.message.edit_text(f"{f}\nBizning ijtimoiy tarmoqlar:\nOur social networks:\n<a href='https://t.me/dramaticEng'>Telegram</a>  |  <a href='https://www.youtube.com/channel/UCtHZPqD5u4MlzPRABEuFtjw'>YouTube</a>",parse_mode='html', disable_web_page_preview=True)
            await call.message.edit_reply_markup(reply_markup=next2)
        elif t.has_previous():
            await call.message.edit_text(f"{f}\nBizning ijtimoiy tarmoqlar:\nOur social networks:\n<a href='https://t.me/dramaticEng'>Telegram</a>  |  <a href='https://www.youtube.com/channel/UCtHZPqD5u4MlzPRABEuFtjw'>YouTube</a>",parse_mode='html', disable_web_page_preview=True)
            await call.message.edit_reply_markup(reply_markup=back)
    except:
        await call.message.answer("⚠️⚠️⚠️\n/movie_list buyrug'ini yuboring")






# @dp.message_handler(commands=['movie_list'], state=get_about.search)
# async def al(msg: types.Message):
#     films = db.sorted_movie()
#     n = db.count_movies()[0]
#     f = ""
#     for film in films:
#         if film[1] == None:
#             f += f'<a href="{film[3]}">{film[0]}</a>\n'
#         else:
#             f += f'<a href="{film[3]}">{film[0]}</a>  -  {film[1]}\n'
#     await msg.answer(f, parse_mode='html', disable_web_page_preview=True)
