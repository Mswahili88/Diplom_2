import allure
import requests
import urls
from data import TestDataBody


class TestGetOrder:

    @allure.title('Проверка получения заказов конкретного авторизованного пользователя')
    @allure.description('Проверяем, что авторизованный пользователь может успешно получить свои заказы')
    def test_get_auth_user_oder(self, payload_data_new):
        user = requests.post(urls.URL_BASE + urls.URL_REG_USER, data=payload_data_new)
        token = user.json()["accessToken"]
        requests.post(urls.URL_BASE + urls.URL_MAKE_ORDER, headers={'Authorization': token},
                              data=TestDataBody.space_burger)
        requests.post(urls.URL_BASE + urls.URL_MAKE_ORDER, headers={'Authorization': token},
                      data=TestDataBody.space_burger)
        total = requests.get(urls.URL_BASE + urls.URL_GET_ORDER_USER, headers={'Authorization': token})
        assert total.status_code == 200 and len(total.json()["orders"]) == 2
        print(total.json()['orders'])

    @allure.title('Проверка получения заказов неавторизованным пользователем')
    @allure.description('Проверяем,что неавторизованный пользователь не сможет получить список заказов')
    def test_get_non_auth_user_order(self, payload_data_new):
        requests.post(urls.URL_BASE + urls.URL_REG_USER, data=payload_data_new)
        total = requests.get(urls.URL_BASE + urls.URL_GET_ORDER_USER)
        assert total.status_code == 401 and total.json() == TestDataBody.get_non_auth_user_order_401_body
        print(total.json())

