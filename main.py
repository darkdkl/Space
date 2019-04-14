import requests,os,time
from instabot import Bot
from dotenv import load_dotenv

PATH = os.path.normcase('./images')
os.makedirs(PATH, exist_ok=True)


def fetch_spacex_last_launch(name):
    response = requests.get('https://api.spacexdata.com/v3/launches/76')
    url_imgs = []
    for img_url_prepare in response.json()['links']["flickr_images"]:
        url_imgs.append(img_url_prepare)

    for number, url_img in enumerate(url_imgs):
        names = f'{name}{number}'
        download_image(url_img, names)


def get_extension(url):
    return url.rsplit('.')[-1]


def fetch_hubble(collection):
    params = {'page': 'all'}
    response = requests.get(
        f'http://hubblesite.org/api/v3/images/{collection}', params=params)
    img_url_prepare = []
    for img_id in response.json():
        ids = img_id['id']
        response = requests.get(f'http://hubblesite.org/api/v3/image/{ids}')

        for img in response.json()['image_files']:
            img_url_prepare.append(img['file_url'])
            download_image(img_url_prepare[-1], ids)


def download_image(url, name):

    img_response = requests.get(url)
    exstension = get_extension(url)
    fname = f'{PATH}/{name}.{exstension}'
    with open(fname, 'wb') as img:
        img.write(img_response.content)

def main():
    
    fetch_hubble('wallpaper')
    fetch_spacex_last_launch('spacex')
    bot = Bot()
    bot.login(username=os.getenv('LOGIN'), password=os.getenv('PASSWORD'))
    extension=('.jpg','.JPG','.png','.PNG')
    for img in os.listdir(PATH):
        if os.path.isfile(PATH+'/'+img) and img.endswith(extension):
            bot.upload_photo(PATH+'/'+img, caption='КосмоФото')
            time.sleep(3)
        else:
            print('Подходящие файлы не найдены')



if __name__ == "__main__":
    main()

