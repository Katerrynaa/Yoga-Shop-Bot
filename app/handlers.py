from aiogram import Router, F

from aiogram.types import Message,CallbackQuery
from aiogram.filters import CommandStart

import app.keyboards as kb 
import app.database.requests as rq


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await  rq.set_user(message.from_user.id)
    await message.answer("Hello! Welcome to the shop!", reply_markup=kb.main)



@router.message(F.text == 'Catalog')
async def catalog(message: Message):
    await message.answer("Select product category", reply_markup=await kb.categories())


@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.message.answer("Choose item by category", reply_markup= await kb.items(callback.data.split('_')[1] ))



@router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.message.answer(f'Your item is: {item_data.name}\nDescription: {item_data.description}\nPrice: {item_data.price}$', 
                                  reply_markup= await kb.items(callback.data.split('_')[1] ))








