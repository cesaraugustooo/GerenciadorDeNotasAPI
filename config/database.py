from peewee import SqliteDatabase

database = SqliteDatabase('database.db')


def conect():
    database.connect()
    from models.notas import Categorias,Notas
    database.create_tables([Categorias,Notas])

def end():
    database.close()
