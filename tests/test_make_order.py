import allure
import requests
import urls
from data import TestDataBody


class TestMakeOrder:

    @allure.title('Проверка создания заказа с авторизацией')
    @allure.description('Проверяем авторизованным пользователем успешное создание заказа с ингридиентами')
    def test_order_auth_done(self, payload_data_new):
        user = requests.post(urls.URL_BASE + urls.URL_REG_USER, data=payload_data_new)
        token = user.json()["accessToken"]
        order = requests.post(urls.URL_BASE + urls.URL_MAKE_ORDER, headers={'Authorization': token},
                              data=TestDataBody.space_burger)
        assert order.status_code == 200 and order.json()["order"]["status"] == "done"

    @allure.title('Проверка создания заказа без ингредиентов')
    @allure.description('Проверяем создание заказа при условии отсутствия каких бы то ни было ингредиентов')
    def test_empty_ingredient(self, payload_data_new):
        user = requests.post(urls.URL_BASE + urls.URL_REG_USER, data=payload_data_new)
        token = user.json()["accessToken"]
        order = requests.post(urls.URL_BASE + urls.URL_MAKE_ORDER, headers={'Authorization': token},
                              data=TestDataBody.body_with_empty_ingredients)
        assert order.status_code == 400 and order.json() == TestDataBody.order_non_ingredients_400_body

    @allure.title('Проверка создания заказа с неверным хэшем ингредиента')
    @allure.description('Проверяем создание заказа при условии неверного хэша ингредиента, ошибка 500')
    def test_wrong_hash_ingredient(self, payload_data_new):
        user = requests.post(urls.URL_BASE + urls.URL_REG_USER, data=payload_data_new)
        token = user.json()["accessToken"]
        order = requests.post(urls.URL_BASE + urls.URL_MAKE_ORDER, headers={'Authorization': token},
                              data=TestDataBody.body_with_wrong_hash)
        assert order.status_code == 500

    @allure.title('Проверка создания заказа без авторизации')
    @allure.description('Проверяем возможность создания заказа неавторизованным пользователем')
    def test_order_non_auth(self, payload_data_new):
        requests.post(urls.URL_BASE + urls.URL_REG_USER, data=payload_data_new)
        order = requests.post(urls.URL_BASE + urls.URL_MAKE_ORDER, data=TestDataBody.space_burger)
        assert order.status_code == 200 and order.json()["name"] == "Space бургер"
