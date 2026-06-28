from datetime import UTC, datetime, timedelta
from typing import Annotated

import bcrypt
from database import Usuario, UsuarioBase, UsuarioCriar, get_session
from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt
from pydantic import BaseModel
from sqlmodel import Session, select

SECRET_KEY = "ESTUDOS_RONIELLI"
ALGORITHM = "HS256"

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(prefix="/usuarios", tags=["usuarios"])


def hash_senha(senha: str) -> str:
    return bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()


def verificar_senha(senha: str, hash: str) -> bool:
    return bcrypt.checkpw(senha.encode(), hash.encode())


bearer_scheme = HTTPBearer(auto_error=False)


def get_current_user(
    request: Request,
    session: SessionDep,
    credentials: Annotated[
        HTTPAuthorizationCredentials | None, Depends(bearer_scheme)
    ] = None,
) -> Usuario:
    token = credentials.credentials if credentials else request.cookies.get("authToken")
    if not token:
        raise HTTPException(status_code=401, detail="não autenticado")
    try:
        dados = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = dados["sub"]
    except Exception:
        raise HTTPException(status_code=401, detail="token invalido") from None
    usuario = session.exec(select(Usuario).where(Usuario.email == email)).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="token invalido")
    return usuario


class Token(BaseModel):
    access_token: str
    token_type: str


@router.get("", response_model=list[Usuario])
def get(session: SessionDep):
    return session.exec(select(Usuario)).all()


@router.get("/me", response_model=Usuario)
def me(usuario: Annotated[Usuario, Depends(get_current_user)]):
    return usuario


@router.get("/{usuario_id}", response_model=Usuario)
def busca(usuario_id: int, session: SessionDep):
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="usuario não encontrado")
    return usuario


@router.post("", status_code=201, response_model=Usuario)
def criar(usuario: UsuarioCriar, session: SessionDep):
    dados = usuario.model_dump()
    dados["senha_hash"] = hash_senha(dados.pop("senha"))
    db_usuario = Usuario.model_validate(dados)
    session.add(db_usuario)
    session.commit()
    session.refresh(db_usuario)
    return db_usuario


@router.post("/login", response_model=Token)
def login(usuario: UsuarioCriar, session: SessionDep, response: Response):
    usuario_db = session.exec(
        select(Usuario).where(Usuario.email == usuario.email)
    ).first()
    if not usuario_db or not verificar_senha(usuario.senha, usuario_db.senha_hash):
        raise HTTPException(status_code=401, detail="credenciais invalidas")
    token = jwt.encode(
        {"sub": usuario_db.email, "exp": datetime.now(UTC) + timedelta(minutes=30)},
        SECRET_KEY,
        algorithm=ALGORITHM,
    )
    response.set_cookie(key="authToken", value=token, httponly=True, max_age=1800)
    return {"access_token": token, "token_type": "bearer"}


@router.delete("/{usuario_id}", status_code=204)
def delete(usuario_id: int, session: SessionDep):
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="usuario não encontrado")
    session.delete(usuario)
    session.commit()


@router.put("/{usuario_id}", response_model=Usuario)
def substituir(usuario_id: int, usuario: UsuarioBase, session: SessionDep):
    db_usuario = session.get(Usuario, usuario_id)
    if not db_usuario:
        raise HTTPException(status_code=404, detail="usuario não encontrado")
    db_usuario.email = usuario.email
    session.add(db_usuario)
    session.commit()
    session.refresh(db_usuario)
    return db_usuario
