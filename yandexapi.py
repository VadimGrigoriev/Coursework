import requests
from tqdm import tqdm


class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_folder(self):
        """Метод создает папку на Яндекс.Диск"""
        while True:
            name_folder = input('Введите название папки: ')
            url = 'https://cloud-api.yandex.net/v1/disk/resources'
            headers = self.get_headers()
            params = {'path': name_folder}
            res = requests.put(url, headers=headers, params=params)
            if res.ok:
                return name_folder
            else:
                print('Папка с таким названием уже существует, придумайте новое название.')

    def upload_file(self, link, name_folder):
        """Метод для загрузки файла на Яндекс.Диск по URL"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {
            'path': name_folder,
            'url': link
        }
        res = requests.post(url, headers=headers, params=params)
        if res.ok:
            pass
        else:
            print('Ошибка при загрузке фотографии на Яндекс.Диск.')

    def upload_list_of_photos(self, list_photos, name_folder):
        """Метод загружает список фотографий на Яндекс.Диск по URL"""
        pbar = tqdm(list_photos, ncols=81, desc='Выполнение...')
        for photo in pbar:
            disk_filename = f"{name_folder}/{photo['file_name']}"
            link = photo['url']
            self.upload_file(link, disk_filename)
        print('Фотографии загружены!')
