from hashlib import sha512
from peewee import fn

from mgsistemas_db import db, Empresa, Usuario

@db.func()
def encripta_senha(senha):
	return sha512(senha.encode('utf-8')).hexdigest()


usuario_login = "suporte"
usuario_senha = "123"
usuario_senha_encriptada = encripta_senha(usuario_senha)

try:
	query = Usuario.select().where(Usuario.usuario == usuario_login).get()

	if query.senha == usuario_senha_encriptada:
		print("Usuario e Senha são Iguais")

	else:
		print("Usuario ou Senha incorretos")

except:
	print("Usuario ou Senha incorretos")