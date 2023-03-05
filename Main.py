import requests
from datetime import datetime
from key import API_TOKEN_KEY #Use self-generated API in a seperated python file

def BgChanger(img, bgcolor): 
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg', files={'image_file':open(img, 'rb')}, 
        data={'size':'auto', 'bg_color': bgcolor}, 
        headers={'X-Api-Key': API_TOKEN_KEY},)
    
    if response.status_code == requests.codes.ok:
        with open('Output-Images/hasilnya-%s.png' %datetime.now().strftime('%Y-%m-%d_%H-%M-%S'), 'wb') as out:
            out.write(response.content) #output a png file with the current time on the file name
    else:
        print('Error :', response.status_code, response.text) #output if something doesn't work

BgChanger(img = 'Background-images/lowquality1.jpg', bgcolor= 'FF0000') 