from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from create_bot import bot, dp, p2p
from keyboards import kb_client, tov_line_fut_uch, tov_line_fut_pent, tov_line_fut_stal, tov_line_tol_uch,\
    tov_line_tol_pent, korzina_kb, kupit_fut_uch_kb, kupit_fut_pent_kb, kupit_fut_stal_kb, kupit_tol_uch_kb, kupit_tol_pent_kb, fut_ili_tol,\
    vibor_merch_fut, vibor_merch_tol
import string
import sqlite3


items={'fut_uch':{'nameXS':'Футболка Учение XS', 'price':1937, 'nameS':'Футболка Учение S',
                  'nameM':'Футболка Учение М', 'nameL':'Футболка Учение L', 'nameXL':'Футболка Учение XL', 'name2XL':'Футболка Учение 2XL',
                  'name3XL':'Футболка Учение 3XL', 'name4XL':'Футболка Учение 4XL', 'name5XL':'Футболка Учение 5XL'},

       'fut_pent':{'nameXS':'Футболка Пентаграмма XS', 'price':1937, 'nameS':'Футболка Пентаграмма S',
                  'nameM':'Футболка Пентаграмма М', 'nameL':'Футболка Пентаграмма L', 'nameXL':'Футболка Пентаграмма XL', 'name2XL':'Футболка Пентаграмма 2XL',
                  'name3XL':'Футболка Пентаграмма 3XL', 'name4XL':'Футболка Пентаграмма 4XL', 'name5XL':'Футболка Пентаграмма 5XL'},

       'fut_stal':{'nameXS':'Футболка Сталинеш XS', 'price':1937, 'nameS':'Футболка Сталинеш S',
                  'nameM':'Футболка Сталинеш М', 'nameL':'Футболка Сталинеш L', 'nameXL':'Футболка Сталинеш XL', 'name2XL':'Футболка Сталинеш 2XL',
                  'name3XL':'Футболка Сталинеш 3XL', 'name4XL':'Футболка Сталинеш 4XL', 'name5XL':'Футболка Сталинеш 5XL'},

       'tol_uch':{'nameS':'Худи Учение S','nameM':'Худи Учение М', 'nameL':'Худи Учение L',
                  'nameXL':'Худи Учение XL', 'name2XL':'Худи Учение 2XL','name3XL':'Худи Учение 3XL',
                  'name4XL':'Худи Учение 4XL', 'name5XL':'Худи Учение 5XL', 'price':4000},

       'tol_pent':{'nameS':'Худи Пентаграмма S','nameM':'Худи Пентаграмма М', 'nameL':'Худи Пентаграмма L',
                  'nameXL':'Худи Пентаграмма XL', 'name2XL':'Худи Пентаграмма 2XL','name3XL':'Худи Пентаграмма 3XL',
                  'name4XL':'Худи Пентаграмма 4XL', 'name5XL':'Худи Пентаграмма 5XL', 'price':4000}}

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    # connect = sqlite3.connect('korzina_dh.db')
    # cursor = connect.cursor()
    # # cursor.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER UNIQUE, name TEXT)')
    # # cursor.execute('CREATE TABLE IF NOT EXISTS cart(user_id INTEGER, product_id INTEGER)')
    # # cursor.execute('CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price INTEGER)')
    # cursor.execute('INSERT INTO korzina(user_id, item) VALUES (?, ?)', [message.from_user.id, message.chat.first_name])
    # cursor.close()
    # connect.commit()
    # connect.close()
    await bot.send_photo(message.from_user.id, types.InputFile(r'src\photo_menu.jpg'),
                         caption='Привет! Это бот для заказа футболок и худи от издательства DHARMA1937. Перед заказом прочти, пожалуйста, дисклеймер', reply_markup=kb_client)


# @dp.message_handler(commands=['Открыть_каталог'])
async def katalog(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выбери мерч', reply_markup=fut_ili_tol)

# @dp.message_handler(commands=['Обратная_связь'])
async def obr_svyaz(message : types.Message):
    await bot.send_message(message.from_user.id, 'Контакты обратной связи')

# @dp.message_handler(commands=['Корзина'])
async def korzina(message : types.Message):
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    tovari = cursor.execute('SELECT item FROM korzina WHERE user_id=(?)', [message.from_user.id]).fetchall()
    ceni = cursor.execute('SELECT price FROM korzina WHERE user_id=(?)', [message.from_user.id]).fetchall()
    ItemsWithoutTuple = [i[0] for i in tovari]
    toviki = ', '.join(ItemsWithoutTuple)
    CeniWithoutTuple = [i[0] for i in ceni]
    cennik = [int(item) for item in CeniWithoutTuple]
    global sum_cennik
    sum_cennik = sum(cennik)
    cursor.close()
    connect.commit()
    await bot.send_message(message.from_user.id, f'Ваши товары: {toviki}\nЦены: {sum_cennik}руб.', reply_markup=korzina_kb)

@dp.callback_query_handler(text='futbolki')
async def futbolki(callback_query : types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Футболки', reply_markup=vibor_merch_fut)

@dp.callback_query_handler(text='tolstovki')
async def futbolki(callback_query : types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Худи', reply_markup=vibor_merch_tol)


# колбэки для ФУТБОЛКИ УЧЕНИЕ
@dp.callback_query_handler(text='kupit_fut_uch_xs')
async def kupit_fut_uch(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_uch']['nameXS']
    product_price = items['fut_uch']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Учение XS добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_uch_s')
async def kupit_fut_uch(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_uch']['nameS']
    product_price = items['fut_uch']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Учение S добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_uch_m')
async def kupit_fut_uch(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_uch']['nameM']
    product_price = items['fut_uch']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Учение M добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_uch_l')
async def kupit_fut_uch(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_uch']['nameL']
    product_price = items['fut_uch']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Учение L добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_uch_xl')
async def kupit_fut_uch(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_uch']['nameXL']
    product_price = items['fut_uch']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Учение XL добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_uch_2xl')
async def kupit_fut_uch(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_uch']['name2XL']
    product_price = items['fut_uch']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Учение 2XL добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_uch_3xl')
async def kupit_fut_uch(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_uch']['name3XL']
    product_price = items['fut_uch']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Учение 3XL добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_uch_4xl')
async def kupit_fut_uch(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_uch']['name4XL']
    product_price = items['fut_uch']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Учение 4XL добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_uch_5xl')
async def kupit_fut_uch(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_uch']['name5XL']
    product_price = items['fut_uch']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Учение 5XL добавлена в корзину')


# колбэки для ФУТБОЛКИ ПЕНТАГРАММА
@dp.callback_query_handler(text='kupit_fut_pent_xs')
async def kupit_fut_pent(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_pent']['nameXS']
    product_price = items['fut_pent']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Пентаграмма XS добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_pent_s')
async def kupit_fut_pent(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_pent']['nameS']
    product_price = items['fut_pent']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Пентаграмма S добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_pent_m')
async def kupit_fut_pent(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_pent']['nameM']
    product_price = items['fut_pent']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Пентаграмма M добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_pent_l')
async def kupit_fut_pent(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_pent']['nameL']
    product_price = items['fut_pent']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Пентаграмма L добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_pent_xl')
async def kupit_fut_pent(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_pent']['nameXL']
    product_price = items['fut_pent']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Пентаграмма XL добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_pent_2xl')
async def kupit_fut_pent(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_pent']['name2XL']
    product_price = items['fut_pent']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Пентаграмма 2XL добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_pent_3xl')
async def kupit_fut_pent(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_pent']['name3XL']
    product_price = items['fut_pent']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Пентаграмма 4XL добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_pent_4xl')
async def kupit_fut_pent(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_pent']['name4XL']
    product_price = items['fut_pent']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Пентаграмма 4XL добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_pent_5xl')
async def kupit_fut_pent(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_pent']['name5XL']
    product_price = items['fut_pent']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Пентаграмма 5XL добавлена в корзину')


# колбэки ФУТБОЛКИ СТАЛИНЕШ
@dp.callback_query_handler(text='kupit_fut_stal_xs')
async def kupit_fut_stal(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_stal']['nameXS']
    product_price = items['fut_stal']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Сталинеш XS добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_stal_s')
async def kupit_fut_stal(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_stal']['nameS']
    product_price = items['fut_stal']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Сталинеш S добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_stal_m')
async def kupit_fut_stal(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_stal']['nameM']
    product_price = items['fut_stal']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Сталинеш M добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_stal_l')
async def kupit_fut_stal(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_stal']['nameL']
    product_price = items['fut_stal']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Сталинеш L добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_stal_xl')
async def kupit_fut_stal(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_stal']['nameXL']
    product_price = items['fut_stal']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Сталинеш XL добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_stal_2xl')
async def kupit_fut_stal(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_stal']['name2XL']
    product_price = items['fut_stal']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Сталинеш 2XL добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_stal_3xl')
async def kupit_fut_stal(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_stal']['name3XL']
    product_price = items['fut_stal']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Сталинеш 3XL добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_stal_4xl')
async def kupit_fut_stal(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_stal']['name4XL']
    product_price = items['fut_stal']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Сталинеш 4XL добавлена в корзину')

@dp.callback_query_handler(text='kupit_fut_stal_5xl')
async def kupit_fut_stal(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['fut_stal']['name5XL']
    product_price = items['fut_stal']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Футболка Сталинеш 5XL добавлена в корзину')


# колбэки ХУДИ УЧЕНИЕ
@dp.callback_query_handler(text='kupit_tol_uch_s')
async def kupit_tol_uch(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['tol_uch']['nameS']
    product_price = items['tol_uch']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Худи Учение S добавлено в корзину')

@dp.callback_query_handler(text='kupit_tol_uch_m')
async def kupit_tol_uch(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['tol_uch']['nameM']
    product_price = items['tol_uch']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Худи Учение M добавлено в корзину')

@dp.callback_query_handler(text='kupit_tol_uch_l')
async def kupit_tol_uch(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['tol_uch']['nameL']
    product_price = items['tol_uch']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Худи Учение L добавлено в корзину')

@dp.callback_query_handler(text='kupit_tol_uch_xl')
async def kupit_tol_uch(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['tol_uch']['nameXL']
    product_price = items['tol_uch']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Худи Учение XL добавлено в корзину')

@dp.callback_query_handler(text='kupit_tol_uch_2xl')
async def kupit_tol_uch(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['tol_uch']['name2XL']
    product_price = items['tol_uch']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Худи Учение 2XL добавлено в корзину')

@dp.callback_query_handler(text='kupit_tol_uch_3xl')
async def kupit_tol_uch(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['tol_uch']['name3XL']
    product_price = items['tol_uch']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Худи Учение 3XL добавлено в корзину')

@dp.callback_query_handler(text='kupit_tol_uch_4xl')
async def kupit_tol_uch(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['tol_uch']['name4XL']
    product_price = items['tol_uch']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Худи Учение 4XL добавлено в корзину')

@dp.callback_query_handler(text='kupit_tol_uch_5xl')
async def kupit_tol_uch(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['tol_uch']['name5XL']
    product_price = items['tol_uch']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Худи Учение 5XL добавлено в корзину')

# колбэки ХУДИ ПЕНТАГРАММА
@dp.callback_query_handler(text='kupit_tol_pent_s')
async def kupit_tol_pent(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['tol_pent']['nameS']
    product_price = items['tol_pent']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Худи Пентаграмма S добавлено в корзину')

@dp.callback_query_handler(text='kupit_tol_pent_m')
async def kupit_tol_pent(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['tol_pent']['nameM']
    product_price = items['tol_pent']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Худи Пентаграмма M добавлено в корзину')

@dp.callback_query_handler(text='kupit_tol_pent_l')
async def kupit_tol_pent(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['tol_pent']['nameL']
    product_price = items['tol_pent']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Худи Пентаграмма L добавлено в корзину')

@dp.callback_query_handler(text='kupit_tol_pent_xl')
async def kupit_tol_pent(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['tol_pent']['nameXL']
    product_price = items['tol_pent']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Худи Пентаграмма XL добавлено в корзину')

@dp.callback_query_handler(text='kupit_tol_pent_2xl')
async def kupit_tol_pent(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['tol_pent']['name2XL']
    product_price = items['tol_pent']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Худи Пентаграмма 2XL добавлено в корзину')

@dp.callback_query_handler(text='kupit_tol_pent_3xl')
async def kupit_tol_pent(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['tol_pent']['name3XL']
    product_price = items['tol_pent']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Худи Пентаграмма 3XL добавлено в корзину')

@dp.callback_query_handler(text='kupit_tol_pent_4xl')
async def kupit_tol_pent(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['tol_pent']['name4XL']
    product_price = items['tol_pent']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Худи Пентаграмма 4XL добавлено в корзину')

@dp.callback_query_handler(text='kupit_tol_pent_5xl')
async def kupit_tol_pent(callback_query : types.CallbackQuery):
    await callback_query.answer(cache_time=10)
    product = items['tol_pent']['name5XL']
    product_price = items['tol_pent']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    # await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    await callback_query.message.answer('Худи Пентаграмма 5XL добавлено в корзину')


# @dp.callback_query_handler(cb.filter(id='2'))
# async def kupit_fut_uch(callback_query : types.CallbackQuery, callback_data : dict):
#     await callback_query.answer(cache_time=10)
#
#     product = items['fut_pent']['name']
#     product_price = items['fut_pent']['price']
#     user_id = callback_query.from_user.id
#     connect = sqlite3.connect('korzina_dh.db')
#     cursor = connect.cursor()
#     cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', [user_id, product, product_price])
#     cursor.close()
#     connect.commit()
#     connect.close()
#
#     await callback_query.message.answer('Футболка Пентаграмма добавлена в корзину')
#
#
#
# @dp.callback_query_handler(cb.filter(id='3'))
# async def kupit_fut_uch(callback_query : types.CallbackQuery, callback_data : dict):
#     await callback_query.answer(cache_time=10)
#
#     product = items['fut_stal']['name']
#     product_price = items['fut_stal']['price']
#     user_id = callback_query.from_user.id
#     connect = sqlite3.connect('korzina_dh.db')
#     cursor = connect.cursor()
#     cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', [user_id, product, product_price])
#     cursor.close()
#     connect.commit()
#     connect.close()
#
#     await callback_query.message.answer('Футболка Сталинеш добавлена в корзину')
#
# @dp.callback_query_handler(cb.filter(id='4'))
# async def kupit_fut_uch(callback_query : types.CallbackQuery, callback_data : dict):
#     await callback_query.answer(cache_time=10)
#
#     product = items['tol_uch']['name']
#     product_price = items['tol_uch']['price']
#     user_id = callback_query.from_user.id
#     connect = sqlite3.connect('korzina_dh.db')
#     cursor = connect.cursor()
#     cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', [user_id, product, product_price])
#     cursor.close()
#     connect.commit()
#     connect.close()
#
#     await callback_query.message.answer('Худи Учение добавлена в корзину')
#
# @dp.callback_query_handler(cb.filter(id='5'))
# async def kupit_fut_uch(callback_query : types.CallbackQuery, callback_data : dict):
#     await callback_query.answer(cache_time=10)
#
#     product = items['tol_pent']['name']
#     product_price = items['tol_pent']['price']
#     user_id = callback_query.from_user.id
#     connect = sqlite3.connect('korzina_dh.db')
#     cursor = connect.cursor()
#     cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', [user_id, product, product_price])
#     cursor.close()
#     connect.commit()
#     connect.close()
#
#     await callback_query.message.answer('Худи Пентаграмма добавлена в корзину')




# @dp.message_handler(Command('Kupit'))
# async def kupit(message : types.Message):
#     connect = sqlite3.connect('korzina.db')
#     cursor = connect.cursor()
#     data = cursor.execute('SELECT * FROM cart WHERE user_id=(?)', [message.from_user.id]).fetchall()
#     data_tovary = cursor.execute('SELECT product_id FROM cart WHERE user_id=(?)', [message.from_user.id]).fetchall()
#     cursor.close()
#     connect.commit()
#     cursor = connect.cursor()
#     new_data = []
#     for i in range(len(data)):
#         new_data.append(cursor.execute('SELECT * FROM products WHERE id=(?)', [data[i][1]]).fetchall())
#     cursor.close()
#     connect.commit()
#     connect.close()
#     new_data = [new_data[i][0] for i in range(len(new_data))]
#     prices = [types.labeled_price.LabeledPrice(label=i[1], amount=i[2]) for i in new_data]
#     await bot.send_message(message.from_user.id, f'{data_tovary}')


@dp.callback_query_handler(text='razmer_fut')
async def razmer_fut(callback_query : types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, types.InputFile(r'src\razmer_fut.jpg'))

@dp.callback_query_handler(text='razmer_tol')
async def razmer_tol(callback_query : types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, types.InputFile(r'src\razmer_tol.jpg'))








@dp.callback_query_handler(text='fut_uch')
async def fut_uch(callback_query : types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, types.InputFile(r'src\fut_uch.jpg'), caption='Футболка Учение\n\nФутболка прямого кроя с цитатой В. Ленина из работы «Три источника и три составных части марксизма». 100% хлопок. Унисекс\n\nДоставка: 600 рублей (почта РФ). От 800 рублей в другие страны', reply_markup=kupit_fut_uch_kb)

@dp.callback_query_handler(text='fut_pent')
async def fut_uch(callback_query : types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, types.InputFile(r'src\fut_pent.jpg'), caption='Футболка Пентаграмма\n\nФутболка с портретами Маркса, Ленина, Мао, Сталина и цитатой Ленина «Учение Маркса всесильно, потому что оно верно». 100% хлопок. Унисекс\n\nДоставка: 600 рублей (почта РФ). От 800 рублей в другие страны', reply_markup=kupit_fut_pent_kb)


@dp.callback_query_handler(text='fut_stal')
async def fut_uch(callback_query : types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, types.InputFile(r'src\fut_stal.jpg'), caption='Футболка Сталинеш\n\nФутболка прямого кроя с принтом И. Сталина в образе Ганеши. 100% хлопок. Унисекс\n\nДоставка: 600 рублей (почта РФ). От 800 рублей в другие страны', reply_markup=kupit_fut_stal_kb)


@dp.callback_query_handler(text='tol_uch')
async def fut_uch(callback_query : types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, types.InputFile(r'src\tol_uch.jpg'), caption='Худи Учение\n\nХуди с цитатой В. Ленина из работы «Три источника и три составных части марксизма». Унисекс 100% хлопок.\n\nДоставка: 600 рублей (почта РФ). От 800 рублей в другие страны', reply_markup=kupit_tol_uch_kb)


@dp.callback_query_handler(text='tol_pent')
async def fut_uch(callback_query : types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, types.InputFile(r'src\tol_pent.jpg'), caption='Худи Пентаграмма\n\nХуди с портретами Маркса, Ленина, Мао, Сталина и цитатой Ленина «Учение Маркса всесильно, потому что оно верно». Унисекс. 100% хлопок\n\nДоставка: 600 рублей (почта РФ). От 800 рублей в другие страны', reply_markup=kupit_tol_pent_kb)

@dp.callback_query_handler(text='Ochistit_korzinu')
async def ochistit_korzinu(callback_query : types.CallbackQuery):
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('DELETE FROM korzina WHERE user_id=(?)', [callback_query.from_user.id])
    cursor.close()
    connect.commit()
    connect.close()
    await bot.send_message(callback_query.from_user.id, 'Ваша корзина очищена')

@dp.callback_query_handler(text='Oformit_zakaz')
async def oformit_zakaz(callback_query : types.CallbackQuery):
    new_bill = await p2p.bill(amount=sum_cennik, lifetime=45)
    await bot.send_message(callback_query.from_user.id, new_bill.pay_url)
    if (await p2p.check(bill_id=new_bill.bill_id)).status is True:
        await bot.send_message(callback_query.from_user.id, 'Ваш заказ оплачен')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(katalog, commands=['Открыть_каталог'])
    dp.register_message_handler(obr_svyaz, commands=['Обратная_связь'])
    dp.register_message_handler(korzina, commands=['Корзина'])





