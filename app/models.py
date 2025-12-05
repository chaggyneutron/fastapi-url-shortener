from sqlmodel import SQLModel, Field
from datetime import datetime

class URL(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    short_code: str = Field(index=True, unique=True)
    target_url: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    click_count: int = Field(default=0)

