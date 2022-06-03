from hashlib import sha512
from mgsistemas_db import db, Empresa, Usuario
from peewee import fn

@db.func()
def encripta_senha(senha):
	return sha512(senha.encode('utf-8')).hexdigest()


try:
	Empresa.create(
		nome="Empresa Teste"
	)
except:
	...


try:
	Usuario.create(
		usuario="suporte",
		senha=fn.encripta_senha('123'),
		empresa=Empresa.select().where(Empresa.nome=="Empresa Teste").get()
	)
except:
	...
