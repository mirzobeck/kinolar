import logging
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from data.config import CHANNELS
from utils.misc import subscription
from loader import bot, db


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            user = update.message.from_user.id
            if update.message.text in ['/start',]:
                return
        else:
            return
        logging.info(user)
        result = "⚠️⚠️⚠️👇🏻\n"
        final_status = True
        for channel in db.get_channel():
            status = await subscription.check(user_id=user,
                                              channel=channel[0])
            final_status *= status
            channel = await bot.get_chat(channel[0])
            if not status:
                invite_link = await channel.export_invite_link()
                result += (f"❌ <a href='{invite_link}'><b>{channel.title}</b></a>\n")
                
        if not final_status:
            await update.message.answer(f"{result}\nUlanib bo'lgach qayta /start tugmasini bosing!", disable_web_page_preview=True)
            raise CancelHandler()