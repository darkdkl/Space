import requests
import os
import time
from instabot import Bot
from dotenv import load_dotenv
import fetch_spacex
import fetch_hubble
import download_img
import settings


def main():

    fetch_hubble.fetch_hubble_images()
    fetch_spacex.fetch_spacex_last_launch(settings.SPACEX_PHOTO_NAME)
    bot = Bot()
    bot.login(username=os.getenv('LOGIN'), password=os.getenv('PASSWORD'))
    print('Начинаем выгрузку файлов в Instagram  ,пожалуйста подождите...')
    extensions = ('.jpg', '.JPG', '.png', '.PNG')
    for img in os.listdir(settings.IMAGE_DIR):
        if os.path.isfile(settings.IMAGE_DIR+'/'+img) and img.endswith(extensions):
            bot.upload_photo(settings.IMAGE_DIR+'/'+img,
                             caption=settings.INSTAGRAM_PHOTO_CAPTIONS)
            time.sleep(3)
        else:
            print('Подходящие файлы не найдены')


if __name__ == "__main__":
    main()
