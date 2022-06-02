from mgsistemas_db import Empresa, Usuarios



try:
	Empresa.create(
		nome="Empresa Teste"
	)
except:
	...


try:
	Usuarios.create(
		usuario="admin",
		senha="123",
		empresa=Empresa.select().where(Empresa.nome=="Empresa Teste").get()
	)
except:
	...
