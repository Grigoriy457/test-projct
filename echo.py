import discord
import sys
import threading
import time
from config import *
import global_functions as gf


client = discord.Client()


@client.event
async def on_ready():
	print(f"[+] Logged in ({client.user})!")


@client.event
async def on_message(message):
	if message.author == client.user or message.author.bot:  # Проверка сообщения от бота или пользователя
		return

	if message.content != "":  # ОБработка пустого сообщения (если отправляется картинка без текста)
		await message.channel.send(message.content)


def start_bot(token):
	client.run(token)


if __name__ == "__main__":
	time.sleep(2)

	token = sys.argv[1]
	threading.Thread(target=gf.scheduler, args=(token, client.user,)).start()
	start_bot(token)