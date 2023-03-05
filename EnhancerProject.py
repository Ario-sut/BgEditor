import requests
from datetime import datetime
from key import API_TOKEN_KEY_2

def enhancer(img):
  response = requests.post(
    'https://www.cutout.pro/api/v1/matting?mattingType=18',
    files={'file': open(img, 'rb')},
    headers={'APIKEY': API_TOKEN_KEY_2},
  )
  if response.status_code == requests.codes.ok: 
    with open('Output-Images/hasilnya-%s.png' %datetime.now().strftime('%Y-%m-%d_%H-%M-%S'), 'wb') as out:
        out.write(response.content)
  else:
     print('Error: ', response.status_code, response.text)

enhancer(img ='Background-Images/quote1.png')