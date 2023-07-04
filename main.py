from yandexapi import YandexDisk
from vkapi import VkUser
import json


def get_file(photo_list):
    for i in photo_list:
        del i['url']
    with open('info.json', 'w') as file_info:
        json.dump(photo_list, file_info, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    vk_token = '...'
    print('Введите ID VK, по умолчанию будет использован ваш ID')
    user_id = input('ID VK: ')
    print('Введите Токен Яндекс.Диска')
    ya_token = input('Токен Яндекс.Диска: ')
    ya = YandexDisk(ya_token)
    user_vk = VkUser(vk_token)
    name_folder = ya.create_folder()
    list_photos = user_vk.get_list_of_photos(user_id=None)
    ya.upload_list_of_photos(list_photos, name_folder)
    get_file(list_photos)
