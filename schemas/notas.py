from pydantic import BaseModel
from schemas.categorias import CategoriaRead


class NotasCreate(BaseModel):
    titulo : str
    descricao : str
    conteudo : str
    categoria : int

class NotasRead(BaseModel):
    id_nota: int
    titulo : str
    descricao : str
    conteudo : str
    categoria : CategoriaRead

class NotasUpdate(BaseModel):
    titulo: str
    descricao: str
    conteudo: str
    categoria: int

class NotasReadAll(BaseModel):
    notas : list[NotasRead]




