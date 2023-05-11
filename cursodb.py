from sqlalchemy import create_engine

postgresql_engine = create_engine(
    "postgresql://postgres:1234@127.0.0.1/curso",
    pool_reset_on_return=None,
)