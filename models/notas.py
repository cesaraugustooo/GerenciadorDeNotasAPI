from peewee import AutoField,IntegerField,CharField,Model,ForeignKeyField
from config.database import database

class Categorias(Model):
    id_categoria = AutoField()
    nome_categoria = CharField()
    class Meta:
        database = database



class Notas(Model):
    id_nota = AutoField()
    titulo = CharField()
    descricao = CharField()
    conteudo = CharField()
    categoria = ForeignKeyField(model=Categorias,backref='categorias')
    class Meta:
        database = database