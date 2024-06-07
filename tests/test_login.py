import allure
import requests
import urls
from data import TestDataBody


class TestLogin:

    @allure.title('Успешная авторизация зарегистрированного пользователя')
    @allure.description('Проверяем, что зарегистрированный пользователь успешно проходит авторизацию')
    def test_auth_user(self, payload_data_new):
        requests.post(urls.URL_BASE + urls.URL_REG_USER, data=payload_data_new)
        response = requests.post(urls.URL_BASE + urls.URL_AUTH, data=payload_data_new)
        assert response.status_code == 200 and TestDataBody.body_keys in TestDataBody.BODY_OK_REGISTRATION_AUTH

    @allure.title('Неуспешная авторизация пользователя с отсутствующим обязательным к заполнению полем')
    @allure.description('Проверяем, что без поля "email" не удастся пройти авторизацию')
    def test_auth_user_without_email(self):
        response = requests.post(urls.URL_BASE + urls.URL_AUTH, data=TestDataBody.BODY_WITHOUT_LOGIN)
        assert response.status_code == 401 and response.json() == TestDataBody.user_auth_no_email_401_body




