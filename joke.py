import discord
from discord.ext import commands

import random
import requests
import sys, os
import asyncio
import threading
import time

from config import *
from global_functions import *
from db import Database


client = commands.Bot(command_prefix='!')

db = Database("db.db")


def stop_bot(token):
	os.kill(os.getpid(), 9)


async def check(token):
	await asyncio.sleep(2)

	data = db.get_bot_data(token)

	if data == None:
		stop_bot(token)


def scheduler(token):
	while True:
		asyncio.run(check(token))


@client.event
async def on_ready():
	print(f"Logged in ({client.user})!")


@client.command()
async def joke(message):
	if message.author == client.user or message.author.bot:
		return

	response = requests.get("http://rzhunemogu.ru/RandJSON.aspx?CType=1")
	if response.status_code == 200:
		await message.reply(response.text[12:-2], mention_author=False)
	else:
		await message.reply(f"Error!\nStatus code: {response.status_code}")


def start_bot(token):
	client.run(token)


if __name__ == "__main__":
	time.sleep(2)

	token = sys.argv[1]

	threading.Thread(target=scheduler, args=(token,)).start()
	start_bot(token)