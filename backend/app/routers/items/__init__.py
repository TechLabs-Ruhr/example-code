from fastapi import Depends

import app.crud.users as crud
import app.schemas as schemas
from app.database.session import Session, get_db
from app.routers.api_router import api_router


@api_router.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
