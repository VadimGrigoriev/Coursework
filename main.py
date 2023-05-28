from yandexapi import YandexDisk
from vkapi import VkUser


with open('ya_token.txt') as ya_file:
    ya_token = ya_file.read().strip()

with open('vk_token.txt') as vk_file:
    vk_token = vk_file.read().strip()

if __name__ == '__main__':
    print('Введите ID VK, по умолчанию будет использован ваш ID')
    user_id = input('ID VK: ')
    ya = YandexDisk(ya_token)
    user_vk = VkUser(vk_token)
    user_filename = user_vk.user_filename(user_id=None)
    ya.create_folder(user_filename)
    list_photos = user_vk.get_list_of_photos(user_id=None)
    ya.upload_list_of_photos(list_photos, user_filename)
