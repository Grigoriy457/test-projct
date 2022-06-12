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
	if message.author == client.user or message.author.bot:
		return

	response = requests.get("http://rzhunemogu.ru/Rand.aspx?CType=1")

	if response.status_code == 200:
		tree = ET.ElementTree(ET.fromstring(response.text))
		await message.reply(tree.find("content").text, mention_author=False)
	else:
		await message.reply(f"Error!\nStatus code: {response.status_code}")


def start_bot(token):
	client.run(token)


if __name__ == "__main__":
	time.sleep(2)

	token = sys.argv[1]
	threading.Thread(target=gf.scheduler, args=(token, client.user,)).start()
	start_bot(token)