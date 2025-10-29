from contextlib import contextmanager
from typing import Iterator
from urllib.parse import quote_plus

from logger import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


SessionFactory = sessionmaker(
    bind=create_engine(
        f"mysql+pymysql://root:{quote_plus("%1TcEzxuzkpz1NUoqd@G4iMt")}@host.docker.internal:3306/library",
        # "mysql://root:password@localhost:3306/library",
        pool_recycle=60,
        pool_pre_ping=True,
    ),
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)


def create_session() -> Iterator[Session]:
    logger.debug("Creating session factory")
    session = SessionFactory()

    try:
        yield session
        logger.debug("Committing session")
        session.commit()
    except Exception as e:
        logger.error(e)
        logger.warning("Rollbacking session")
        session.rollback()
        logger.warning("Rollbacked session")
        raise
    finally:
        logger.debug("Closing session")
        session.close()
        logger.debug("Closed session")


@contextmanager
def open_session() -> Iterator[Session]:
    logger.debug("Returning session")
    return create_session()
