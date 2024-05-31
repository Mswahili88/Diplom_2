import allure
import pytest
import requests
import urls
import helper
from data import TestDataBody


@allure.step('Создание уникального пользователя и его регистрация c возвратом данных по регистрации')
@pytest.fixture(scope='function')
def default_user():
    payload = helper.TestMethodsHelper.create_random_login_password()
    response = requests.post(urls.URL_BASE + urls.URL_REG_USER, data=payload)
    yield response
    token = response.json()["accessToken"]
    requests.delete(urls.URL_BASE + urls.URL_DELETE_USER, data=payload, headers={"Authorization": token})


@allure.step('Создание данных для уникального пользователя с его регистрацией и возвратом входных данных')
@pytest.fixture(scope='function')
def payload_data():
    payload = helper.TestMethodsHelper.create_random_login_password()
    response = requests.post(urls.URL_BASE + urls.URL_REG_USER, data=payload)
    yield payload
    token = response.json()["accessToken"]
    requests.delete(urls.URL_BASE + urls.URL_DELETE_USER, data=payload, headers={"Authorization": token})

@allure.step('Создание данных для пользователя с его регистрацией, возвратом данных по регистрации и удалением измененного пользователя')
@pytest.fixture(scope='function')
def patch_data():
    payload = helper.TestMethodsHelper.create_random_login_password()
    response = requests.post(urls.URL_BASE + urls.URL_REG_USER, data=payload)
    yield response
    token = response.json()["accessToken"]
    requests.delete(urls.URL_BASE + urls.URL_DELETE_USER, data=TestDataBody.BODY_WITH_CHANGED_DATA,
                    headers={"Authorization": token})
