import requests
import os
import download_img


def fetch_spacex_last_launch(name):
    launch = check_img_last_launch_availability()

    response = requests.get(f'https://api.spacexdata.com/v3/launches/{launch}')
    url_imgs = []
    for img_url_prepare in response.json()['links']["flickr_images"]:
        url_imgs.append(img_url_prepare)

    for number, url_img in enumerate(url_imgs):
        name = f'{name}{number}'
        download_img.download_image(url_img, name)


def check_img_last_launch_availability():

    latest_launch_url = 'https://api.spacexdata.com/v3/launches/latest'

    response = requests.get(latest_launch_url)
    number_of_flight = int(response.json()["flight_number"])

    if not response.json()['links']["flickr_images"]:
        for launch in range(number_of_flight, 0, -1):
            search_response = requests.get(
                f'https://api.spacexdata.com/v3/launches/{launch}')

            if search_response.json()['links']["flickr_images"]:
                break
        return launch
    return number_of_flight


if __name__ == "__main__":
    image_name = 'spacex_'
    fetch_spacex_last_launch(image_name)
