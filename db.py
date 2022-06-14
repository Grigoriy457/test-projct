import sqlite3
import os



class Database:
	def __init__(self, db_file):
		if not os.path.exists(db_file):  # Проверка на существование файла
			with open(db_file, "w"):  # Создание файла db
				pass

		self.connection = sqlite3.connect(db_file, check_same_thread=False)
		self.cursor = self.connection.cursor()

		if not os.path.exists(db_file):  # Проверка на существование файла
			# Создание таблицы
			self.cursor.execute("""CREATE TABLE "bots" (
									   "token"        VARCHAR NOT NULL,
									   "bot_name"     VARCHAR NOT NULL,
									   "program_type" VARCHAR NOT NULL
								   );""")

	
	# Удаление бота из таблицы
	def delete_bot_from_bots(self, token):
		with self.connection:
			data = self.cursor.execute("""SELECT * FROM "bots" WHERE "token" = ?;""", (token,)).fetchone()
			self.cursor.execute("""DELETE FROM "bots" WHERE "token" = ?;""", (token,))
			return data


	# Удаление всех ботов из таблицы
	def delete_all_bots(self):
		with self.connection:
			self.cursor.execute("""DELETE FROM "bots";""")


	# Получение информации о боте
	def get_bot_data(self, token):
		with self.connection:
			data = self.cursor.execute("""SELECT * FROM "bots" WHERE "token" = ?;""", (token,)).fetchone()
			return data

	
	# Добавление бота в таблицу
	def add_bot_to_bots(self, token, name, program_type):
		with self.connection:
			self.cursor.execute("""INSERT INTO "bots" ("token", "bot_name", "program_type") VALUES (?, ?, ?);""", (token, name, program_type,))

	
	# Получение всех ботов из таблицы
	def get_all_bots(self):
		with self.connection:
			data = self.cursor.execute("""SELECT * FROM "bots";""").fetchall()
			if bool(len(data)):
				return data
			return list()