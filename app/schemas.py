from pydantic import BaseModel, AnyHttpUrl


class URLCreate(BaseModel):
    target_url: AnyHttpUrl


class URLRead(BaseModel):
    short_code: str
    target_url: AnyHttpUrl
    click_count: int

