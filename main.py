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



    
fetch_spacex_last_launch(last_launch,name)

