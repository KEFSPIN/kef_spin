import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums import ParseMode
from api.utils import check_subscription

TOKEN = "7542181325:AAGvpHUXgPTWRadQid_ZtN1iUOodzqWcfkg"
CHANNEL_USERNAME = "@shopkefira"

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message()
async def start(message: types.Message):
    if not await check_subscription(bot, message.from_user.id, CHANNEL_USERNAME):
        return await message.answer("Щоб грати в рулетку, підпишись на канал: https://t.me/shopkefira")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="🎯 Крутити рулетку", web_app=types.WebAppInfo(url="https://yourdomain.com/roulette"))
    ]])
    await message.answer("Ласкаво просимо в KEF_SPIN!", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
