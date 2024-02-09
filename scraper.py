import requests
import json


ACCESS_KEY = 'ACCESS KEY'

URL = 'https://api.unsplash.com/search/photos'
PARAMS = {
    'query': 'product',  
    'client_id': ACCESS_KEY,
    'per_page': 30,
}

def fetch_images(url, params):
    response = requests.get(url, params=params)
    return response.json()

def save_image_data(data):
    image_data = [{'url': item['urls']['regular'], 'description': item['alt_description'] or 'No description available'} for item in data['results']]
    with open('image_data.json', 'w') as f:
        json.dump(image_data, f, indent=4)

if __name__ == '__main__':
    data = fetch_images(URL, PARAMS)
    save_image_data(data)
    print("Image URLs and descriptions saved to image_data.json.")

