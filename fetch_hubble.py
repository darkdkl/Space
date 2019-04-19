import requests,os
import download_img

def fetch_hubble_images():
    collection='wallpaper'
    params = {'page': 'all'}
    response = requests.get(
        f'http://hubblesite.org/api/v3/images/{collection}', params=params)
    img_url_prepare = []
    for img_id in response.json():
        image_id = img_id['id']
        response = requests.get(f'http://hubblesite.org/api/v3/image/{image_id}')

        for img in response.json()['image_files']:
            img_url_prepare.append(img['file_url'])
            download_img.download_image(img_url_prepare[-1], image_id)

if __name__ == "__main__":
    fetch_hubble_images()
