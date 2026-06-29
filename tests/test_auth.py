from unittest.mock import Mock, patch

import pytest

enviar_email = Mock()


@pytest.mark.parametrize(
    "metodo, url",
    [
        ("get", "/tarefas"),
        ("get", "/usuarios/me"),
    ],
)
def test_rotas_protegidas_sem_token(client, metodo, url):
    r = getattr(client, metodo)(url)
    assert r.status_code == 401


def test_me_token_expirado(client, monkeypatch):
    from config import settings

    client.post("/usuarios", json={"email": "r@g.com", "senha": "12345678"})
    monkeypatch.setattr(settings, "access_token_expire_minutes", -1)  # nasce vencido
    token = client.post(
        "/usuarios/login", json={"email": "r@g.com", "senha": "12345678"}
    ).json()["access_token"]
    r = client.get("/usuarios/me", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 401


def test_registro_manda_email(client):
    with patch("routers.usuarios.enviar_email") as email_fake:
        r = client.post("/usuarios", json={"email": "r@g.com", "senha": "12345678"})
        assert r.status_code == 201
        email_fake.assert_called_once()  # mandou? (sem mandar de verdade)


@pytest.fixture(name="token")
def token_fixture(client):
    client.post("/usuarios", json={"email": "r@g.com", "senha": "12345678"})
    r = client.post("/usuarios/login", json={"email": "r@g.com", "senha": "12345678"})
    return r.json()["access_token"]


def test_registro(client):
    r = client.post("/usuarios", json={"email": "r@g.com", "senha": "12345678"})
    assert r.status_code == 201
    assert r.json()["id"] == 1
    assert "senha_hash" not in r.json()


def test_login_sucesso(client):
    r = client.post("/usuarios", json={"email": "r@g.com", "senha": "12345678"})
    r = client.post("/usuarios/login", json={"email": "r@g.com", "senha": "12345678"})
    assert r.status_code == 200
    assert "access_token" in r.json()


def test_login_senha_errada(client):
    r = client.post("/usuarios", json={"email": "r@g.com", "senha": "12345678"})
    r = client.post("/usuarios/login", json={"email": "r@g.com", "senha": "123456789"})
    assert r.status_code == 401


def test_me_sem_token(client):
    r = client.get("/usuarios/me")
    assert r.status_code == 401


def test_me_com_token(client, token):
    r = client.get("/usuarios/me", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200
    assert r.json()["email"] == "r@g.com"
    assert "senha_hash" not in r.json()


def test_listar_tarefas_protegida(client):
    r = client.get("/tarefas")
    assert r.status_code == 401


def test_registro_email_invalido(client):
    r = client.post("/usuarios", json={"email": "banana", "senha": "senha-1234"})
    assert r.status_code == 422


def test_registro_senha_curta(client):
    r = client.post("/usuarios", json={"email": "ok@x.com", "senha": "123"})
    assert r.status_code == 422


def test_registro_senha_letra(client):
    r = client.post("/usuarios", json={"email": "ok@x.com", "senha": "abcdefgh"})
    assert r.status_code == 422
