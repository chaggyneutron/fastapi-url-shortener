from typing import Union

from pydantic import AnyHttpUrl
from sqlmodel import Session, select

from .models import URL
import secrets
import string


def generate_short_code(length: int = 7) -> str:
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def create_short_url(session: Session, target_url: Union[str, AnyHttpUrl]) -> URL:
    # Convert AnyHttpUrl (Pydantic type) to plain string for SQLite
    target_url_str = str(target_url)

    short_code = generate_short_code()
    db_url = URL(short_code=short_code, target_url=target_url_str)
    session.add(db_url)
    session.commit()
    session.refresh(db_url)
    return db_url


def get_url_by_code(session: Session, short_code: str) -> URL | None:
    statement = select(URL).where(URL.short_code == short_code)
    return session.exec(statement).first()

