import pytest
from database import get_session
from fastapi.testclient import TestClient
from main import app
from sqlalchemy import event
from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    # FK fica DESLIGADA por padrão no SQLite; ligamos a cada conexão nova.
    # Tem que ser aqui dentro: é onde o `engine` local existe.
    def liga_fk(dbapi_connection, _):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

    event.listen(engine, "connect", liga_fk)

    SQLModel.metadata.create_all(engine)  # cria as tabelas no banco vazio
    with Session(engine) as session:
        yield session  # entrega pro teste...
    # ...e o que vem depois do yield é o "teardown" (afterEach)
    engine.dispose()  # fecha as conexões do engine (sem isso: ResourceWarning)


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    yield TestClient(app)
    app.dependency_overrides.clear()
