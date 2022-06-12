import discord
import random
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
	if message.author == client.user or message.author.bot:
		return

	message_text = format_text(message.content)
	if message_text in [i.lower() for i in HELLO_TYPES]:
		await message.channel.send(f"{random.choice(HELLO_TYPES).title()}, {message.author.mention}!", mention_author=False)


def start_bot(token):
	client.run(token)


if __name__ == "__main__":
	time.sleep(2)

	token = sys.argv[1]
	threading.Thread(target=gf.scheduler, args=(token, client.user,)).start()
	start_bot(token)