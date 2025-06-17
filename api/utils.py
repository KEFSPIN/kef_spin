from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest

async def check_subscription(bot: Bot, user_id: int, channel: str) -> bool:
    try:
        member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
        return member.status in ("member", "creator", "administrator")
    except TelegramBadRequest:
        return False
