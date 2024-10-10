from pydantic import BaseModel

class CategoriaCreate(BaseModel):
    nome_categoria: str

class CategoriaRead(BaseModel):
    id_categoria: int
    nome_categoria: str

class CategoriaReadAll(BaseModel):
    categorias : list[CategoriaRead]

class CategoriaUpdate(BaseModel):
    nome_categoria: str