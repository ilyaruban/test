import json
import pprint

import requests

with open('token_yandex.txt', 'r') as file_yandex:
    token_yandex = file_yandex.readline()

url_yandex = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

url_folder_create = 'https://cloud-api.yandex.net/v1/disk/resources'

url_get_folder = 'https://cloud-api.yandex.net/v1/disk/resources'


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.params = {}
        self.name_folder = ''
        self.list_files = []

    def create_folder(self, url):
        self.name_folder = 'тест_1'
        headers = {
            'Authorization': self.token
        }
        path = {
            'path': str(self.name_folder)
        }
        response = requests.put(url, headers=headers, params=path)
        return response.status_code, self.name_folder

    def get_folder(self, url):
        headers = {
            'Authorization': self.token
        }
        path = {
            'path': 'disk:/'
        }
        responce = requests.get(url, headers=headers, params=path)
        dict_folder = json.loads(responce.text)
        for name in dict_folder['_embedded']['items']:
            self.list_files.append(name['name'])
        return self.list_files


yandex_load = YaUploader(token_yandex)

create = yandex_load.create_folder(url_folder_create)

list_folder = yandex_load.get_folder(url_get_folder)


def test_1():
    assert 200 <= create[0] < 300, 'Ошибка выполнения запроса'

    assert create[1] in list_folder, 'название папки должно быть в списке'


if __name__ == '__main__':
    test_1()