from tinydb import TinyDB, Query

login = 'admin'
senha = '123'

db = TinyDB('db.json')


#Cria a tabela empresa
#usuarios = db.table('usuarios')
#usuarios.insert({'login':'admin', 'senha':'123'})
#usuarios.insert({'login':'suporte', 'senha':'432'})

def criar_usuario(login, senha):
	usuarios = db.table('usuarios')
	u = usuarios.search(Query().login == login)
	if u == []:
		print("Criando o usuario")
		usuarios.insert({'login':login, 'senha':senha})

criar_usuario('admin1', '123')

def fazer_login(login, senha):
	usuarios = db.table('usuarios')
	u = usuarios.search(Query().login == login)
	if len(u) == 1:
		if u[0]['senha'] == senha:
			print("Logado com Sucesso!")
		else:
			print("Usuário ou Senha Incorretos")	

	elif u == []:
		print("Usuário ou Senha Incorretos")


fazer_login('admin', '123')

"""
#Cria a tabela empresa
empresas = db.table('empresas')
"""

#u = db.table('usuarios')
#print(u.all())
#print(u.search(Query().login == login))
