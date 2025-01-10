import requests

def duck(bot, chat_id):
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    image_url = data['url']
    bot.send_message(chat_id, image_url)
