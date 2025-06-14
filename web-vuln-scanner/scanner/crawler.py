# scanner/crawler.py

import requests
from bs4 import BeautifulSoup

def get_all_forms(url):
    try:
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, "html.parser")
        return soup.find_all("form")
    except Exception as e:
        print(f"[!] Could not fetch forms from {url}: {e}")
        return []
