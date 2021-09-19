from requests.models import Response
from helper.logger import LOGGER
from client.character_client import CharacterClient as cl
import pytest
from schema.characters import Character
from faker import Faker
from config import settings as cfg
from base64 import b64encode
from collections import namedtuple


URL = cfg.url


@pytest.fixture(scope="session")
def faker():
    yield Faker()


@pytest.fixture(scope="class")
def character_client():
    data = f"{cfg.email}:{cfg.password}".encode("utf-8")
    _b64encode = b64encode(data).decode("utf-8")
    _client = cl(URL, default_headers={"Authorization": f"Basic {_b64encode}"})
    _client.reset_collection()
    yield _client


@pytest.fixture(scope="function")
def create_character(character_client, faker):
    model = Character(
        name=faker.name(),
        universe=faker.address(),
        education=faker.company(),
        other_aliases="qwe",
        weight=faker.pyfloat(),
        height=faker.pyfloat(),
        identity=faker.job(),
    )
    res = character_client.create(model)
    _ = namedtuple("resp", "res model")

    yield _(res, model)

    character_client.delete(model.name)
