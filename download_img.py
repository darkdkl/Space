import requests,os
import settings

def download_image(url, name):
    os.makedirs(settings.IMAGE_DIR, exist_ok=True)
    img_response = requests.get(url)
    exstension = url.rsplit('.')[-1]
    fname = f'{settings.IMAGE_DIR}/{name}.{exstension}'
    with open(fname, 'wb') as img:
        img.write(img_response.content)
if __name__ == "__main__":
    download_image('https://media.stsci.edu/uploads/image_file/image_attachment/1/full_jpg.jpg','NASA')