from typing import Dict, List

from pydantic.types import PositiveInt

import app.crud.dummy as crud
from app.routers.api_router import api_router


@api_router.get("/dummy/numbers", tags=["dummy"], response_model=List[int])
def get_dummy_numbers():
    """
    Get a list of random numbers with hardcoded elements
    """
    return crud.create_dummy_numbers()


@api_router.get("/dummy/numbers/{n}", tags=["dummy"], response_model=List[int])
def get_dummy_numbers_param(n: PositiveInt):
    """
    Get a list of random numbers with n elements
    """
    return crud.create_dummy_numbers_param(n)


@api_router.get("/faker/person", tags=["dummy"], response_model=Dict)
def get_dummy_random_person():
    """
    Get a random person
    """
    return crud.get_dummy_random_person()


@api_router.get("/faker/person/{n}", tags=["dummy"], response_model=List[Dict])
def get_dummy_random_person_param(n: PositiveInt):
    """
    Get a list of random persons of length n
    """
    return crud.get_dummy_random_person_param(n)
