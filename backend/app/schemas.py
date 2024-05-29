from pydantic import BaseModel


class TagBase(BaseModel):
    name: str


class TagCreate(TagBase):
    pass


class Tag(TagBase):
    id: int

    class Config:
        orm_mode = True


class ProjectBase(BaseModel):

    description: str


class ProjectCreate(ProjectBase):
    title: str


class Project(ProjectBase):  # this info is what gets returned from the api
    id: int
    is_active: bool

    tags: list(Tag) = []

    class Config:
        orm_mode = True
