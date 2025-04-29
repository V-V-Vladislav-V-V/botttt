import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = '7575261191:AAFEgmlTbahKifPtOWsFL8rt1hksYBOhQ5s'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))  # Обработчик команды `/start`
async def cmd_start(message: types.Message):
    """Обработчик команды /start"""
    # Структура первой клавиатуры
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Выбор А", callback_data="choice_a"),
         InlineKeyboardButton(text="Выбор Б", callback_data="choice_b")]
    ])
    await message.answer("Привет! Выберите один из вариантов:",
                         reply_markup=keyboard)  # Ответ пользователю с клавиатурой


@dp.callback_query(lambda cq: True)  # Обработчик любых callback-запросов
async def process_callback(callback_query: types.CallbackQuery):
    """Реакция на нажатие inline-кнопок"""
    data = callback_query.data  # Данные, присланные кнопкой (например, choice_a, confirm и др.)
    chat_id = callback_query.from_user.id  # Идентификатор чата пользователя
    message_id = callback_query.message.message_id  # Идентификатор сообщения, в котором находится кнопка

    if data == "choice_a":  # Если пользователь выбрал "Выбор А"
        # Меняем текущее сообщение
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Вы выбрали Вариант А.")

        # Новая клавиатура с возможностью возврата назад
        new_keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Подтверждение", callback_data="confirm"),
             InlineKeyboardButton(text="Отмена", callback_data="cancel")],
            [InlineKeyboardButton(text="Назад", callback_data="back")]  # Кнопка возврата
        ])
        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_keyboard)

    elif data == "choice_b":  # Если пользователь выбрал "Выбор Б"
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Вы выбрали Вариант Б.")
        new_keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Подтверждение", callback_data="confirm"),
             InlineKeyboardButton(text="Отмена", callback_data="cancel")],
            [InlineKeyboardButton(text="Назад", callback_data="back")]  # Та же кнопка "назад"
        ])
        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_keyboard)

    elif data == "back":  # Возвращаемся обратно на начальную страницу
        # Вернуть изначальное состояние (первичная клавиатура)
        back_keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Выбор А", callback_data="choice_a"),
             InlineKeyboardButton(text="Выбор Б", callback_data="choice_b")]
        ])
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Вернулись назад. Повторите выбор:")
        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=back_keyboard)

    elif data == "confirm":  # Подтверждение выбора
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Ваш выбор подтвержден!")

    elif data == "cancel":  # Отмена выбора
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Действие отменено.")


if __name__ == "__main__":  # Основная точка входа программы
    dp.run_polling(bot)  # Бот начинает постоянно запрашивать новые событи...