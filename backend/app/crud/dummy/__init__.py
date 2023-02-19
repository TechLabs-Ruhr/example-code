import logging
from random import randint

from pydantic.types import PositiveInt

logger = logging.getLogger("faker")
logger.setLevel(logging.INFO)  # Quiet faker locale messages down in tests.

from faker import Faker  # noqa: E402

fake = Faker("de_DE")


def create_dummy_numbers():
    data = [randint(0, 100) for _ in range(0, 10)]
    return data


def create_dummy_numbers_param(n: PositiveInt):
    """
    Get a list of random numbers with n elements
    """
    data = [randint(0, 100) for _ in range(0, n)]
    return data


def get_dummy_random_person():
    """
    Get a random person
    """
    data = {"name": fake.name(), "address": fake.address()}
    return data


def get_dummy_random_person_param(n: PositiveInt):
    """
    Get a list of random persons of length n
    """
    data = [{"name": fake.name(), "address": fake.address()} for _ in range(0, n)]
    return data
