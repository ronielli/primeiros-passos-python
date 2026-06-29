from config import settings
from pydantic import EmailStr, field_validator
from sqlalchemy import event
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine


class CategoriaBase(SQLModel):
    nome: str
    descricao: str | None = None


class Categoria(CategoriaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tarefas: list["Tarefa"] = Relationship(back_populates="categoria")


class UsuarioCriar(SQLModel):
    email: EmailStr
    senha: str = Field(min_length=8)

    @field_validator("senha")
    @classmethod
    def senha_tem_numero(cls, v: str) -> str:
        if not any(c.isdigit() for c in v):
            raise ValueError("a senha precisa ter pelo menos um número")
        return v


class UsuarioBase(SQLModel):
    email: EmailStr
    senha_hash: str


class Usuario(UsuarioBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class TarefaBase(SQLModel):
    titulo: str
    feita: bool = False
    prioridade: int = 0
    categoria_id: int | None = Field(default=None, foreign_key="categoria.id")


class UsuarioPublico(SQLModel):
    id: int
    email: EmailStr


class Tarefa(TarefaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    categoria: Categoria | None = Relationship(back_populates="tarefas")


class TarefaComCategoria(SQLModel):
    id: int | None
    titulo: str
    feita: bool
    categoria: Categoria | None = None


engine = create_engine(settings.database_url)


@event.listens_for(engine, "connect")
def enforce_foreign_keys(dbapi_connection, _):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
