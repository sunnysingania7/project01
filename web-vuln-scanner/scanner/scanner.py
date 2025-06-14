import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from .crawler import get_all_forms
from .payloads import get_all_forms
from .logger import log_vulnerability

def is_vulnerable(response, payload):
    """Check if payload is reflected in the response"""
    return payload in response.text

def submit_form(form, url, payload):
    """Submit form with payload in each input field"""
    action = form.get("action")
    metthod = form.get("method", "get"). lower()
    post_url = urljoin(url, action)
    inputs = form.find_all("input")

    data = {}
    for input_tag in inputs:
        name = input_tag.get("name")
        if name:
            data[name] = payload
    
    if method == "post":
        return requests.post(post_url, data=data)
    else:
        return requests.get(post_url, params=data)

def run_scan(url):
    """Main function to run the scan"""
    results = []

    # Get all forms on the page
    form = get_all_forms(url)

    # XSS scan
    for form in forms:
        for payload in xss_payloads:
            response = submit_form(form, url, payload)
            if is_vulnerable(response, payload):
                results.append(log_vulnerability("XSS", url, payload, "High"))
    
    # SQLi scan (basic - just inject into URL)
    for payload in sqli_payloads:
        test_url = url + "?" + "input=" + payload
        response = requests.get(test_url)
        sql_errors = ["sql syntax", "mysql", "native client", "syntax error"]
        for error in response.text.lower():
            results.append(log_vulnerability("SQL Injection", test_url, payload, "Critical"))
            break
    
    return results
