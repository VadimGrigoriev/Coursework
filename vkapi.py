import requests


class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version='5.131'):
        self.params = {
            'access_token': token,
            'v': version
        }

    def get_users_photos(self, user_id=None, count=5):
        """Метод для получения информации о фотографиях с альбома пользователя"""
        get_users_photos_url = self.url + 'photos.get'
        get_users_photos_params = {
            'owner_id': user_id,
            'album_id': 'profile',
            'rev': 1,
            'extended': 1,
            'count': count
        }
        res = requests.get(get_users_photos_url, params={**self.params, **get_users_photos_params})
        if res.ok:
            return res.json()
        else:
            print('Ошибка при получении информации о фотографиях.')

    def get_list_of_photos(self, user_id=None, count=5):
        """Метод создает список с основной информацией о фотографиях пользователя"""
        photos = self.get_users_photos(user_id, count)
        list_photos = []
        for photo in photos['response']['items']:
            dict_photo = {
                'file_name': f"{photo['likes']['count']}.jpg",
                'url': photo['sizes'][-1]['url'],
                'size': photo['sizes'][-1]['type']
            }
            if any(f"{photo['likes']['count']}.jpg" in p['file_name'] for p in list_photos):
                dict_photo['file_name'] = f"{photo['likes']['count']}_{photo['date']}.jpg"
            list_photos.append(dict_photo)
        return list_photos
