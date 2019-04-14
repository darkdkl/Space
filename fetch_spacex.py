import requests,os
import main

def fetch_spacex_last_launch(name):
    response = requests.get('https://api.spacexdata.com/v3/launches/76')
    url_imgs = []
    for img_url_prepare in response.json()['links']["flickr_images"]:
        url_imgs.append(img_url_prepare)

    for number, url_img in enumerate(url_imgs):
        names = f'{name}{number}'
        main.download_image(url_img, names)