import sys
from logging.config import fileConfig
from pathlib import Path

from sqlalchemy import create_engine, pool

from alembic import context

# === ADIÇÃO 1: deixar o Python achar os módulos da API ======================
# (mesma ideia do `pythonpath` dos testes — a API usa imports "crus")
sys.path.append(str(Path(__file__).resolve().parents[1] / "fundamentos" / "api"))

import database  # noqa: E402, F401  (importa p/ REGISTRAR as tabelas no metadata)
from config import settings  # noqa: E402
from sqlmodel import SQLModel  # noqa: E402

# ============================================================================

# Objeto de config do Alembic — dá acesso aos valores do alembic.ini.
config = context.config

# Configura o logging a partir do .ini.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# === ADIÇÃO 3: apontar para o metadata dos seus modelos =====================
# É o que o autogenerate compara com o banco para descobrir o que mudou.
target_metadata = SQLModel.metadata
# ============================================================================


def run_migrations_offline() -> None:
    """Roda migrations em modo 'offline' (gera SQL sem conectar no banco)."""
    # ADIÇÃO 2: usa a SUA URL (do .env via settings), não a placeholder do .ini
    context.configure(
        url=settings.database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Roda migrations em modo 'online' (conecta no banco e aplica)."""
    # ADIÇÃO 2: monta o engine direto da SUA URL (do .env), ignorando o .ini
    connectable = create_engine(settings.database_url, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
