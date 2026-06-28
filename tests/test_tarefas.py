def test_raiz(client):
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_criar_tarefa(client):
    r = client.post("/categorias", json={"nome": "Estudos"})
    assert r.json()["id"] == 1
    assert r.status_code == 201
    r = client.post(
        "/tarefas", json={"titulo": "string", "feita": False, "categoria_id": 1}
    )
    assert r.status_code == 201


def test_get_inexistente(client):
    r = client.get("/tarefas/10")
    assert r.status_code == 404


def test_criar_e_buscar(client):
    r = client.post("/categorias", json={"nome": "Estudos"})
    assert r.json()["id"] == 1
    assert r.status_code == 201
    r = client.post(
        "/tarefas", json={"titulo": "string", "feita": False, "categoria_id": 1}
    )
    assert r.status_code == 201
    r = client.get("/tarefas/1")
    assert r.status_code == 200


def test_deletar_tarefa(client):
    r = client.post("/categorias", json={"nome": "Estudos"})
    assert r.json()["id"] == 1
    assert r.status_code == 201
    r = client.post(
        "/tarefas", json={"titulo": "string", "feita": False, "categoria_id": 1}
    )
    assert r.status_code == 201
    r = client.delete("/tarefas/1")
    assert r.status_code == 204


def test_criar_tarefa_categoria_inexistente(client):
    r = client.post(
        "/tarefas", json={"titulo": "string", "feita": False, "categoria_id": 1}
    )
    assert r.status_code == 422
