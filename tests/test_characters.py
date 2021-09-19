import allure
from truth.truth import AssertThat

from helper import common_steps
from schema.characters import Character, Characters


@allure.label("layer", "rest")
@allure.label("owner", "aslagunkov")
class TestCharacters:


    @allure.label("Method", "GET")
    @allure.title("Проверяем структуру ответа на получение списка всех персонажей")
    def test_get_list(self, character_client):
        r = character_client.get_list()
        with common_steps.STATUS_200:
            AssertThat(r.status_code).IsEqualTo(200)
        with allure.step("Проверяем структуру ответа"):
            Characters.parse_obj(r.json())

    @allure.label("Method", "POST")
    @allure.title("Создаем персонажа с полной информацией")
    def test_create(self, create_character):
        with common_steps.STATUS_200:
            AssertThat(create_character.res.status_code).IsEqualTo(200)

    @allure.label("Method", "POST")
    @allure.title("Создаем персонажа с пустым body")
    def test_create_with_empty_body(self, character_client):
        model = Character()
        r = character_client.create(model)
        with common_steps.STATUS_400:
            AssertThat(r.status_code).IsEqualTo(400)

    @allure.label("Method", "GET")
    @allure.title("Находим персонажа с помощью имени")
    def test_get_by_name(self, character_client, create_character):
        model = create_character.model  # создаем персонажа
        res = character_client.get_by_name(model.name)
        with common_steps.STATUS_200:
            AssertThat(res.status_code).IsEqualTo(200)
        with allure.step("Проверяем, что имя совпадает с созданным"):
            AssertThat(res.json()["result"]["name"]).Contains(model.name)
