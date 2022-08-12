# API_KEY ='mt4c1kecYJ1NqPrxxrSrBPFE'
import requests
from data.config import API_KEY

def bg_remove(FILE_NAME):
    pht=''

    response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    data={
        'image_url': FILE_NAME,
        'size': 'auto'
    },
    headers={'X-Api-Key': API_KEY},
)
    if response.status_code == requests.codes.ok:
        pht = response.content
    else:
        print("Error:", response.status_code, response.text)
    return pht
