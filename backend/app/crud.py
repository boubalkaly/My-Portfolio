from sqlalchemy.orm import Session

from . import models, schemas


def get_project(db: Session, project_id: int):  # get the project
    return db.query(models.Project).filter(models.Project.id == project_id).first()


def get_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Project).offset(skip).limit(limit).all()


def get_project_by_title(db: Session, title: str):
    return db.query(models.Project).filter(models.Project.title == title).first()


def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(title=project.title)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def create_tag(db: Session, tag: schemas.TagCreate):
    db_tag = models.Tag()
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag
