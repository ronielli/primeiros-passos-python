from contextlib import asynccontextmanager

from database import create_db_and_tables
from fastapi import FastAPI
from routers import categorias, tarefas


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def raiz():
    return {"status": "ok"}


app.include_router(tarefas.router)

app.include_router(categorias.router)
