from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

next2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton('Keyingi sahifa', callback_data='next')]
    ]
)

back_next = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton('Oldingi sahifa', callback_data='back'), InlineKeyboardButton('Keyingi sahifa', callback_data='next')]
    ]
)
back = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton('Oldingi sahifa', callback_data='back')]
    ]
)

back2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton('Bosh menyu', callback_data='main menu')]
    ]
)


allow = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton('Bekor qilmoq ❌', callback_data='main menu'), InlineKeyboardButton('Yuborish ✅', callback_data='send')]
    ]
)
