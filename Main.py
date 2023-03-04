import requests
from datetime import datetime
from key import API_TOKEN_KEY

def BgChanger(img, bgcolor):
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg', files={'image_file':open(img, 'rb')}, 
        data={'size':'auto', 'bg_color': bgcolor}, 
        headers={'X-Api-Key': API_TOKEN_KEY},)
    
    if response.status_code == requests.codes.ok:
        with open('Output-Images/hasilnya-%s.png' %datetime.now().strftime('%Y-%m-%d_%H-%M-%S'), 'wb') as out:
            out.write(response.content)
    else:
        print('Error :', response.status_code, response.text)

BgChanger(img = 'Background-images/389564.jpg', bgcolor= 'FF0000')