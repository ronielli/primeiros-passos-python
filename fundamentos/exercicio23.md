# Exercício 23 — Background Tasks (email de boas-vindas sem travar a resposta)

## Contexto

Hoje o `POST /usuarios` chama `enviar_email(...)` **antes** do `return` — o usuário
espera o email pra receber a resposta. Vamos mandar o email em **segundo plano** com
`BackgroundTasks`: responde na hora, email vai depois.

(Você já viu a diferença na demo: ~2s vs ~2ms.)

## O que fazer

### `api/routers/usuarios.py` — rota `criar`

1. Importe `BackgroundTasks` do FastAPI:
   ```python
   from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Request, Response
   ```
2. Adicione o parâmetro na assinatura e troque a chamada direta por `add_task`:
   ```python
   @router.post("", status_code=201, response_model=UsuarioPublico)
   def criar(usuario: UsuarioCriar, session: SessionDep, tarefas: BackgroundTasks):
       ...
       session.refresh(db_usuario)
       tarefas.add_task(enviar_email, db_usuario.email)   # antes era: enviar_email(...)
       return db_usuario
   ```

> `add_task(funcao, arg1, arg2, ...)` — passa a **função** e os **argumentos** dela
> separados (não `enviar_email(email)`, e sim `enviar_email, email`). O FastAPI chama
> ela depois de mandar a resposta.

## O que conferir

### Os testes continuam passando

```bash
uv run poe test
```

O seu `test_registro_manda_email` (com `patch`) deve continuar verde. Pense por quê:
o `TestClient` executa as background tasks **como parte do request**, antes do
`client.post(...)` retornar — então o mock ainda captura a chamada. (Se quebrar, me avise.)

### (Opcional) Ver rodando

```bash
uv run poe dev
# POST /usuarios no /docs → resposta volta na hora; o print do email aparece no
# terminal do servidor logo depois.
```

## Restrições

- Não mude o comportamento visível (ainda retorna 201 + UsuarioPublico).
- `add_task` recebe a função e os args **separados**, não a função já chamada.

## Conceitos que este exercício fixa

- `BackgroundTasks` é injetado como parâmetro (igual `session`/`Depends`).
- `add_task(fn, args)` = "rode isso depois de responder".
- Bom pra trabalho leve (email, log); pesado/crítico → fila (Celery/RQ + Redis).
- TestClient roda as background tasks dentro do request (por isso o mock ainda pega).

## Demo de referência (o exemplo mais simples — lento vs rápido)

App isolado que mostra a diferença no relógio (~2s vs ~2ms):

```python
import time

from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


def enviar_email_lento(destino: str) -> None:
    time.sleep(2)  # simula um email que demora 2s
    print(f"📧 [background] email enviado para {destino}")


# ❌ ANTIGO: o usuário espera o email (2s) pra receber a resposta
@app.post("/registro-lento")
def registro_lento(email: str):
    enviar_email_lento(email)  # bloqueia 2s
    return {"ok": True, "modo": "lento"}


# ✅ COM BackgroundTasks: responde JÁ, o email roda DEPOIS da resposta
@app.post("/registro-rapido")
def registro_rapido(email: str, tarefas: BackgroundTasks):
    tarefas.add_task(enviar_email_lento, email)  # "faça isso depois de responder"
    return {"ok": True, "modo": "rapido"}
```

Rodar: `uv run uvicorn demo:app` e comparar `time_total` dos dois com `curl -w`.

### E se a background task der ERRO?

Fire-and-forget: o usuário **já recebeu sucesso**, então não fica sabendo. O erro só
vai pro **log do servidor**, **sem retry** e sem persistência. Por isso:
- leve/não-crítico (email, log) → `BackgroundTasks` ✅
- pesado/crítico (pagamento, nota fiscal) → fila com retry (Celery/RQ + Redis) ✅
