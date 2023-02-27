from sqlalchemy.orm import Session

from app import models, schemas


def get_job(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()

def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Job).offset(skip).limit(limit).all()

def get_jobs_by_category(db: Session, category: str):
    return db.query(models.Job).filter(models.Job.category == category).first()

def get_job_graph(db: Session):
    # Example function to return nodes & edges - could be optimized
    nodes = []
    edges = []
    from pydantic import parse_obj_as
    for node in db.query(models.Job).all():
        nodes.append(parse_obj_as(schemas.JobNodes, node).dict(by_alias=True))
        for node_target in node.children:
            edges.append({
                'from': node_target.id,
                'to': node.id,
                'label': 'hardcoded'
            })
    
    return {'nodes': nodes, 'edges': edges}

