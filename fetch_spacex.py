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



def fetch_spacex_last_launch(name):
    launch='76'
    response = requests.get(f'https://api.spacexdata.com/v3/launches/{launch}')
    url_imgs = []
    for img_url_prepare in response.json()['links']["flickr_images"]:
        url_imgs.append(img_url_prepare)

    for number, url_img in enumerate(url_imgs):
        names = f'{name}{number}'
        download_image(url_img, names)