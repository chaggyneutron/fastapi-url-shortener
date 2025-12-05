from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlmodel import Session

from .database import init_db, get_session
from .schemas import URLCreate, URLRead
from .crud import create_short_url, get_url_by_code

app = FastAPI(title="URL Shortener API")


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/shorten", response_model=URLRead)
def shorten_url(payload: URLCreate, session: Session = Depends(get_session)):
    url = create_short_url(session, payload.target_url)
    return URLRead(
        short_code=url.short_code,
        target_url=url.target_url,
        click_count=url.click_count,
    )


@app.get("/{short_code}")
def redirect(short_code: str, session: Session = Depends(get_session)):
    url = get_url_by_code(session, short_code)
    if not url:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="URL not found"
        )
    url.click_count += 1
    session.add(url)
    session.commit()
    return RedirectResponse(url.target_url)

