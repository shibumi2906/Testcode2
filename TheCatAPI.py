
import requests
from config import CAT_API_URL, CAT_API_KEY

def get_random_cat_image():
    headers = {'x-api-key': CAT_API_KEY}
    response = requests.get(CAT_API_URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data[0]['url']
    else:
        return None
