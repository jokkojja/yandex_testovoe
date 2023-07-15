from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
menu = [
    [InlineKeyboardButton(text="Сказ про бабушку и ChatGPT", callback_data="grandma_GPT")],
    [InlineKeyboardButton(text="История противостояние SQL и NoSQL", callback_data="sql_nosql")],
    [InlineKeyboardButton(text="Лав стори", callback_data="love_story")],
    [InlineKeyboardButton(text="Ссылка на реп к этому супер боту", callback_data="git_rep")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)