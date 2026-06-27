from typing import Annotated

from database import Tarefa, get_session
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(prefix="/tarefas", tags=["tarefas"])


@router.get("", response_model=list[Tarefa])
def get_tarefas(session: SessionDep):
    return session.exec(select(Tarefa)).all()


@router.get("/{tarefa_id}", response_model=Tarefa)
def busca(tarefa_id: int, session: SessionDep):
    tarefa = session.get(Tarefa, tarefa_id)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa


@router.post("", status_code=201, response_model=Tarefa)
def criar(tarefa: Tarefa, session: SessionDep):
    session.add(tarefa)
    session.commit()
    session.refresh(tarefa)
    return tarefa


@router.put("/{tarefa_id}", response_model=Tarefa)
def substituir(tarefa_id: int, tarefa: Tarefa, session: SessionDep):
    db_tarefa = session.get(Tarefa, tarefa_id)
    if not db_tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    db_tarefa.titulo = tarefa.titulo
    db_tarefa.feita = tarefa.feita
    session.add(db_tarefa)
    session.commit()
    session.refresh(db_tarefa)
    return db_tarefa


@router.delete("/{tarefa_id}", status_code=204)
def delete(tarefa_id: int, session: SessionDep):
    tarefa = session.get(Tarefa, tarefa_id)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    session.delete(tarefa)
    session.commit()
