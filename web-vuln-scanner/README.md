# Web Vulnerablity Scanner - Poject01

Welcome to the Web Vulnerability Scanner - a hands-on cybersecutity project built with python and Flask. This scanner was crafted during my internship to deepen my understanding of web security and refine my full-stack development skills. 

From crwaling target websites to injecting payloads and identifying flaws, this tool is a practical demonstration of how modern web vulnerabilites like XSS and SQL Injection can be detected. It's designed not only to scan but also to **educate**, with a clear interface and PDF reporting to document everything in a neat format. 

--- 

## Behind the Build 

The idea was simple: build a scanner that can visit a URL, explore the forms it contains, and test them with crafted payloads to identify security loopholes. As a cybersecurity enthusiast and a learner, I put together the core logic for crawling, scanning, and exporting. The tool is powered by 'BeautifulSoup', 'requests', and 'Flask', with a frontend that updates the user with a timer, countdown, and progress bar while the scan is happening. 

--- 

## Key Highlights 

- Scans for **XSS** and **SQL Injection** vulnerabilites in forms 
- Automatically crawls and logs input fields 
- Displays results directly in the brower (with bullet points)
- Wraps up everything into a downloadable **PDF report** 
- Timer + countdown + progress bar a smooth user experience 
- Clean, structured codebase and easy-to-navigate UI 

--- 

## Tech Stack 

Layer     : Tools/Techologies 
Backend   : Python, Flask 
Frontedn  : HTML, CSS, JavaScript 
Libraries : BeautifulSoup, requests, xhtml2pdf 
Extras    : Session handling, PDF rendering

--- 

## Project Structure 
``` 
web-vuln-scanner/ 
    docs/ 
        Internship Report - Web Vulnerability Scanner.pdf
    app.py                     # Flask app entry 
    scanner/                   # Core scanning engine 
        scanner.py             # XSS + SQLi detection logic 
        crawler.py             # Form grabbing 
        payloads.py            # Vulnerability test payloads 
        logger.py              # Scan logs 
        __init__.py 
    templates/                 # HTML frontnd 
        index.html 
        result.html 
        report_template.html 
    static/                    # Styling files 
        sytle.css 
        result.css 
    reports/                   # Styling files 
    requirments.txt            # Auto-generated PDF reports 
    README.md                  # This file 
```

--- 

## How to Run It

```bash 
git clone https://github.com/sunnysingania7/project01.git
cd project01/web-vuln-scanner
pip install -r requirements.txt 
python app.py 
``` 

Then visit: `http://127.0.0.1:5000` in your browser and start scanning. 

--- 

## Internship Reflection 

This project was a major part of my internship submission. All scanning logic, payload handling, and security flow design were develop independently by me. From code to concept, I explored how real-world sites can be tested ethically  for vulnerabilities. 

*Special thanks to OpenAI's ChatGPT* - while all logic was written and understood by me, ChatGPT helped stramline some of folder organization, frontend enhancements, and syntax optimizations. 

--- 

## License 

This project is open-source under the MIT License. Feel free to use, learn from, and improve it further. 

--- 

## Contribute 

If you're into web security or ethical hacking, feel free to fork the repo, suggest improvements, or add new vulnerability checks like CSRF or Open Redirects. 

--- 

## GitHub Repo 

[https://github.com/sunnysingania7/project01]
(https://github.com/sunnysingania7/project01)

--- 

## 📄 Project Report

You can view the detailed project report here:  
[Download Internship Report (PDF)]
(./docs/Internship_Report_Web_Vulnerability_Scanner.pdf)

--- 

Thank you for visiting!
