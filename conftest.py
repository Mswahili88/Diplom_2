import allure
import pytest
import requests
import urls
import helper
from data import TestDataBody


@allure.step('Создание данных для уникального пользователя и дальнейшее его удаление')
@pytest.fixture(scope='function')
def payload_data_new():
    payload = helper.TestMethodsHelper.create_random_login_password()
    yield payload
    response = requests.post(urls.URL_BASE + urls.URL_AUTH, data=payload)
    token = response.json()["accessToken"]
    requests.delete(urls.URL_BASE + urls.URL_DELETE_USER, data=payload, headers={"Authorization": token})
#для бОльшей части теста оставил одну фикстуру

@allure.step('Создание данных для пользователя с его регистрацией, возвратом данных по регистрации и удалением измененного пользователя')
@pytest.fixture(scope='function')
def patch_data():
    payload = helper.TestMethodsHelper.create_random_login_password()
    response = requests.post(urls.URL_BASE + urls.URL_REG_USER, data=payload)
    yield response
    token = response.json()["accessToken"]
    requests.delete(urls.URL_BASE + urls.URL_DELETE_USER, data=TestDataBody.BODY_WITH_CHANGED_DATA,
                    headers={"Authorization": token})
#эту фикстуру для 1 теста я держу только для того, чтобы, согласно требованиям из задания, удалять созданные перед тестом данные
#в данном случае требуется удаление созданного в фикстуре пользователя, у которого в результате теста были изменены данные
#как выполнить это постусловие - вернуть измененные данные обратно в фикстуру для удаления или как-то по-другому, я просто не знаю


@allure.step('Создание двух пользователей для теста с последующим их удалением')
@pytest.fixture(scope='function')
def two_default_users():
    payload_one = helper.TestMethodsHelper.create_random_login_password()
    response_one = requests.post(urls.URL_BASE + urls.URL_REG_USER, data=payload_one)
    payload_two = helper.TestMethodsHelper.create_random_login_password()
    response_two = requests.post(urls.URL_BASE + urls.URL_REG_USER, data=payload_two)
    token_two = response_two.json()["accessToken"]
    data = [payload_one, token_two]
    yield data
    token_one = response_one.json()["accessToken"]
    requests.delete(urls.URL_BASE + urls.URL_DELETE_USER, data=payload_one,
                    headers={"Authorization": token_one})
    requests.delete(urls.URL_BASE + urls.URL_DELETE_USER, data=payload_two,
                    headers={"Authorization": token_two})
    # эту фикстуру для 1 теста я держу только для того, чтобы, согласно требованиям из задания, удалять созданные перед тестом данные
    # в данном случае мне для теста были нужны 2 пользователя, чтобы взять от одного токен, а от другого - почту.
    # как выполнить постусловие - удалить сразу обоих созданных юзеров, я не знаю.


