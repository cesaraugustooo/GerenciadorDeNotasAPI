from fastapi import APIRouter,HTTPException
from schemas.notas import NotasRead, NotasReadAll, NotasCreate, NotasUpdate
from models.notas import *

router = APIRouter()

@router.post(path='/notas', response_model=NotasRead)
def create_notas(notas: NotasCreate):
    notas = Notas.create(**notas.model_dump())
    return notas

@router.get(path='/notas/{id}', response_model=NotasRead)
def get_notas(id: int):
    nota = Notas.get_or_none(Notas.id_nota == id)
    if not nota:
        raise HTTPException(status_code=404, detail="nota nâo cadastrado")
    return nota
@router.patch(path='/notas/{id}', response_model=NotasRead)
def update_notas(id: int, notas: NotasUpdate):
    nota = Notas.get_or_none(Notas.id_nota == id)
    if not nota:
        raise HTTPException(status_code=404, detail="nota nâo cadastrado")
    nota.titulo = notas.titulo
    nota.descricao = notas.descricao
    nota.conteudo = notas.conteudo
    nota.categoria = notas.categoria
    nota.save()
    return nota
@router.delete(path='/notas/{id}', response_model=NotasRead)
def delete_notas(id: int):
    nota = Notas.get_or_none(Notas.id_nota == id)
    if not nota:
        raise HTTPException(status_code=404, detail="nota nâo cadastrado")
    nota.delete_instance()
    return nota

@router.get(path='/notas', response_model=NotasReadAll)
def list_notas():
    notas = Notas.select()
    return {'notas': notas}
