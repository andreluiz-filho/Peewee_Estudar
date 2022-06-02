from datetime import datetime

from peewee import (
	SqliteDatabase, 
	Model, 
	TextField,
	ForeignKeyField,
	DateTimeField,
	IntegerField
)


db = SqliteDatabase('db_main.db')

class BaseModel(Model):
	
	class Meta:
		database = db


class Empresa(BaseModel):
	nome = TextField(unique=True)
	#email = TextField()
	#endereco = TextField()
	#pasta_empresa = TextField()

class Usuarios(BaseModel):
	usuario = TextField(unique=True)
	senha = TextField()
	empresa = ForeignKeyField(Empresa, backref='usuarios')


db.create_tables([Empresa, Usuarios])
