from config import *


def format_text(text):
	new_text = ""
	for i in text.lower():
		if i in ALPHABET:
			new_text += i
	return new_text