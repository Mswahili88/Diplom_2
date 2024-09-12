import allure
import requests
import urls
from data import TestDataBody


class TestCreateUser:
    @allure.title('Создание уникального пользователя')
    @allure.description('Проверяем успешное создание пользователя, статус 200 и соответствие тела ответа согласно ТЗ')
    def test_create_user(self, payload_data_new):
        response = requests.post(urls.URL_BASE + urls.URL_REG_USER, data=payload_data_new)
        assert response.status_code == 200 and TestDataBody.body_keys in TestDataBody.BODY_OK_REGISTRATION_AUTH

    @allure.title('Проверка регистрации уже существующего пользователя')
    @allure.description('Проверяем, что нельзя повторно зарегистрировать уже существующего пользователя')
    def test_same_user(self, payload_data_new):
        requests.post(urls.URL_BASE + urls.URL_REG_USER, data=payload_data_new)
        response = requests.post(urls.URL_BASE + urls.URL_REG_USER, data=payload_data_new)
        assert response.status_code == 403 and response.json() == TestDataBody.user_same_name_403_body

    @allure.title('Проверка регистрации пользователя без одного из обязательных атрибутов регистрации')
    @allure.description('Проверяем, что нельзя зарегистрировать пользователя без поля "email"')
    def test_empty_login_user(self):
        response = requests.post(urls.URL_BASE + urls.URL_REG_USER, data=TestDataBody.BODY_WITHOUT_LOGIN)
        assert response.status_code == 403 and response.json() == TestDataBody.user_without_login_403_body

