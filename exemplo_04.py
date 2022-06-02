from hashlib import sha512
from exemplo_01 import db, Pessoa
from peewee import fn



@db.func()
def encripta_senha(senha):
	return sha512(senha.encode('utf-8')).hexdigest()

Pessoa.create(
	nome='Criptografada',
	senha=fn.encripta_senha('1234'),
	email='cript2@teste.com',
	idade=25
)