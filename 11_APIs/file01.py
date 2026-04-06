import requests

def get_quotes():
    url = "https://api.freeapi.app/api/v1/public/quotes?page=1&limit=10&query=human"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        author = data['data']['data'][1]
        message = data['message']
        return author


print(get_quotes())