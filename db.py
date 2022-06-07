import sqlite3



class Database:
	def __init__(self, db_file):
		self.connection = sqlite3.connect(db_file, check_same_thread=False)
		self.cursor = self.connection.cursor()


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