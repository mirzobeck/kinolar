from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Kino qo'shish"), KeyboardButton('Kino olib tashlash')],
        [KeyboardButton("Kanal qo'shish"), KeyboardButton('Kanal olib tashlash')],
        [KeyboardButton('Reklama tarqatish')]
    ], resize_keyboard=True, one_time_keyboard=True
)

btn2 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Kino qo'shish"), KeyboardButton('Kino olib tashlash')],
        [KeyboardButton("Kanal qo'shish"), KeyboardButton('Reklama tarqatish')]
    ], resize_keyboard=True, one_time_keyboard=True
)

next = ReplyKeyboardMarkup(
    keyboard=[
        ['Keyingisi']
    ], resize_keyboard=True, one_time_keyboard=True
)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton('Bosh menyu')]
    ], resize_keyboard=True, one_time_keyboard=True
)

rek_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Video 📹"), KeyboardButton('Foto 📷')],
        [KeyboardButton("Xabar ✍🏻"), KeyboardButton('Bosh menyu')]
    ], resize_keyboard=True, one_time_keyboard=True
)