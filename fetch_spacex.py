import requests,os
import download_img

def fetch_spacex_last_launch(name):
    launch=check_img_last_launch_availability()
    response = requests.get(f'https://api.spacexdata.com/v3/launches/{launch}')
    url_imgs = []
    for img_url_prepare in response.json()['links']["flickr_images"]:
        url_imgs.append(img_url_prepare)

    for number, url_img in enumerate(url_imgs):
        name = f'{name}{number}'
        download_img.download_image(url_img, name)

def check_img_last_launch_availability():

    latest_launch_url='https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(latest_launch_url)
    number_of_flight=int(response.json()["flight_number"])
    
    if not bool(response.json()['links']["flickr_images"]):
        launch_with_photo=0
        while True:
            launch_with_photo=number_of_flight-1
            search = requests.get(f'https://api.spacexdata.com/v3/launches/{launch_with_photo}')
            if bool(search):
                break
        return launch_with_photo
    return number_of_flight


if __name__ == "__main__":
    image_name='spacex_'    
    fetch_spacex_last_launch(image_name)