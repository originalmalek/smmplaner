import argparse
import os

import facebook
import telebot
import vk_api

from dotenv import load_dotenv
from vk_api import VkUpload


def post_vk(post_text, image_name, vk_token, vk_group_id):
    vk_session = vk_api.VkApi(token=vk_token)
    vk_methods = vk_session.get_api()

    saved_group_photo = VkUpload(vk_session).photo_wall(photos=image_name, group_id=vk_group_id)

    owner_id = saved_group_photo[0]['owner_id']
    from_group = 1
    media_id = saved_group_photo[0]['id']

    vk_methods.wall.post(message=post_text, access_token=vk_token, v=5.122, group_id=vk_group_id,
                         from_group=from_group, attachments=f'photo{owner_id}_{media_id}', owner_id=-vk_group_id)


def post_telegram(post_text, image_name, telegram_token, telegram_group_name):
    bot = telebot.TeleBot(telegram_token)

    with open(image_name, 'rb') as image:
        bot.send_photo(chat_id=telegram_group_name, photo=image, caption=post_text)


def post_facebook(post_text, image_name, fb_access_token, fb_group_id):
    graph = facebook.GraphAPI(access_token=fb_access_token)
    with open(image_name, 'rb') as image:
        graph.put_photo(image=image, message=post_text, album_path=fb_group_id + "/photos")


def main():
    load_dotenv()
    vk_token = os.getenv('VK_ACCESS_TOKEN')
    vk_group_id = int(os.getenv('VK_GROUP_ID'))
    fb_group_id = os.getenv('FACEBOOK_GROUP_ID')
    fb_access_token = os.getenv('FACEBOOK_ACCESS_TOKEN')
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    telegram_group_name = os.getenv('TELEGRAM_GROUP_NAME')


    parser = argparse.ArgumentParser(description='The programm upload intent to Google DialogFlow')

    parser.add_argument('image_name', help='Enter your image name')
    parser.add_argument('post_text', help='Enter your text')

    args = parser.parse_args()

    image_name = args.image_name
    post_text = args.post_text

    post_telegram(post_text, image_name, telegram_token, telegram_group_name)
    post_vk(post_text, image_name, vk_token, vk_group_id)
    post_facebook(post_text, image_name, fb_access_token, fb_group_id)


if __name__ == '__main__':
    main()
