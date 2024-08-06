import re
import requests

from bs4 import BeautifulSoup

url = 'https://www.football.co.il/player/45897'
player_id = url.split('/')[-1]

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Successfully retrieved the page.")
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.title.string if soup.title else "No title found")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    print(response.text)