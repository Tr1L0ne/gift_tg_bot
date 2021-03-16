from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from data import MyDb
from config import TOKEN
import keyboards as kb
import cases, info
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

db = MyDb("db.db")

user = None

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
	global user
	user = message.from_user.id

	await message.answer("Welcome to the gif bot!", reply_markup=kb.markup)

	if(not db.user_id_exists(message.from_user.id)):
		# если юзера нет в базе, добавляем его
		db.add_user_id(message.from_user.id)
		db.mn(user)
		db.mn1(user)
		db.mn2(user)
		db.mn3(user)
		db.mn4(user)
		db.mn5(user)
		db.mn6(user)

@dp.message_handler(text="Как открыть коробку?")
async def show_how_to_open(message: types.Message):
	global user
	await message.answer(f"{info.htoc_text}")
	user = message.from_user.id

@dp.message_handler(text="🎁 Призы 🎁")
async def show_prizes(message: types.Message):
	global user
	user = message.from_user.id
	await message.answer(f"{info.prz}", reply_markup=kb.markup_cases)

@dp.callback_query_handler(text_contains="case_")
async def menu(call: types.CallbackQuery):
	if call.data and call.data.startswith("case_"):
		code = call.data[-1:]
		if code.isdigit():
			code = int(code)
		if code == 1:
			await call.message.edit_text(f"{cases.case_1}", reply_markup=kb.markup_cases)
		if code == 2:
			await call.message.edit_text(f"{cases.case_2}", reply_markup=kb.markup_cases)
		if code == 3:
			await call.message.edit_text(f"{cases.case_3}", reply_markup=kb.markup_cases)
		if code == 4:
			await call.message.edit_text(f"{cases.case_4}", reply_markup=kb.markup_cases)
		else:
			await bot.answer_callback_query(call.id)

@dp.message_handler(text="Пополнить счёт")
async def money_up(message: types.Message):
	global user
	user = message.from_user.id
	await message.answer("Выберите сумму:", reply_markup=kb.markup_money_button)

@dp.callback_query_handler(text_contains="money_1")
async def menu(call: types.CallbackQuery):
	global user
	await call.message.answer("Счёт пополнен на 250р")
	await call.message.edit_text("Успешно!", reply_markup=kb.mnn)
	db.add_money(250, user)

@dp.message_handler(text="Открыть коробку удачи")
async def open_case(message: types.Message):
	global user
	user = message.from_user.id
	await message.answer(f"Вам доступны: {db.money_chek2(user)}", reply_markup=kb.markup_cases_buy)

@dp.callback_query_handler(text_contains="money_")
async def menu(call: types.CallbackQuery):
	global user
	if call.data and call.data.startswith("money_"):
		code2 = call.data[-1:]
		if code2.isdigit():
			code2 = int(code2)
		if db.what_time(user) == True:
			if code2 == 5:
				if db.money_chek(250, user) == True:
					await call.message.edit_text("Успешно!")
					await call.message.answer("Вы купили кейс за 250р!")
					db.reduce_money(250, user)
					db.insert_case("base_case", user)
				else:
					await call.message.answer("Нужно пополнится чтобы получить подарок 😢")
			if code2 == 6:
				if db.money_chek(500, user) == True:
					await call.message.edit_text("Успешно!")
					await call.message.answer("Вы купили кейс за 500р!")
					db.reduce_money(500, user)
					db.insert_case("boyar_case", user)
				else:
					await call.message.answer("Нужно пополнится чтобы получить подарок 😢")
			if code2 == 7:
				if db.money_chek(1000, user) == True:
					await call.message.edit_text("Успешно!")
					await call.message.answer("Вы купили кейс за 1000р!")
					db.reduce_money(1000, user)
					db.insert_case("velmoj_case", user)
				else:
					await call.message.answer("Нужно пополнится чтобы получить подарок 😢")
			if code2 == 8:
				if db.money_chek(2000, user) == True:
					await call.message.edit_text("Успешно!",)
					await call.message.answer("Вы купили кейс за 2000р!")
					db.reduce_money(2000, user)
					db.insert_case("mecenat_case", user)
				else:
					await call.message.answer("Нужно пополнится чтобы получить подарок 😢")
			else:
				await bot.answer_callback_query(call.id)
		else:
			await call.message.answer("Сегодня вы уже купили 3 кейса!")
			db.add_time(user)

@dp.message_handler(text="Мои подарки")
async def my_prizes(message: types.Message):
	global user
	user = message.from_user.id
	await message.answer(f"""
		Твои подарки:
		{db.show_cases(user)}""")

if __name__ == '__main__':
	executor.start_polling(dp)