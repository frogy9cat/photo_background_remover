import requests

def bot_pic():
    pic_url = "https://www.gosrf.ru/wp-content/uploads/2022/04/ff0e0789ee4741a3b7a03ea0b2c0b41b.jpg"
    response = requests.get(pic_url)
    return response.content