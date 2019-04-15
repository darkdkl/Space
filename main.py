import requests,os,time
from instabot import Bot
from dotenv import load_dotenv
import fetch_spacex
import fetch_hubble

PATH = os.path.normcase('./images')
os.makedirs(PATH, exist_ok=True)

def main():
    
    fetch_hubble.fetch_hubble()
    fetch_spacex.fetch_spacex_last_launch('spacex')
    caption='КосмоФото'
    bot = Bot()
    bot.login(username=os.getenv('LOGIN'), password=os.getenv('PASSWORD'))
    print('Начинаем выгрузку файлов в Instagram  ,пожалуйста подождите...')
    extension=('.jpg','.JPG','.png','.PNG')
    for img in os.listdir(PATH):
        if os.path.isfile(PATH+'/'+img) and img.endswith(extension):
            bot.upload_photo(PATH+'/'+img, caption=caption)
            time.sleep(3)
        else:
            print('Подходящие файлы не найдены')



if __name__ == "__main__":
    main()
    

