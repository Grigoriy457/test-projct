from discord.ext import commands
import requests
import sys
import threading
import time
import xml.etree.ElementTree as ET
from config import *
import global_functions as gf


client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
	print(f"[+] Logged in ({client.user})!")


@client.command()
async def joke(message):
	if message.author == client.user or message.author.bot:  # Проверка сообщения от бота или пользователя
		return

	response = requests.get("http://rzhunemogu.ru/Rand.aspx?CType=1")  # Отправка запроса на сайт с шуками

	if response.status_code == 200:  # Проверка статус кода (200 - всё хорошо)
		tree = ET.ElementTree(ET.fromstring(response.text))  # Парсинг xml структуры
		await message.reply(tree.find("content").text, mention_author=False)  # Получение content из xml структуры
	else:
		await message.reply(f"Error!\nStatus code: {response.status_code}")


def start_bot(token):
	client.run(token)  # Запуск бота


if __name__ == "__main__":
	time.sleep(2)

	token = sys.argv[1]  # Получение токена из строки вызова (python echo.py TOKEN)
	threading.Thread(target=gf.scheduler, args=(token, client.user,)).start()
	start_bot(token)