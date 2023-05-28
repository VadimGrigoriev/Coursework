import requests
from tqdm import tqdm
import json


class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_folder(self, title):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': title}
        res = requests.put(url, headers=headers, params=params)
        return res.json()

    @staticmethod
    def get_file(photo_list):
        for i in photo_list:
            del i['url']
        with open('info.json', 'w') as file_info:
            json.dump(photo_list, file_info, ensure_ascii=False, indent=2)

    def upload_file(self, link, disk_filename):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {
            'path': disk_filename,
            'url': link
        }
        res = requests.post(url, headers=headers, params=params)

    def upload_list_of_photos(self, list_photos, user_filename):
        pbar = tqdm(list_photos, ncols=81, desc='Выполнение...')
        for photo in pbar:
            disk_filename = f"{user_filename}/{photo['file_name']}"
            link = photo['url']
            self.upload_file(link, disk_filename)
        self.get_file(list_photos)
        print('Фотографии загружены!')
