import shutil
from datetime import datetime
from itertools import zip_longest

from aiogram import types, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from detection_text.detect_text import get_price_from_photo, get_converted_price, get_description_from_photo, \
    convert_to_rubles_and_kop
from split_photo.splitter import get_split_nikora, get_split_universami
import os


async def message_get_photo_nikora(message: types.Message, state: FSMContext):
    print('Фото принято')
    await message.photo[-1].download('/Users/kseniiamurasheva/PycharmProjects/PriceBot/Photos/photo.jpg')

    if os.path.isdir('/Users/kseniiamurasheva/PycharmProjects/PriceBot/runs'):
        # Если файл существует, удалить его
        shutil.rmtree('/Users/kseniiamurasheva/PycharmProjects/PriceBot/runs')

    get_split_nikora('Photos/photo.jpg')

    prices = []
    descriptions = []

    if os.path.isdir('/Users/kseniiamurasheva/PycharmProjects/PriceBot/runs/detect/exp/crops/price'):
        for photo in os.listdir('/Users/kseniiamurasheva/PycharmProjects/PriceBot/runs/detect/exp/crops/price'):
            one_price = []
            price_url = '/Users/kseniiamurasheva/PycharmProjects/PriceBot/runs/detect/exp/crops/price/'+photo
            price = get_price_from_photo(price_url)
            one_price.append(price)
            if price:
                price = get_converted_price(price)
                rub, kop = convert_to_rubles_and_kop(price)
                one_price.append(f'{rub} руб. {kop} коп.')
            else:
                one_price.append('непонятно')
            prices.append(one_price)

    if os.path.isdir('/Users/kseniiamurasheva/PycharmProjects/PriceBot/runs/detect/exp/crops/description'):
        for description in os.listdir('/Users/kseniiamurasheva/PycharmProjects/PriceBot/runs/detect/exp/crops/description'):
            description_url = '/Users/kseniiamurasheva/PycharmProjects/PriceBot/runs/detect/exp/crops/description/'+description
            description = get_description_from_photo(description_url)
            if description:
                descriptions.append(description)
            else:
                descriptions.append('непонятно')

    for pair in prices:
        if pair[0]:
            await message.answer(f'💰{pair[0].strip()} лар. — это <b>{pair[1].strip()}</b> по актуальному курсу.')

    for desc in descriptions:
        await message.answer(f'Это название товара — {desc.strip()}. Если хочешь его перевести, просто выдели его и выбери «Перевести» (убедись, что эта возможность включена в настройках телеграма)')
    await message.answer(f'Смени магазин через кнопку Menu или отправь ценник из прежнего магазина')

async def message_get_photo_universami(message: types.Message, state: FSMContext):
    print('Фото принято')
    await message.photo[-1].download('/Users/kseniiamurasheva/PycharmProjects/PriceBot/Photos/photo.jpg')

    if os.path.isdir('/Users/kseniiamurasheva/PycharmProjects/PriceBot/runs'):
        # Если файл существует, удалить его
        shutil.rmtree('/Users/kseniiamurasheva/PycharmProjects/PriceBot/runs')

    get_split_universami('Photos/photo.jpg')

    prices = []
    descriptions = []

    if os.path.isdir('/Users/kseniiamurasheva/PycharmProjects/PriceBot/runs/detect/exp/crops/price'):
        for photo in os.listdir('/Users/kseniiamurasheva/PycharmProjects/PriceBot/runs/detect/exp/crops/price'):
            one_price = []
            price_url = '/Users/kseniiamurasheva/PycharmProjects/PriceBot/runs/detect/exp/crops/price/'+photo
            price = get_price_from_photo(price_url)
            one_price.append(price)
            if price:
                price = get_converted_price(price)
                rub, kop = convert_to_rubles_and_kop(price)
                one_price.append(f'{rub} руб. {kop} коп.')
            else:
                one_price.append('непонятно')
            prices.append(one_price)

    if os.path.isdir('/Users/kseniiamurasheva/PycharmProjects/PriceBot/runs/detect/exp/crops/description'):
        for description in os.listdir('/Users/kseniiamurasheva/PycharmProjects/PriceBot/runs/detect/exp/crops/description'):
            description_url = '/Users/kseniiamurasheva/PycharmProjects/PriceBot/runs/detect/exp/crops/description/'+description
            description = get_description_from_photo(description_url)
            if description:
                descriptions.append(description)
            else:
                descriptions.append('непонятно')

    for pair in prices:
        if pair[0]:
            await message.answer(f'💰{pair[0].strip()} лар. — это <b>{pair[1].strip()}</b> по актуальному курсу.')

    for desc in descriptions:
        await message.answer(f'Это название товара — {desc.strip()}. Если хочешь его перевести, просто выдели его и выбери «Перевести» (убедись, что эта возможность включена в настройках телеграма)')

    await message.answer(f'Смени магазин через кнопку Menu или отправь ценник из прежнего магазина')