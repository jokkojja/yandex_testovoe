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
    await message.answer(config.START_MESSAGE)


@router.message(Command(commands=["menu"]))
async def menu(message: Message) -> None:
    """_summary_

    Args:
        message (Message): _description_
    """
    await message.answer(config.CHOOSE_VOICE_TEXT, reply_markup=keyboard.menu)
    
@router.message(Command(commands=["next_step"]))
async def menu(message: Message) -> None:
    """_summary_

    Args:
        message (Message): _description_
    """
    await message.answer(config.NEXT_STEP_TEXT)
    
    
@router.message(F.text.lower() == "селфи")
async def selfie(message: Message) -> None:
    """_summary_

    Args:
        message (Message): _description_
    """
    await message.answer_photo(config.SELFIE_URL)   
    
    
@router.message(F.text.lower() == "старшая школа")
async def hight_school(message: Message) -> None:
    """_summary_

    Args:
        message (Message): _description_
    """
    await message.answer_photo(config.HIGH_SCHOOL)     
    
    
@router.message(F.text.lower() == "увлечение")
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
    

# @router.message_handler(content_types=[
#     types.ContentType.VOICE,
#     ])
# async def voice_to_text



