import json

from app.settings import valid_email, valid_password
from app.primer_api import PetFriends
import os

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в результате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result



def test_post_add_pet_nofoto(name='King-Pongs', animal_type='Monkey-King', age='155'):
    """Проверяем создание нового питомца без фото"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.post_add_pet_nofoto(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    print('РЕЗУЛЬТАТ>>>', result)
    assert status == 200
    assert result['name'] == name, result['animal_type'] == animal_type and result['age'] == age



def test_post_changes_pet_foto(pet_photo=r'../images/king-kong1.jpg'):
    """Проверяем добавление фото к id добавленного питомца без фото..."""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # Добавляем фото
    status, result = pf.post_add_pet_photo(auth_key, pet_photo)
    # Получаем значение картинки1:
    dict_py1 = result.get('pet_photo')
    #value_image1 = dict_py1.get('pet_photo')
    print(dict_py1)

    #Добавление нового фото:
    pf.post_add_pet_photo(auth_key, r'../images/king-kong2.jpg')
    _, result2 = pf.post_add_pet_photo(auth_key, pet_photo)

    # Получаем значение картинки2:
    dict_py2 = result2.get('pet_photo')
    #value_image2 = dict_py2.get('pet_photo')
    print(dict_py2)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert dict_py1 == dict_py2






# def test_post_add_pet_foto(pet_photo=r'../images/king-kong2.jpg'):
#     """Проверяем добавление нового фото"""
#
#     # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
#     pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
#
#     # Запрашиваем ключ api и сохраняем в переменую auth_key
#     _, auth_key = pf.get_api_key(valid_email, valid_password)
#
#     # Добавляем фото
#     status, result = pf.post_add_pet_photo(auth_key, pet_photo)
#
#     # Получаем значение картинки1:
#     dict_py = json.loads(result)
#     value_image = dict_py.get('pet_photo')
#     print(value_image)
#
#
#     # Сверяем полученный ответ с ожидаемым результатом
#     assert status == 200
#     assert 'data:image/jpeg' in result


# def test_post_change_pet_foto(pet_photo=r'../images/king-kong2.jpg'):
#     """Проверяем добавление нового фото"""
#
#     # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
#     pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
#
#     # Запрашиваем ключ api и сохраняем в переменую auth_key
#     _, auth_key = pf.get_api_key(valid_email, valid_password)
#
#     # Добавляем фото
#     status, result = pf.post_add_pet_photo(auth_key, pet_photo)
#
#     # Сверяем полученный ответ с ожидаемым результатом
#     dict_py = json.loads(result)
#     value_image = dict_py.get('pet_photo')
#     print(value_image)
#     assert status == 200
#     assert 'data:image/jpeg' in result

"""
find(str, start) : параметр start задает начальный индекс, с которого будет производиться поиск
"""
