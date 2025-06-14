from flask import Flask, render_template, request, send_file, session
from scanner import scan_website
from datetime import datetime
from io import BytesIO
from xhtml2pdf import pisa
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key' # Needed for session handling

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    url = request.form['url']
    if not url.startswith('http'):
        url = 'http://' + url
    
    # Perform the scan
    results = scan_website(url)

    # Store results in session for PDF download
    session['results'] = results
    session['target_url'] = url
    
    return render_template('result.html', url=url, results=results)

@app.route('/download', methods=['GET'])
def download_pdf():
    results = session.get('results', [])
    url = session.get('target_url', 'N/A')

    html = render_template('report_template.html', results=results, url=url)
    pdf = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=pdf)

    if pisa_status.err:
        return "PDF generation failed"
    
    pdf.seek(0)
    filename = f"Scan_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    return send_file(pdf, as_attachment=True, download_name=filename, mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
