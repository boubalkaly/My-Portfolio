from fastapi import FastAPI
from .router import projects
from .database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(projects.router)
