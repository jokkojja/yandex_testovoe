from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import config
menu = [
    [InlineKeyboardButton(text=config.BABUSHKA_TEXT, callback_data="grandma_GPT")],
    [InlineKeyboardButton(text=config.SQL_TEXT, callback_data="sql_nosql")],
    [InlineKeyboardButton(text=config.LOVE_TEXT, callback_data="love_story")],
    [InlineKeyboardButton(text=config.REP_TEXT, callback_data="git_rep")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)