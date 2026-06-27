from fastapi import FastAPI
from routers import tarefas

app = FastAPI()


@app.get("/")
def raiz():
    return {"status": "ok"}


app.include_router(tarefas.router)
