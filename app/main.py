from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from router import info, user
from db import session
from models.user import User
from api.deps import get_db

session.Base.metadata.create_all(bind=session.engine)

app = FastAPI(title="Best Practice Layout Structure", version="1.1.1")
templates = Jinja2Templates(directory="templates")

@app.get("/admin/users", response_class=HTMLResponse)
def admin_users(request: Request, db: Session = Depends(get_db)):
    users = db.query(User).all()
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

app.include_router(info.router, prefix="/api/v1/info", tags=["Information"])
app.include_router(user.router, prefix="/api/v1/user", tags=["User"])