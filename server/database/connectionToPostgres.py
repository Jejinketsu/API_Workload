import psycopg2
import json

class DataBasePostGres(object):
	def __init__(self):
		file = open('database/db_auth_postgres.json')
		auth = json.load(file)
		file.close()

		self.host = auth['host']
		self.usuario = auth['user']
		self.db = auth['db']
		self.password = auth['password']
		self.conexao = None
		self.cursor = None

	def connect(self):
		self.conexao = psycopg2.connect(host=self.host, database=self.db, user=self.usuario, password=self.password)
		self.cursor = self.conexao.cursor()

	def disconnect(self):
		self.conexao.close()

	def insert(self, archive):
		self.cursor.execute("""INSERT INTO workload(dado) VALUES(%s);""", (archive,))
		self.conexao.commit()

"""
teste = DataBasePostGres()
teste.connect()
bytes = b'teste2'
teste.insert(bytes)
teste.disconnect()
"""