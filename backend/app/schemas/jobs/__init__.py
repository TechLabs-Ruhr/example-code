from pydantic import BaseModel, Field
from typing import Optional
from functools import cached_property

class JobBase(BaseModel):
    title: str
    description: str
    label: Optional[str]


class JobCreate(JobBase):
    pass


class Job(JobBase):
    id: int
    # parents: list[JobBase] = []
    class Config:
        orm_mode = True

class JobRelation(Job):
    children: list[Job] = []
    parents: list[Job] = []
    class Config:
        orm_mode = True

class JobNodes(Job):
    pass

class JobEdges(BaseModel):
    from_: int
    to: int
    description: Optional[str] = Field(alias="label")

    class Config:
        fields = {
            'from_': 'from'  # to allow use of registred python keyword from
        }

class JobGraph(BaseModel):
    nodes: list[JobNodes]
    edges: list[JobEdges]
