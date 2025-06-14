# scanner/scanner.py

import requests
from urllib.parse import urljoin
from .payloads import xss_payloads, sqli_payloads
from .crawler import get_all_forms
from .logger import log_vulnerability

def run_scan(url):
    results = []
    forms = get_all_forms(url)

    # XSS scanning
    for form in forms:
        for payload in xss_payloads:
            action = form.get("action")
            method = form.get("method", "get").lower()
            post_url = urljoin(url, action)
            data = {inp.get("name"): payload for inp in form.find_all("input") if inp.get("name")}

            response = (requests.post(post_url, data=data) if method == "post"
                        else requests.get(post_url, params=data))

            if payload in response.text:
                results.append(log_vulnerability("XSS", post_url, payload, "High"))

    # SQLi scanning
    for payload in sqli_payloads:
        test_url = f"{url}?input={payload}"
        resp = requests.get(test_url)
        if any(err in resp.text.lower() for err in ["sql syntax", "mysql", "syntax error"]):
            results.append(log_vulnerability("SQL Injection", test_url, payload, "Critical"))

    return results
