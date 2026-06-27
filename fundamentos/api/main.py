from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tarefas = [
    {"id": 1, "titulo": "Aprender FastAPI", "feita": False},
    {"id": 2, "titulo": "Tomar café", "feita": True},
]


@app.get("/")
def raiz():
    return {"msg": "ola mundo"}


@app.get("/tarefas")
def get_tarefas():
    return tarefas


@app.get("/tarefas/{tarefa_id}")
def busca(tarefa_id: int):
    for item in tarefas:
        if item["id"] == tarefa_id:
            return item
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")


class TarefaNova(BaseModel):
    titulo: str
    feita: bool = False


@app.post("/tarefas", status_code=201)
def criar(tarefa: TarefaNova):
    novo_id = max((t["id"] for t in tarefas), default=0) + 1
    nova = {"id": novo_id, "titulo": tarefa.titulo, "feita": tarefa.feita}
    tarefas.append(nova)
    return nova
