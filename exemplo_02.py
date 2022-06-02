from exemplo_01 import Pessoa, Grupo, Nota


fulano = Nota(
	nome='Fulano',
	idade=18,
	senha='1234',
	email='eu@eu.com'
)

try:
	fulano.save()

	Pessoa.create(
		nome='Fausto',
		idade=3,
		email='fausto@live',
		senha='7654321'
	)
except:
	...



#Nota.create(titulo='Nova Nota', nota='Anotação Nova', dona=Pessoa.select().where(Pessoa.nome=='Fausto'),grupo=Grupo.select().where(Grupo.nome=='Azul').get())