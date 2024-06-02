import allure
import requests
import urls
from data import TestDataBody


class TestChangeDataUser:

    @allure.title('Проверка изменения всех данных авторизованным пользователем')
    @allure.description('Проверяем, что авторизованный пользователь может поменять любое из своих регистрационных полей')
    def test_change_data_auth(self, patch_data):
        token = patch_data.json()["accessToken"]
        change = requests.patch(urls.URL_BASE + urls.URL_CHANGE_DATA, headers={'Authorization': token},
                                data=TestDataBody.BODY_WITH_CHANGED_DATA)
        assert change.status_code == 200 and change.json()["user"] == TestDataBody.RESPONSE_BODY_CHANGED_DATA

    @allure.title('Проверка невозможности изменения данных неавторизованным пользователем')
    @allure.description('Проверяем, что неавторизованный пользователь не может поменять свои регистрационные данные')
    def test_change_data_non_auth(self, patch_data):
        change = requests.patch(urls.URL_BASE + urls.URL_CHANGE_DATA, data=TestDataBody.BODY_WITH_CHANGED_DATA)
        assert change.status_code == 401 and change.json() == TestDataBody.user_patch_data_non_auth_401_body

    @allure.title('Проверка невозможности изменения данных авторизованным пользователем с чужой почтой')
    @allure.description('Проверяем, что авторизованный пользователь не может поменять данные, указав чужую почту')
    def test_change_data_existing_email(self, two_default_users):
        change = requests.patch(urls.URL_BASE + urls.URL_CHANGE_DATA, headers={'Authorization': two_default_users[1]},
                                data=two_default_users[0])
        assert change.status_code == 403 and change.json() == TestDataBody.user_patch_data_with_existing_email_403_body
