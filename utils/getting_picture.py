import requests

def get_picture(pic_url):
    response = requests.get(pic_url)
    return response.content