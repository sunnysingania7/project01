# scanner/payloads.py 

# List of payloads for different types of vulnerabilites 

xss_payloads = [
    '<script>alert(1)</script>',
    '"><img src=x onerror=alert(1)',
]

sqli_payloads = [
    "' OR '1'='1'",
    "'; DROP TABLE users; --",
]

# You can add more later!
