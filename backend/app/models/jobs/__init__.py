from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.hybrid import hybrid_property

from app.database.database import Base


association_job_table = Table(
    "association_job_table",
    Base.metadata,
    Column("parent_id", ForeignKey("jobs.id")),
    Column("child_id", ForeignKey("jobs.id")),
    Column("description", String),
)

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    category = Column(String, index=True)

    parents = relationship(
        'Job',
        secondary=association_job_table,
        primaryjoin=association_job_table.c.parent_id==id,
        secondaryjoin=association_job_table.c.child_id==id,
        backref='children'
    )


    @hybrid_property
    def label(self):
        return f"{self.title} - {self.description}"
