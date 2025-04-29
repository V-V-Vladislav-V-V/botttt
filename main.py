import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7575261191:AAFEgmlTbahKifPtOWsFL8rt1hksYBOhQ5s")
disp = Dispatcher()

@disp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="tralalelo  tralala")],
        [types.KeyboardButton(text="golubiro shpioniro")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="who is?")
    await message.answer( " who is",reply_markup=keyboard)

async def main():
    await disp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())