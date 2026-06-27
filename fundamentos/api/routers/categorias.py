from typing import Annotated

from database import Categoria, CategoriaBase, get_session
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(prefix="/categorias", tags=["categorias"])


@router.get("", response_model=list[Categoria])
def get(session: SessionDep):
    return session.exec(select(Categoria)).all()


@router.get("/{categoria_id}", response_model=Categoria)
def busca(categoria_id: int, session: SessionDep):
    categoria = session.get(Categoria, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="categoria não encontrada")
    return categoria


@router.post("", status_code=201, response_model=Categoria)
def criar(categoria: CategoriaBase, session: SessionDep):
    db_categoria = Categoria.model_validate(categoria)
    session.add(db_categoria)
    session.commit()
    session.refresh(db_categoria)
    return db_categoria


@router.delete("/{categoria_id}", status_code=204)
def delete(categoria_id: int, session: SessionDep):
    categoria = session.get(Categoria, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="categoria não encontrada")
    session.delete(categoria)
    session.commit()


@router.put("/{categoria_id}", response_model=Categoria)
def substituir(categoria_id: int, categoria: CategoriaBase, session: SessionDep):
    db_categoria = session.get(Categoria, categoria_id)
    if not db_categoria:
        raise HTTPException(status_code=404, detail="categoria não encontrada")
    db_categoria.nome = categoria.nome
    session.add(db_categoria)
    session.commit()
    session.refresh(db_categoria)
    return db_categoria
