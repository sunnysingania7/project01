# scanner/logger.py

def log_vulnerability(vuln_type, url, payload, severity):
    """Return a dictionary of the found vulnerability"""
    return {
        "type": vuln_type,
        "url": url,
        "payload": payload,
        "serverity": serverity
    }
