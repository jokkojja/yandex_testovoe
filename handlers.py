from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
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
                      Также есть вариант выбрать что-нибудь из меню. Для этого просто напиши 'Меню'")


@router.message(F.text == "Меню")
async def menu(message: Message) -> None:
    """_summary_

    Args:
        message (Message): _description_
    """
    await message.answer('Выбирай о чем хочешь послушать войс:', reply_markup=keyboard.menu)
    
    
@router.message(F.text == "Селфи")
async def menu(message: Message) -> None:
    """_summary_

    Args:
        message (Message): _description_
    """
    await message.answer('Селфи')   
    
    
@router.message(F.text == "Старшая школа")
async def menu(message: Message) -> None:
    """_summary_

    Args:
        message (Message): _description_
    """
    await message.answer('Старшая школа')     
    
    
@router.message(F.text == "Увлечение")
async def menu(message: Message) -> None:
    """_summary_

    Args:
        message (Message): _description_
    """
    await message.answer('Увлечение')      