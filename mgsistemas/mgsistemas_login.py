from hashlib import sha512
from peewee import fn

from mgsistemas_db import db, Empresa, Usuario

@db.func()
def encripta_senha(senha):
	return sha512(senha.encode('utf-8')).hexdigest()


usuario_login = "suporte"
usuario_senha = "123"
usuario_senha_encriptada = encripta_senha(usuario_senha)


query = Usuario.select(Usuario.usuario.in_([usuario_login]))

print(query.get())

"""
for i in query:
	if i.usuario == usuario_login:

		if i.senha == usuario_senha_encriptada:
			print("Usuario e Senha são Iguais")
			break
		else:
			print("Usuario ou Senha incorreto")
			break
	else:
		print("Usuario ou Senha incorreto")
		break
"""