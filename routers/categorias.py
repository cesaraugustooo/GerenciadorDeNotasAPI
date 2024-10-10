from fastapi import APIRouter,HTTPException
from schemas.categorias import CategoriaRead,CategoriaReadAll,CategoriaCreate,CategoriaUpdate
from models.notas import *



router = APIRouter()

@router.post(path="/categorias",response_model=CategoriaRead)
def create_categorias(categorias : CategoriaCreate):
    categoria = Categorias.create(**categorias.model_dump())
    return categoria

@router.get(path="/categorias/{id}",response_model=CategoriaRead)
def get_categoria(id: int):
    categoria = Categorias.get_or_none(Categorias.id_categoria==id)
    if not categoria:
        raise HTTPException(status_code=404, detail="categoria nâo cadastrado")
    return categoria
@router.get(path="/categorias",response_model=CategoriaReadAll)
def get_all_categorias():
    categorias = Categorias.select()
    return {'categorias':categorias}
@router.delete(path="/categorias/{id}",response_model=CategoriaRead)
def delete_categoria(id: int):
    categorias = Categorias.get_or_none(Categorias.id_categoria==id)
    categorias.delete_instance()
    if not categorias:
        raise HTTPException(status_code=404, detail="categoria nâo cadastrado")
    return categorias
@router.patch(path="/categorias/{id}",response_model=CategoriaRead)
def update_categoria(id: int,categoria : CategoriaUpdate):
    categorias = Categorias.get_or_none(Categorias.id_categoria==id)
    if not categoria:
        raise HTTPException(status_code=404, detail="categorioa nâo cadastrado")
    categorias.nome_categoria = categoria.nome_categoria
    categorias.save()
    return categorias
