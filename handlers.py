from aiogram import types, F, Router
from aiogram.types import Message, FSInputFile, ContentType
from aiogram.filters import Command

import config
import keyboard


router = Router()


@router.message(Command(commands=["start"]))
async def start_handler(message: Message) -> None:
    """ Process /start command. Sends start message

    Args:
        message (Message): Object represents a message
    """
    await message.answer(config.START_MESSAGE)


@router.message(Command(commands=["menu"]))
async def menu(message: Message) -> None:
    """ Process /menu command. Sends keyboard and help text

    Args:
        message (Message): Object represents a message
    """
    await message.answer(config.CHOOSE_VOICE_TEXT, reply_markup=keyboard.menu)
    
@router.message(Command(commands=["next_step"]))
async def menu(message: Message) -> None:
    """ Process /next_step command

    Args:
        message (Message): Object represents a message
    """
    await message.answer(config.NEXT_STEP_TEXT)
    
    
@router.message(F.text.lower() == "селфи")
async def selfie(message: Message) -> None:
    """ Sends my selfie

    Args:
        message (Message): Process /next_step command
    """
    await message.answer_photo(config.SELFIE_URL)   
    
    
@router.message(F.text.lower() == "старшая школа")
async def hight_school(message: Message) -> None:
    """ Sends my cool photo

    Args:
        message (Message): Process /next_step command
    """
    await message.answer(config.HIGHT_SCHOOL_TEXT)  
    await message.answer_photo(config.HIGH_SCHOOL)     
    
    
@router.message(F.text.lower() == "увлечение")
async def hobby(message: Message) -> None:
    """ Sends text about by hobby

    Args:
        message (Message): Process /next_step command
    """
    await message.answer(config.HOBBY_TEXT) 
    

@router.callback_query(F.data == "grandma_GPT")
async def babushka(callback: types.CallbackQuery) -> None:
    """ Sends voice with gpt explanation

    Args:
        callback (types.CallbackQuery): Object represents an incoming callback query from a callback button in an inline keyboard
    """
    voice = FSInputFile(config.BABUSHKA)
    await callback.message.answer_voice(voice=voice)
    

@router.callback_query(F.data == "sql_nosql")
async def sql_nosql(callback: types.CallbackQuery) -> None:
    """ Sends voice with sql nosql speech

    Args:
        callback (types.CallbackQuery): Object represents an incoming callback query from a callback button in an inline keyboard
    """
    voice = FSInputFile(config.SQL)
    await callback.message.answer_voice(voice=voice)
     
    
@router.callback_query(F.data == "love_story")
async def love_story(callback: types.CallbackQuery) -> None:
    """ Sends voice with my love story

    Args:
        callback (types.CallbackQuery): Object represents an incoming callback query from a callback button in an inline keyboard
    """
    voice = FSInputFile(config.LOVE_STORY)
    await callback.message.answer_voice(voice=voice)
    
    
@router.callback_query(F.data == "git_rep")
async def git_rep(callback: types.CallbackQuery) -> None:
    """ Sends this project url

    Args:
        callback (types.CallbackQuery): Object represents an incoming callback query from a callback button in an inline keyboard
    """
    await callback.message.answer(config.REP_URL)
    



