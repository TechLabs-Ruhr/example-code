from fastapi import Depends, HTTPException

import app.crud.jobs as crud_jobs

import app.schemas as schemas
from app.database.session import Session, get_db
from app.routers.api_router import api_router


@api_router.get("/jobs/", response_model=list[schemas.JobRelation])
def read_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    jobs = crud_jobs.get_jobs(db, skip=skip, limit=limit)
    return jobs

@api_router.get("/jobs/{job_id}", response_model=schemas.JobRelation)
def read_job(job_id: int, db: Session = Depends(get_db)):
    db_job = crud_jobs.get_job(db, job_id=job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job

@api_router.post("/users/init/", response_model=list[schemas.JobRelation])
def init_jobs(
    db: Session = Depends(get_db)
):
    from app import models
    job1 = models.Job(title="Technican Mechanics I", description="Test")
    job2 = models.Job(title="Technican Mechanics II", description="Test 2")
    job2.children.append(job1)
    db.add_all([job1, job2])
    db.commit()
    db.refresh(job2)
    print(job2.children)
    return [job2]

@api_router.get("/jobs/graph/", response_model=schemas.JobGraph, response_model_by_alias=True)
def read_job_graph(db: Session = Depends(get_db)):
    print('test')
    graph = crud_jobs.get_job_graph(db)
    graph_pydantic = schemas.JobGraph(**graph)
    return graph_pydantic.dict(by_alias=True)
