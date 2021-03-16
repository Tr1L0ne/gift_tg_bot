from aiogram.types import ReplyKeyboardRemove, \
	ReplyKeyboardMarkup, KeyboardButton, \
	InlineKeyboardMarkup, InlineKeyboardButton

#Клавиатура (панелька)
how_to_open_case_button = KeyboardButton("Как открыть коробку?")
prizes_button = KeyboardButton("🎁 Призы 🎁")
open_case_button = KeyboardButton("Открыть коробку удачи")
my_prizes_button = KeyboardButton("Мои подарки")
buy_button = KeyboardButton("Пополнить счёт")

markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
	how_to_open_case_button).add(prizes_button).add(open_case_button).add(
	my_prizes_button).add(buy_button)

#Кнопки под сообщением
base_case = InlineKeyboardButton("Базовый Кейс", callback_data="case_1")
boyar_case = InlineKeyboardButton("Кейс для бояр", callback_data="case_2")
velmoj_case = InlineKeyboardButton("Кейс для Вельмож", callback_data="case_3")
mecenat_case = InlineKeyboardButton("Кейс для Меценатов", callback_data="case_4")

markup_cases = InlineKeyboardMarkup().add(base_case).add(boyar_case).add(
	velmoj_case).add(mecenat_case)

money_button1 = InlineKeyboardButton("250р", callback_data="money_1")
mnn = InlineKeyboardButton("Вы пополнили счёт!")

markup_money_button = InlineKeyboardMarkup().add(money_button1)

base = InlineKeyboardButton("Базовый Кейс (250 рублей)", callback_data="money_5")
boyar = InlineKeyboardButton("Кейс для бояр (500 рублей)", callback_data="money_6")
velmoj = InlineKeyboardButton("Кейс для Вельмож (1000 рублей)", callback_data="money_7")
mecenat = InlineKeyboardButton("Кейс для Меценатов (2000 рублей)", callback_data="money_8")

markup_cases_buy = InlineKeyboardMarkup().add(base).add(boyar).add(
	velmoj).add(mecenat)