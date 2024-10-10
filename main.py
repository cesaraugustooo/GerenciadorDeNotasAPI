from fastapi import FastAPI
from routers.notas import router as notas_router
from routers.categorias import router as categorias_router
from config.database import conect,end
app = FastAPI()

app.add_event_handler("startup", conect)
app.add_event_handler("shutdown", end)


app.include_router(notas_router,tags=["notas"])
app.include_router(categorias_router,tags=["categorias"])




