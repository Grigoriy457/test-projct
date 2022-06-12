import sqlite3



class Database:
	def __init__(self, db_file):
		try:
			with open(db_file, "r") as file:
				self.connection = sqlite3.connect(db_file, check_same_thread=False)
				self.cursor = self.connection.cursor()
		except FileNotFoundError:
			with open(db_file, "w") as file:
				self.connection = sqlite3.connect(db_file, check_same_thread=False)
				self.cursor = self.connection.cursor()

				self.cursor.execute("""CREATE TABLE "bots" (
									   	   "token"        VARCHAR NOT NULL,
									   	   "bot_name"     VARCHAR NOT NULL,
									   	   "program_type" VARCHAR NOT NULL
									   );""")


	def delete_bot_from_bots(self, token):
		with self.connection:
			data = self.cursor.execute("""SELECT * FROM "bots" WHERE "token" = ?;""", (token,)).fetchone()
			self.cursor.execute("""DELETE FROM "bots" WHERE "token" = ?;""", (token,))
			return data


	def delete_all_bots(self):
		with self.connection:
			self.cursor.execute("""DELETE FROM "bots";""")


	def get_bot_data(self, token):
		with self.connection:
			data = self.cursor.execute("""SELECT * FROM "bots" WHERE "token" = ?;""", (token,)).fetchone()
			return data


	def add_bot_to_bots(self, token, name, program_type):
		with self.connection:
			self.cursor.execute("""INSERT INTO "bots" ("token", "bot_name", "program_type") VALUES (?, ?, ?);""", (token, name, program_type,))


	def get_all_bots(self):
		with self.connection:
			data = self.cursor.execute("""SELECT * FROM "bots";""").fetchall()
			if bool(len(data)):
				return data
			return list()