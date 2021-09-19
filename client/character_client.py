from requests import Response
from requests.models import Response

from client.base_client import BaseClient
from schema.characters import Character


class CharacterClient(BaseClient):

    CHARACTER_URL = "/v2/character"
    CHARACTERS_URL = "/v2/characters"

    def get_list(self) -> Response:
        return self.make_request("GET", self.CHARACTERS_URL)

    def get_by_name(self, character_name) -> Response:
        name = {"name": character_name}
        return self.make_request("GET", self.CHARACTER_URL, params=name)

    def create(self, model: Character) -> Response:
        return self.make_request("POST", self.CHARACTER_URL, json=model.dict())

    def change_info(self, model: Character) -> Response:
        return self.make_request("PUT", self.CHARACTER_URL, json=model.dict())

    def delete(self, character_name) -> Response:
        name = {"name": character_name}
        return self.make_request("DELETE", self.CHARACTER_URL, params=name)
