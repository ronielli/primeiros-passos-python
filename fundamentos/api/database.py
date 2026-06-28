from config import settings
from sqlalchemy import event
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine


class CategoriaBase(SQLModel):
    nome: str
    descricao: str | None = None


class Categoria(CategoriaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tarefas: list["Tarefa"] = Relationship(back_populates="categoria")


class UsuarioCriar(SQLModel):
    email: str
    senha: str


class UsuarioBase(SQLModel):
    email: str
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
    email: str


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
