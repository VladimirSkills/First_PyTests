import requests
import json

class PetFriends:
    """апи библиотека к веб приложению Pet Friends"""

    def __init__(self):
        self.idp = ""
        self.base_url = "https://petfriends.skillfactory.ru/"


    def get_api_key(self, email: str, passwd: str) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
        JSON с уникальным ключом пользователя, найденного по указанным email и паролем"""

        headers = {
            'email': email,
            'password': passwd,
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result


    # Добавление питомца без фото
    def post_add_pet_nofoto(self, auth_key: json, name: str, animal_type: str, age: str) -> json:

        headers = {'auth_key': auth_key['key']}  #, 'Content-Type': data.content_type}
        data = {'name': name, 'animal_type': animal_type, 'age': age}
        res = requests.post(self.base_url + 'api/create_pet_simple', data=data, headers=headers)
        status = res.status_code
        try:
            result = res.json()
            #print(res.json().get("id"))
            self.idp = res.json().get("id")
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result


    # Добавление фото питомца
    def post_add_pet_photo(self, auth_key: json, pet_photo: str) -> json:
        headers = {'auth_key': auth_key['key']}
        pet_id = self.idp  # Добавляем фото к созданному питомцу без фото
        files = {"pet_photo": open(pet_photo, "rb")}
        res = requests.post(self.base_url + 'api/pets/set_photo/' + pet_id, files=files, headers=headers)
        status = res.status_code
        result = res.text
        return status, result




