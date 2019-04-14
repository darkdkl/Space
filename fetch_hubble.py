import requests,os
import main

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
            main.download_image(img_url_prepare[-1], ids)
