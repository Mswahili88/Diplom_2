class TestDataBody:

    BODY_WITHOUT_LOGIN = {"email": "", "password": "111222333", "name": "Петя"
                          }
    BODY_WITH_CHANGED_DATA = {"email": "vvp@yxxx.ru", "password": "222333444", "name": "Аноним"}
    RESPONSE_BODY_CHANGED_DATA = {"email": "vvp@yxxx.ru", "name": "Аноним"}

    BODY_OK_REGISTRATION_AUTH = {"success": True,
                                 "user": {
                                    "email": "",
                                    "name": ""},
                                 "accessToken": "Bearer ...",
                                 "refreshToken": ""}

    body_keys = ('success' and 'true' and 'user' and 'email' and 'name' and 'accessToken' and 'refreshToken')

    space_burger = {"ingredients": ["61c0c5a71d1f82001bdaaa73"]}
    body_with_empty_ingredients = {"ingredients": []}
    body_with_wrong_hash = {"ingredients": ["61c0c5a71d1f82001bdaaa73678"]}

    user_same_name_403_body = {"success": False, "message": "User already exists"}
    user_without_login_403_body = {"success": False, "message": "Email, password and name are required fields"}
    user_auth_no_email_401_body = {"success": False, "message": "email or password are incorrect"}
    user_patch_the_same_email_403_body = {"success": False, "message": "User with such email already exists"}
    user_patch_data_non_auth_401_body = {"success": False, "message": "You should be authorised"}
    user_patch_data_with_existing_email_403_body = {"success": False,"message": "User with such email already exists"}
    order_non_ingredients_400_body = {"success": False, "message": "Ingredient ids must be provided"}
    get_non_auth_user_order_401_body = {"success": False, "message": "You should be authorised"}



