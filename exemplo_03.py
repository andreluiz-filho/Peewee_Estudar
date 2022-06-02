from exemplo_01 import *


nota = Nota.select().where(Nota.titulo=='Blah')


notas_rosas = (
	Nota.select()
	.join(Grupo)
	.where(Grupo.nome=='Azul').get()

)


n = Nota.select()

for i in n.dicts:
	print(i)

