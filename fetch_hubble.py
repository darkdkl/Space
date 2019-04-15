import requests,os

PATH = os.path.normcase('./images')
os.makedirs(PATH, exist_ok=True)


def get_extension(url):
    return url.rsplit('.')[-1]

def download_image(url, name):
    print('\u001b[1A загрузка файла с именем:',name ,',пожалуйста подождите...')
    img_response = requests.get(url)
    exstension = get_extension(url)
    fname = f'{PATH}/{name}.{exstension}'
    with open(fname, 'wb') as img:
        img.write(img_response.content)

def fetch_hubble():
    collection='wallpaper'
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
