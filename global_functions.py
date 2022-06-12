import asyncio
from db import Database
import os
from config import *


db = Database("db.db")


def format_text(text):
	new_text = ""
	for i in text.lower():
		if i in ALPHABET + " ":
			new_text += i
	return new_text


def stop_bot(token, bot_name):
	print(f"[+] Bot {bot_name} is disabled!")
	os.kill(os.getpid(), 9)


async def check(token, bot_name):  # Проверка существованиятокена бота в базе данных
	await asyncio.sleep(2)

	data = db.get_bot_data(token)

	if data == None:
		stop_bot(token, bot_name)


def scheduler(token, bot_name):
	while True:
		asyncio.run(check(token, bot_name))