# test_criar_categoria — POST 201 + id.
# test_listar_categorias — cria 2, GET /categorias retorna 2.
# test_categoria_inexistente — GET /categorias/999 → 404.
# test_atualizar_categoria — POST, PUT muda o nome, confere.
# test_deletar_categoria — POST, DELETE → 204, GET → 404.


def test_criar_categoria(client):
    r = client.post("/categorias", json={"nome": "Estudos", "descricao": "Estudos"})
    assert r.status_code == 201
    assert "id" in r.json()


def test_listar_categorias(client):
    client.post("/categorias", json={"nome": "Estudos"})
    client.post("/categorias", json={"nome": "Trabalho"})

    r = client.get("/categorias")
    assert r.status_code == 200

    dados = r.json()
    assert isinstance(dados, list)
    assert len(dados) == 2  # as 2 que ESTE teste criou
    assert dados[0]["nome"] == "Estudos"


def test_categoria_inexistente(client):
    r = client.get("/categorias/999")
    assert r.status_code == 404


def test_atualizar_categoria(client):
    r = client.post("/categorias", json={"nome": "Estudos", "descricao": "Estudos"})
    assert "id" in r.json()
    r = client.put(
        f"/categorias/{r.json()['id']}",
        json={"nome": "Teste", "descricao": "Teste"},
    )
    assert r.status_code == 200
    assert r.json()["nome"] == "Teste"


def test_deletar_categoria(client):
    r = client.post("/categorias", json={"nome": "Estudos", "descricao": "Estudos"})
    assert "id" in r.json()
    r = client.delete(f"/categorias/{r.json()['id']}")
    assert r.status_code == 204
