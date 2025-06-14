# scanner/logger.py

def log_vulnerability(vuln_type, url, payload, severity):
    return {"type": vuln_type, "url": url, "payload": payload, "severity": severity}
