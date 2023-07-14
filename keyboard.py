from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
menu = [
    [InlineKeyboardButton(text="Сказ про бабушку и ChatGPT", callback_data="generate_text")],
    [InlineKeyboardButton(text="История противостояние SQL и NoSQL", callback_data="generate_image")],
    [InlineKeyboardButton(text="Лав стори", callback_data="buy_tokens")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)