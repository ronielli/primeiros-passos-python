from sqlmodel import Field, Session, SQLModel, create_engine


class Tarefa(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    titulo: str
    feita: bool = False


class CategoriaBase(SQLModel):
    nome: str


class Categoria(CategoriaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


engine = create_engine("sqlite:///tarefas.db")


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
