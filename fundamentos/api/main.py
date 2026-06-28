from fastapi import FastAPI
from routers import categorias, tarefas, usuarios

app = FastAPI()


@app.get("/")
def raiz():
    return {"status": "ok"}


app.include_router(tarefas.router)
app.include_router(categorias.router)
app.include_router(usuarios.router)
