# API_KEY ='mt4c1kecYJ1NqPrxxrSrBPFE'
import requests


def bg_remove(FILE_NAME):
    pht=''
    API_KEY ='mt4c1kecYJ1NqPrxxrSrBPFE'


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
