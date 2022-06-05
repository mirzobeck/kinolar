from aiogram.dispatcher.filters.state import StatesGroup, State


class get_about(StatesGroup):
    search = State()
    name = State()
    about = State()
    photo = State()
    link = State()
    delete = State()
    one_delete = State()
    channel = State()
    del_channel = State()

class rek(StatesGroup):
    turi = State()
    video = State()
    photo = State()
    capti = State()
    xabar = State()