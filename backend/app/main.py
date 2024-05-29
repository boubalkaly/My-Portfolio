from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("projects", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db())):
    db_user = crud.get_project_by_title(db, title=project.title)
    if db_user:
        raise HTTPException(status_code=400, detail="Project alrady in DB")
    return crud.create_project(db=db, project=project)
