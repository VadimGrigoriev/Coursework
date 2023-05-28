import requests


class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version='5.131'):
        self.params = {
            'access_token': token,
            'v': version
        }

    def user_filename(self, user_id=None):
        info_user_url = self.url + 'users.get'
        info_user_params = {
            'user_ids': user_id
        }
        res = requests.get(info_user_url, params={**self.params, **info_user_params}).json()
        info_user = res['response'][0]
        filename = f"{info_user['first_name']} {info_user['last_name']}"
        return filename

    def get_users_photos(self, user_id=None, count=5):
        get_users_photos_url = self.url + 'photos.get'
        get_users_photos_params = {
            'owner_id': user_id,
            'album_id': 'profile',
            'rev': 1,
            'extended': 1,
            'count': count
        }
        res = requests.get(get_users_photos_url, params={**self.params, **get_users_photos_params})
        return res.json()

    def get_list_of_photos(self, user_id=None, count=5):
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
