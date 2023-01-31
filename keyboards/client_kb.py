from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

# первичная клавиатура
katalog_btn = KeyboardButton('/Открыть_каталог')
obr_svyaz = KeyboardButton('/Обратная_связь')
korzina = KeyboardButton('/Корзина')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(katalog_btn).add(obr_svyaz).add(korzina)

# стартовые кнопки выбора мерча ФУТБОЛКИ ИЛИ ХУДИ
futbolki = InlineKeyboardButton('Футболки', callback_data='futbolki')
tolstovki = InlineKeyboardButton('Худи', callback_data='tolstovki')

fut_ili_tol = InlineKeyboardMarkup(row_width=2)
fut_ili_tol.add(futbolki).add(tolstovki)


# стартовые кнопки выбора мерча
fut_uch = InlineKeyboardButton('Футболка Учение', callback_data='fut_uch')
fut_pent = InlineKeyboardButton('Футболка Пентаграмма', callback_data='fut_pent')
fut_stal = InlineKeyboardButton('Футболка Сталинеш', callback_data='fut_stal')
tol_uch = InlineKeyboardButton('Худи Учение', callback_data='tol_uch')
tol_pent = InlineKeyboardButton('Худи Пентаграмма', callback_data='tol_pent')

vibor_merch_fut = InlineKeyboardMarkup(row_width=2)
vibor_merch_tol = InlineKeyboardMarkup(row_width=2)
vibor_merch_fut.add(fut_uch).add(fut_pent).add(fut_stal)
vibor_merch_tol.add(tol_uch).add(tol_pent)


tov_line_fut_uch = InlineKeyboardMarkup()
tov_line_fut_pent = InlineKeyboardMarkup()
tov_line_fut_stal = InlineKeyboardMarkup()
tov_line_tol_uch = InlineKeyboardMarkup()
tov_line_tol_pent = InlineKeyboardMarkup()

# cb = CallbackData('kupit', 'id')
# # кнопки 'купить' для каждого товара
# kupit_fut_uch = InlineKeyboardButton('Купить', callback_data='kupit:1')
# kupit_fut_pent = InlineKeyboardButton('Купить', callback_data='kupit:2')
# kupit_fut_stal = InlineKeyboardButton('Купить', callback_data='kupit:3')
# kupit_tol_uch = InlineKeyboardButton('Купить', callback_data='kupit:4')
# kupit_tol_pent = InlineKeyboardButton('Купить', callback_data='kupit:5')

# размеры
razmer_fut = InlineKeyboardButton('Узнать размер', callback_data='razmer_fut')
razmer_tol = InlineKeyboardButton('Узнать размер', callback_data='razmer_tol')
#
# tov_line_fut_uch.row(kupit_fut_uch, razmer_fut)
# tov_line_fut_pent.row(kupit_fut_pent, razmer_fut)
# tov_line_fut_stal.row(kupit_fut_stal, razmer_fut)
#
# tov_line_tol_uch.row(kupit_tol_uch, razmer_tol)
# tov_line_tol_pent.row(kupit_tol_pent, razmer_tol)

# кнопки для корзины
korzina_kb = InlineKeyboardMarkup(row_width=2)

Kupit = InlineKeyboardButton('Оформить заказ', callback_data='Oformit_zakaz')
Ochist_korz = InlineKeyboardButton('Очистить корзину', callback_data='Ochistit_korzinu')

korzina_kb.row(Kupit, Ochist_korz)



# кнопки ФУТБОЛКИ УЧЕНИЕ
kupit_fut_uch_xs = InlineKeyboardButton(text='xs', callback_data='kupit_fut_uch_xs')
kupit_fut_uch_s = InlineKeyboardButton(text='s', callback_data='kupit_fut_uch_s')
kupit_fut_uch_m = InlineKeyboardButton(text='m', callback_data='kupit_fut_uch_m')
kupit_fut_uch_l = InlineKeyboardButton(text='l', callback_data='kupit_fut_uch_l')
kupit_fut_uch_xl = InlineKeyboardButton(text='xl', callback_data='kupit_fut_uch_xl')
kupit_fut_uch_2xl = InlineKeyboardButton(text='2xl', callback_data='kupit_fut_uch_2xl')
kupit_fut_uch_3xl = InlineKeyboardButton(text='3xl', callback_data='kupit_fut_uch_3xl')
kupit_fut_uch_4xl = InlineKeyboardButton(text='4xl', callback_data='kupit_fut_uch_4xl')
kupit_fut_uch_5xl = InlineKeyboardButton(text='5xl', callback_data='kupit_fut_uch_5xl')

kupit_fut_uch_kb = InlineKeyboardMarkup(row_width=2)
kupit_fut_uch_kb.add(razmer_fut).row(kupit_fut_uch_xs, kupit_fut_uch_s).row(kupit_fut_uch_m, kupit_fut_uch_l).row(kupit_fut_uch_xl,
            kupit_fut_uch_2xl).row(kupit_fut_uch_3xl, kupit_fut_uch_4xl).add(kupit_fut_uch_5xl)


# кнопки ФУТБОЛКИ ПЕНТАГРАММА
kupit_fut_pent_xs = InlineKeyboardButton(text='xs', callback_data='kupit_fut_pent_xs')
kupit_fut_pent_s = InlineKeyboardButton(text='s', callback_data='kupit_fut_pent_s')
kupit_fut_pent_m = InlineKeyboardButton(text='m', callback_data='kupit_fut_pent_m')
kupit_fut_pent_l = InlineKeyboardButton(text='l', callback_data='kupit_fut_pent_l')
kupit_fut_pent_xl = InlineKeyboardButton(text='xl', callback_data='kupit_fut_pent_xl')
kupit_fut_pent_2xl = InlineKeyboardButton(text='2xl', callback_data='kupit_fut_pent_2xl')
kupit_fut_pent_3xl = InlineKeyboardButton(text='3xl', callback_data='kupit_fut_pent_3xl')
kupit_fut_pent_4xl = InlineKeyboardButton(text='4xl', callback_data='kupit_fut_pent_4xl')
kupit_fut_pent_5xl = InlineKeyboardButton(text='5xl', callback_data='kupit_fut_pent_5xl')

kupit_fut_pent_kb = InlineKeyboardMarkup(row_width=2)
kupit_fut_pent_kb.add(razmer_fut).row(kupit_fut_pent_xs, kupit_fut_pent_s).row(kupit_fut_pent_m, kupit_fut_pent_l).row(kupit_fut_pent_xl,
            kupit_fut_pent_2xl).row(kupit_fut_pent_3xl, kupit_fut_pent_4xl).add(kupit_fut_pent_5xl)

# кнопки ФУТБОЛКИ СТАЛИНЕШ
kupit_fut_stal_xs = InlineKeyboardButton(text='xs', callback_data='kupit_fut_stal_xs')
kupit_fut_stal_s = InlineKeyboardButton(text='s', callback_data='kupit_fut_stal_s')
kupit_fut_stal_m = InlineKeyboardButton(text='m', callback_data='kupit_fut_stal_m')
kupit_fut_stal_l = InlineKeyboardButton(text='l', callback_data='kupit_fut_stal_l')
kupit_fut_stal_xl = InlineKeyboardButton(text='xl', callback_data='kupit_fut_stal_xl')
kupit_fut_stal_2xl = InlineKeyboardButton(text='2xl', callback_data='kupit_fut_stal_2xl')
kupit_fut_stal_3xl = InlineKeyboardButton(text='3xl', callback_data='kupit_fut_stal_3xl')
kupit_fut_stal_4xl = InlineKeyboardButton(text='4xl', callback_data='kupit_fut_stal_4xl')
kupit_fut_stal_5xl = InlineKeyboardButton(text='5xl', callback_data='kupit_fut_stal_5xl')

kupit_fut_stal_kb = InlineKeyboardMarkup(row_width=2)
kupit_fut_stal_kb.add(razmer_fut).row(kupit_fut_stal_xs, kupit_fut_stal_s).row(kupit_fut_stal_m, kupit_fut_stal_l).row(kupit_fut_stal_xl,
            kupit_fut_stal_2xl).row(kupit_fut_stal_3xl, kupit_fut_stal_4xl).add(kupit_fut_stal_5xl)


# кнопки ХУДИ УЧЕНИЕ
kupit_tol_uch_s = InlineKeyboardButton(text='s', callback_data='kupit_tol_uch_s')
kupit_tol_uch_m = InlineKeyboardButton(text='m', callback_data='kupit_tol_uch_m')
kupit_tol_uch_l = InlineKeyboardButton(text='l', callback_data='kupit_tol_uch_l')
kupit_tol_uch_xl = InlineKeyboardButton(text='xl', callback_data='kupit_tol_uch_xl')
kupit_tol_uch_2xl = InlineKeyboardButton(text='2xl', callback_data='kupit_tol_uch_2xl')
kupit_tol_uch_3xl = InlineKeyboardButton(text='3xl', callback_data='kupit_tol_uch_3xl')
kupit_tol_uch_4xl = InlineKeyboardButton(text='4xl', callback_data='kupit_tol_uch_4xl')
kupit_tol_uch_5xl = InlineKeyboardButton(text='5xl', callback_data='kupit_tol_uch_5xl')

kupit_tol_uch_kb = InlineKeyboardMarkup(row_width=2)
kupit_tol_uch_kb.add(razmer_tol).row(kupit_tol_uch_s, kupit_tol_uch_m).row(kupit_tol_uch_l, kupit_tol_uch_xl).row(kupit_tol_uch_2xl, kupit_tol_uch_3xl).row(kupit_tol_uch_4xl, kupit_tol_uch_5xl)


# кнопки ХУДИ ПЕНТАГРАММА
kupit_tol_pent_s = InlineKeyboardButton(text='s', callback_data='kupit_tol_pent_s')
kupit_tol_pent_m = InlineKeyboardButton(text='m', callback_data='kupit_tol_pent_m')
kupit_tol_pent_l = InlineKeyboardButton(text='l', callback_data='kupit_tol_pent_l')
kupit_tol_pent_xl = InlineKeyboardButton(text='xl', callback_data='kupit_tol_pent_xl')
kupit_tol_pent_2xl = InlineKeyboardButton(text='2xl', callback_data='kupit_tol_pent_2xl')
kupit_tol_pent_3xl = InlineKeyboardButton(text='3xl', callback_data='kupit_tol_pent_3xl')
kupit_tol_pent_4xl = InlineKeyboardButton(text='4xl', callback_data='kupit_tol_pent_4xl')
kupit_tol_pent_5xl = InlineKeyboardButton(text='5xl', callback_data='kupit_tol_pent_5xl')

kupit_tol_pent_kb = InlineKeyboardMarkup(row_width=2)
kupit_tol_pent_kb.add(razmer_tol).row(kupit_tol_pent_s, kupit_tol_pent_m).row(kupit_tol_pent_l, kupit_tol_pent_xl).row(kupit_tol_pent_2xl, kupit_tol_pent_3xl).row(kupit_tol_pent_4xl, kupit_tol_pent_5xl)

