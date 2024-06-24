from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)

from app.database.requests import get_category, get_item_by_category
from aiogram.utils.keyboard import InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Catalog')],
                                     [KeyboardButton(text='Basket')],
                                     [KeyboardButton(text='Contact'),
                                      KeyboardButton(text='About us')]],
                            resize_keyboard=True)


async def categories():
    all_categories = await get_category()
    keyboard = InlineKeyboardBuilder()

    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f'category_{category.id}'))
    keyboard.add(InlineKeyboardButton(text='Main page', callback_data='main'))
    return keyboard.adjust(2).as_markup()


async def items(category_id):
    all_items = await get_item_by_category(category_id)
    keyboard = InlineKeyboardBuilder()

    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f'item_{item.id}'))
    keyboard.add(InlineKeyboardButton(text='Main page', callback_data='main'))
    return keyboard.adjust(2).as_markup()








# from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                        #    InlineKeyboardButton, InlineKeyboardMarkup)


# catalog = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='T-shirts', callback_data='t-shirts')],
#     [InlineKeyboardButton(text='Jeans', callback_data='jeans')],
#     [InlineKeyboardButton(text='Sneakers', callback_data='sneakers')],
#     [InlineKeyboardButton(text='Sweaters', callback_data='sweaters')]])


# get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Send a number', 
#                                                            request_contact=True)]],
#                                                            resize_keyboard=True)