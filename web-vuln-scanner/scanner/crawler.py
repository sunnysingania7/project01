# scanner/crawler.py

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_forms(url):
    """Extract all form tags from the page"""
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    return soup.find_all('form')

def get_all_links(url):
    """Extract all anchor links from the page"""
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    return [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]
