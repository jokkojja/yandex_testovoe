from aiogram import types, F, Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

import config
import keyboard


router = Router()


@router.message(Command(commands=["start"]))
async def start_handler(message: Message) -> None:
    """_summary_

    Args:
        message (Message): _description_
    """
    await message.answer("Привет! Я помогу тебе познакомиться со мной поближе.\
                      Если хочешь увидеть мое последнее селфи: напиши 'Селфи',\
                      если фото из старшей школы: 'Старшая школа',\
                      если хочешь узнать о моем главном увлечении: 'Увлечение'.\
                      Также есть вариант выбрать что-нибудь из меню. Для этого просто тыкни сюда /menu")


@router.message(Command(commands=["menu"]))
async def menu(message: Message) -> None:
    """_summary_

    Args:
        message (Message): _description_
    """
    await message.answer('Выбирай о чем хочешь послушать войс:', reply_markup=keyboard.menu)
    
@router.message(Command(commands=["next_step"]))
async def menu(message: Message) -> None:
    """_summary_

    Args:
        message (Message): _description_
    """
    await message.answer('Здесь что-то про следующий шаг')
    
    
@router.message(F.text == "Селфи")
async def selfie(message: Message) -> None:
    """_summary_

    Args:
        message (Message): _description_
    """
    await message.answer_photo(config.SELFIE_URL)   
    
    
@router.message(F.text == "Старшая школа")
async def hight_school(message: Message) -> None:
    """_summary_

    Args:
        message (Message): _description_
    """
    await message.answer_photo(config.HIGH_SCHOOL)     
    
    
@router.message(F.text == "Увлечение")
async def hobby(message: Message) -> None:
    """_summary_

    Args:
        message (Message): _description_
    """
    await message.answer('Тут супер текст о моем увлечении') 
    

@router.callback_query(F.data == "grandma_GPT")
async def babushka(callback: types.CallbackQuery) -> None:
    """_summary_

    Args:
        callback (types.CallbackQuery): _description_
    """
    voice = FSInputFile(config.BABUSHKA)
    await callback.message.answer_voice(voice=voice)
    

@router.callback_query(F.data == "sql_nosql")
async def babushka(callback: types.CallbackQuery) -> None:
    """_summary_

    Args:
        callback (types.CallbackQuery): _description_
    """
    voice = FSInputFile(config.SQL)
    await callback.message.answer_voice(voice=voice)
     
    
@router.callback_query(F.data == "love_story")
async def babushka(callback: types.CallbackQuery) -> None:
    """_summary_

    Args:
        callback (types.CallbackQuery): _description_
    """
    voice = FSInputFile(config.LOVE_STORY)
    await callback.message.answer_voice(voice=voice)
    
    
@router.callback_query(F.data == "git_rep")
async def babushka(callback: types.CallbackQuery) -> None:
    """_summary_

    Args:
        callback (types.CallbackQuery): _description_
    """
    await callback.message.answer(config.REP_URL)
