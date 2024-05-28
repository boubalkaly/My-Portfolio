from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Project(Base):
    __tablename__ = "projects"  # this is going to be the name of the database
    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String)
    is_active = Column(Boolean, default=True)

    tags = relationship("Tag", back_populates="owner")


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    owner = relationship("Project", back_populates="tags")


# at the end of the day keep in mind that pydantic models and sqlalchemy models are completely different
