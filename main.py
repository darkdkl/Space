import requests,os

PATH='./images'
os.makedirs(PATH, exist_ok=True)

def fetch_spacex_last_launch(url,name):
    response = requests.get(url)
    url_imgs=[]
    for img_url_prepare in response.json()['links']["flickr_images"]:
        url_imgs.append(img_url_prepare)
    
    for number,url_img in enumerate(url_imgs):
        img_response=requests.get(url_img)
        fname=f'{PATH}/{str(number)}_{name}'
        with open(fname,'wb') as img:
            img.write(img_response.content)
 
last_launch='https://api.spacexdata.com/v3/launches/76'
name='spacex.jpg'
# fetch_spacex_last_launch(last_launch,name)


def get_extension(url):
    return url.rsplit('.')[-1]
    

def download_image(image_id):
    
    response = requests.get(f'http://hubblesite.org/api/v3/image/{image_id}')
    img_url_prepare=[]
       
    for img in response.json()['image_files']:
        img_url_prepare.append(img['file_url'])
         
    img_response=requests.get(img_url_prepare[-1])
    exstension=get_extension(img_url_prepare[-1])
    fname=f'{PATH}/{image_id}.{exstension}'
    with open(fname,'wb') as img:
        img.write(img_response.content)


def get_id(collection):

    params={'page':'all'}
    response = requests.get(f'http://hubblesite.org/api/v3/images/{collection}',params=params)
    
    for id_img in response.json():
        download_image(id_img['id'])
    

#ждать  ответа между скачиваниями - yeld??

get_id('wallpaper')

# download_image(3858)
