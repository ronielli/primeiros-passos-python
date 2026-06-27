from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

tarefas = [
    {"id": 1, "titulo": "Aprender FastAPI", "feita": False},
    {"id": 2, "titulo": "Tomar café", "feita": True},
]


class TarefaNova(BaseModel):
    titulo: str
    feita: bool = False


class TarefaOut(BaseModel):
    id: int
    titulo: str
    feita: bool


router = APIRouter(prefix="/tarefas", tags=["tarefas"])


@router.get("", response_model=list[TarefaOut])
def get_tarefas():
    return tarefas


@router.get("/{tarefa_id}", response_model=TarefaOut)
def busca(tarefa_id: int):
    for item in tarefas:
        if item["id"] == tarefa_id:
            return item
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")


@router.post("", status_code=201, response_model=TarefaOut)
def criar(tarefa: TarefaNova):
    novo_id = max((t["id"] for t in tarefas), default=0) + 1
    nova = {"id": novo_id, "titulo": tarefa.titulo, "feita": tarefa.feita}
    tarefas.append(nova)
    return nova


@router.put("/{tarefa_id}")
def substituir(tarefa: TarefaNova, tarefa_id: int):
    for i, item in enumerate(tarefas):
        if item["id"] == tarefa_id:
            body = {
                "id": item["id"],
                "titulo": tarefa.titulo,
                "feita": tarefa.feita,
            }
            tarefas[i] = body
            return body
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")


@router.delete("/{tarefa_id}", status_code=204)
def delete(tarefa_id: int):
    for i, item in enumerate(tarefas):
        if item["id"] == tarefa_id:
            del tarefas[i]
            return
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")
